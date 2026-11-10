"""异步任务管理：Semaphore 限流、超时取消、异常结果与清理。"""

import asyncio


async def limited_requests():
    semaphore = asyncio.Semaphore(2)
    active = 0
    peak = 0

    async def request(number):
        nonlocal active, peak
        async with semaphore:  # 没有名额的任务在这里等待
            active += 1
            peak = max(peak, active)
            try:
                await asyncio.sleep(0.02)
                return number * 10
            finally:
                active -= 1

    results = await asyncio.gather(*(request(i) for i in range(5)))
    assert results == [0, 10, 20, 30, 40]
    assert peak == 2 and active == 0
    print("限流结果：", results, "最高同时运行数：", peak)
    # Semaphore 限制同时进入代码段的任务数，不等于每秒请求数限制。


async def timeout_example():
    cleaned = asyncio.Event()
    started = asyncio.Event()

    async def slow_operation():
        started.set()
        try:
            await asyncio.sleep(10)
        finally:
            # 取消发生后仍要释放资源。真实场景可在这里关闭连接。
            cleaned.set()

    task = asyncio.create_task(slow_operation())
    await started.wait()
    try:
        # 到时间会取消这里被等待的任务，并等待它处理取消。
        await asyncio.wait_for(task, timeout=0.03)
    except TimeoutError:
        assert cleaned.is_set() and task.cancelled()
        print("任务已超时取消，并完成 finally 清理")
    else:
        raise AssertionError("这个慢任务应该超时")
    # wait_for 不保证在指定毫秒数精确返回：取消和清理也需要时间。
    # 不要吞掉 CancelledError，否则会破坏上层任务的取消行为。


async def failure_example():
    async def request(number):
        await asyncio.sleep(0)
        if number == 2:
            raise ValueError("模拟第 2 个请求失败")
        return number * 10

    # 本例希望一个失败不影响其他结果，所以明确收集异常并逐个处理。
    results = await asyncio.gather(*(request(i) for i in range(3)), return_exceptions=True)
    assert results[:2] == [0, 10] and isinstance(results[2], ValueError)
    for index, result in enumerate(results):
        if isinstance(result, BaseException):
            print(f"请求 {index} 失败：{result}")
        else:
            print(f"请求 {index} 成功：{result}")
    # 默认 gather 会传播异常，但不会自动取消其他任务。


async def main():
    await limited_requests()
    await timeout_example()
    await failure_example()
    # 练习：把并发上限改为 3、请求数改为 8，检查 peak 与最终结果。
    print("异步任务管理案例检查通过")


if __name__ == "__main__":
    asyncio.run(main())
