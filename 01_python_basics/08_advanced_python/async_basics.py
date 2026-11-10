"""异步基础：协程对象、await、任务，以及顺序等待与并发等待。

只用 asyncio.sleep 模拟网络等待，不调用外部服务。
"""

import asyncio
from time import perf_counter


async def fetch_course(name: str, delay: float):
    print(f"开始获取：{name}")
    # await 在这里等待未完成的操作，让事件循环有机会运行其他任务。
    # 不要在这里使用 time.sleep，它会阻塞当前事件循环线程。
    await asyncio.sleep(delay)
    print(f"完成获取：{name}")
    return f"{name}资料"


async def main():
    print("一、调用 async def 得到协程对象；调用本身不会执行函数体")
    coroutine = fetch_course("Python", 0.05)
    print("协程已创建，下面 await 才开始运行")
    assert await coroutine == "Python资料"
    # 同一个协程对象不能重复 await；需要再次调用函数创建新的协程对象。

    print("\n二、连续 await 是顺序执行")
    start = perf_counter()
    first = await fetch_course("FastAPI", 0.15)
    second = await fetch_course("LangChain", 0.10)
    sequential = perf_counter() - start

    print("\n三、先创建任务，再一起等待，两个等待过程可以重叠")
    start = perf_counter()
    task_a = asyncio.create_task(fetch_course("FastAPI", 0.15))
    task_b = asyncio.create_task(fetch_course("LangChain", 0.10))
    results = await asyncio.gather(task_a, task_b)
    concurrent = perf_counter() - start
    # LangChain 更早完成，但 gather 的结果按传入顺序排列。
    assert results == [first, second] == ["FastAPI资料", "LangChain资料"]
    print(f"顺序等待 {sequential:.3f}s；并发等待 {concurrent:.3f}s")
    # 时间随机器负载变化，不用“并发一定快多少”做断言。
    # 异步并发适合等待型任务，不会自动让 CPU 密集计算变快。
    # 在 FastAPI 的 async 路由里直接 await；不要再嵌套 asyncio.run()。

    # 练习：并发获取三门课程，保证输出结果依然按传入课程顺序排列。
    print("异步基础案例检查通过")


if __name__ == "__main__":
    # 独立脚本的事件循环入口；只在最外层使用。
    asyncio.run(main())
