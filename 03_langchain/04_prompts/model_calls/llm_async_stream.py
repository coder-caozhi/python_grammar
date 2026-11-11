# ============================================================================
# 学习目的：把异步生成器用于模型流式输出
# 技术讲解：astream 返回异步迭代对象，用 async for 消费而不是普通 for
# 阅读路线：构造消息 → astream → async for → chunk.content
# 当前代码要注意：创建流对象与消费流是两步；不要直接 await 一个异步生成器对象
# 动手验证：与 llm_stream.py 对比 for 和 async for 的区别
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 1.导入依赖（新增 asyncio 用于运行异步程序）
import os
import asyncio
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage, SystemMessage

# 通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()

# 2.实例化模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 构建消息列表
messages = [
    SystemMessage(content="你叫小问，是一个乐于助人的AI人工助手"),
    HumanMessage(content="你是谁")
]


# 3.异步流式调用大模型（定义异步函数）
async def async_stream_call():
    # astream 返回异步生成器，无需 await 修饰，直接赋值
    # 【理解这一行】返回异步分片迭代对象，后面使用 async for 逐块消费。
    response = model.astream(messages)
    print(f"响应类型：{type(response)}") # 响应类型：<class 'async_generator'>

    # 异步遍历异步生成器（必须使用 async for，不可用普通 for）
    # 异步遍历异步生成器（必须使用 async for，不可用普通 for）
    # 异步遍历异步生成器（必须使用 async for，不可用普通 for）
    async for chunk in response:
        # 刷新缓冲区，实现流式打印（无换行、即时输出）
        print(chunk.content, end="", flush=True)
    print("\n")

# 4.运行异步函数
if __name__ == "__main__":
    asyncio.run(async_stream_call())
