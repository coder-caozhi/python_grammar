# ============================================================================
# 学习目的：理解单次异步模型调用与协程入口
# 技术讲解：ainvoke 需要 await；asyncio.run 用于独立脚本最外层
# 阅读路线：创建模型 → async main → await ainvoke → 输出内容块
# 当前代码要注意：单个 await 不自动产生多个并行请求；原末尾说明的并发效果还需要调度多个任务
# 动手验证：解释在 FastAPI async 路由里为何直接 await 而不是再 asyncio.run
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 1.导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import asyncio
from langchain.messages import HumanMessage,SystemMessage



#通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
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

async def main():
    # 异步调用一条请求
    # 【理解这一行】等待单个异步调用；一个 await 不等于多个请求已并发启动。
    response = await model.ainvoke("解释一下LangChain是什么，简洁回答100字以内")
    print(f"响应类型：{type(response)}")
    print(response.content_blocks)

# 4.运行异步函数
if __name__ == "__main__":
    asyncio.run(main())

'''
LangChain 提供 ainvoke() 异步调用接口，用于在 异步环境（async/await） 中高效并行地执行模型推理。
它的核心作用是：让你同时调用多个模型请求而不阻塞主线程 —— 特别适合大批量请求或 Web 服务场景（如 FastAPI）
'''
