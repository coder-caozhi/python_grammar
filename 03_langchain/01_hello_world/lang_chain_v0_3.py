# ============================================================================
# 学习目的：用 ChatOpenAI 完成一次最小聊天调用
# 技术讲解：OpenAI 兼容协议不等于 OpenAI 提供的模型；实际服务由 base_url 和 model 决定
# 阅读路线：读取 .env → 建立客户端 → invoke → 观察消息对象和 content
# 当前代码要注意：文件名记录课程版本；当前 ChatOpenAI 也可能在新版集成包中使用，不能单凭文件名判断依赖版本
# 动手验证：比较 print(response) 与 print(response.content) 的内容差异
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# LangChain0.3版本使用方式,了解即可，目前再用

# 1.导入依赖
from langchain_openai import ChatOpenAI
from openai import OpenAI
import os
from dotenv import load_dotenv

# 第1版：硬编码写死
# llm = ChatOpenAI(
#     model="deepseek-chat",
#     # 硬编码写死
#     api_key="你自己的api-key",  # 平台提供的 API-Key
#     base_url="https://api.deepseek.com"
# )


# 第2版：配置进环境变量
# llm = ChatOpenAI(
#     model="deepseek-chat",
#     # 配置进环境变量
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )

# 第3版：通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
# 加载.env文件中的环境变量（指定编码，避免中文乱码）
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv(encoding='utf-8')

# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
llm = ChatOpenAI(
    model="deepseek-chat",
    # 配置进环境变量
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# # 2.提供问题，并调用llm
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
response = llm.invoke("你是谁")

print(response)#元数据
print()
print(response.content)

print()

