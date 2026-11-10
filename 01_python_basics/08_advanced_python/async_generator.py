"""异步生成器：把 yield 与 await 结合，模拟逐段接收模型回答。"""

import asyncio
from contextlib import aclosing


async def stream_answer(cleanup_events):
    try:
        for chunk in ["生成器", "可以", "逐段产出结果"]:
            await asyncio.sleep(0.02)  # 模拟下一段文本尚未到达
            yield chunk
    finally:
        cleanup_events.append("closed")
        print("\n流已关闭，资源已清理")


async def main():
    print("一、async for 逐段获取异步生成器的结果")
    cleanup = []
    chunks = []
    async for chunk in stream_answer(cleanup):
        print(chunk, end="", flush=True)
        chunks.append(chunk)
    assert "".join(chunks) == "生成器可以逐段产出结果"
    assert cleanup == ["closed"]

    print("\n二、提前停止时，用 aclosing 确保及时关闭")
    cleanup = []
    # async for 中的 break 本身不保证立刻关闭异步生成器。
    async with aclosing(stream_answer(cleanup)) as stream:
        async for chunk in stream:
            print("只看第一段：", chunk)
            break
    assert cleanup == ["closed"]

    # 普通生成器：def + yield，用 for / next 消费。
    # 协程：async def（不含 yield），用 await 等待一个最终结果。
    # 异步生成器：async def + yield，用 async for / anext 消费。
    # 不能对异步生成器直接使用 list() 或 await stream。
    # 本例只模拟流式文本，不依赖 LangChain 或外部 API。
    # 练习：模拟分三页获取数据，每页 await 等待，再逐条 yield。
    print("异步生成器案例检查通过")


if __name__ == "__main__":
    asyncio.run(main())
