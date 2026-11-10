# 1.导入依赖
import os
from dotenv import load_dotenv

load_dotenv()
from langchain.chat_models import init_chat_model

# 2.实例化模型
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 3.调用模型
print(model.invoke("你是谁").content)