# ============================================================================
# 学习目的：读懂兼容接口的最小模型调用
# 技术讲解：服务地址、模型名、凭据共同决定请求目标
# 阅读路线：加载配置 → ChatOpenAI → invoke 打印消息
# 当前代码要注意：当前代码实际连接 DeepSeek，没有使用 Ollama 的本地地址或专用客户端
# 动手验证：与 02_model_io 中的客户端配置逐项对照
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install -qU langchain-ollama
# pip install -U ollama

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()

# 设置本地模型，不使用深度思考
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
# 打印结果，
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(model.invoke("什么是LangChain，100字以内回答"))

