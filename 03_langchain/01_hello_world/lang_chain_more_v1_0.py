# LangChain1.0+版本使用方式,目前主流,多模型共存


# 1.导入依赖
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
# .env文件读取
load_dotenv()

# 2.实例化模型
# model = init_chat_model(
#     model="deepseek-chat",
#     model_provider="openai",
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )
#
# # 3.调用模型
# print(model.invoke("你是谁").content)
#
# print("*" * 70)

# 4.实例化模型v2
"""
说明：
这里通过 OpenAI 兼容接口连接 DeepSeek，因此显式设置 model_provider="openai"。
"""
model = init_chat_model(
    model="deepseek-chat", # deepseek-chat 对应 DeepSeek-V3.2 的非思考模式
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 5.调用模型v2
print(model.__dict__)
print(model.invoke("你是谁").content)