"""
使用ChatPromptTemplate构造方法直接实例化
实例化时需要传入messages: Sequence[MessageLikeRepresentation]
messages 参数支持如下格式：
	tuple 构成的列表，格式为[(role, content)]
	dict 构成的列表，格式为[{“role”:... , “content”:...}]
	Message 类构成的列表
"""

import os
from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


def get_deepseek_api_key() -> str:
    """读取 DeepSeek API Key。"""
    candidates = [os.getenv("DEEPSEEK_API_KEY")]
    for value in candidates:
        if value:
            return value
    raise RuntimeError(
        "未配置 DeepSeek API Key。请在项目根目录的 .env 文件中设置 "
        "DEEPSEEK_API_KEY。"
    )


chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

prompt = chatPromptTemplate.format_messages(
    name="小谷AI", thing="AI", user_input="7 + 5等于多少"
)
print(prompt)

api_key = get_deepseek_api_key()
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=api_key,
    base_url="https://api.deepseek.com",
)
print()
print("======================")

result = llm.invoke(prompt)
print(result)
print(result.content)