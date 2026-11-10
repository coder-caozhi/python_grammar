from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
chatLLM = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    # other params...
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}]

response = chatLLM.invoke(messages)

print(response.content)