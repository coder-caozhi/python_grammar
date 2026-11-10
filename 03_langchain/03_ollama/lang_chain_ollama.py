# pip install -qU langchain-ollama
# pip install -U ollama

import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

# 设置本地模型，不使用深度思考
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)
# 打印结果，
print(model.invoke("什么是LangChain，100字以内回答"))

