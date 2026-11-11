# ============================================================================
# 学习目的：并发等待多个模型响应并按输入顺序读取
# 技术讲解：abatch 返回协程，await 后得到响应列表，zip 保持问题答案对应
# 阅读路线：questions → await abatch → 遍历结果
# 当前代码要注意：并发数量不等于服务允许的速率；需要时通过 RunnableConfig 控制 max_concurrency
# 动手验证：与同步 batch 对比调用语法，找出必须 await 的位置
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

questions = [
    "什么是redis?简洁回答，字数控制在100以内",
    "Python的生成器是做什么的？简洁回答，字数控制在100以内",
    "解释一下Docker和Kubernetes的关系?简洁回答，字数控制在100以内"
]


# 3.异步批量调用大模型（定义异步函数封装异步操作）
# abatch() 是异步方法，需要基于 async/await 语法构建异步程序，并用 asyncio 驱动运行
async def async_batch_call():
    # 调用 model.abatch() 异步批量处理请求，需用 await 修饰（关键）
    # 【理解这一行】异步执行多个输入；await 后得到结果列表，顺序与输入列表对应。
    response = await model.abatch(questions)
    print(f"响应类型：{type(response)}")

    # 遍历结果并格式化输出（与原来的同步版本格式一致）
    for q, r in zip(questions, response):
        print(f"问题：{q}\n回答：{r.content}\n")


# 4.运行异步函数
if __name__ == "__main__":
    asyncio.run(async_batch_call())