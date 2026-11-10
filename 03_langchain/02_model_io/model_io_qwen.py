#pip install langchain-community
#pip install dashscope

import os
from dotenv import load_dotenv

load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

chatLLM = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    streaming=True,
    base_url="https://api.deepseek.com",
    # other params...
)
# 打印结果
print(chatLLM.invoke("你是谁"))

print("*" * 60)

res = chatLLM.stream([HumanMessage(content="你好，你是谁")])
for r in res:
    print("chat resp:", r.content)
