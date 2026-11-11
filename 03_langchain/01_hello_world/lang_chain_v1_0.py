# ============================================================================
# 学习目的：认识 init_chat_model 统一模型初始化入口
# 技术讲解：model_provider 选择适配器，base_url 选择服务端地址，model 选择远端模型
# 阅读路线：两次初始化 → 各调用一次 → 比较返回文本
# 当前代码要注意：两段代码均调用 DeepSeek，不是不同供应商的对比；每次 invoke 都会发送独立请求
# 动手验证：将两段的提示词设为不同内容，区分客户端配置与问题内容
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# LangChain1.0+版本使用方式,目前主流

# 1.导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# 2.实例化模型
# 什么是关键字参数 k1=v1 ,k2 = v2
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv(encoding='utf-8')

# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 3.调用模型
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(model.invoke("你是谁").content)

# model_provider="openai",
# ValueError: Unable to infer model provider for model="deepseek-chat"', please specify model_provider directly.

print("*" * 50)


#通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
model2 = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com")

# 3.调用模型
print(model2.invoke("你是谁").content)
