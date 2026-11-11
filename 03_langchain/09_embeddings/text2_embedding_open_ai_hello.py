# ============================================================================
# 学习目的：用 OpenAI 兼容客户端调用通义嵌入接口
# 技术讲解：SDK 名称与实际服务商解耦；base_url 指向 DashScope
# 阅读路线：读取 aliQwen-api → embeddings.create → 序列化响应
# 当前代码要注意：使用 embedding 模型，不是聊天模型；本例未调用 load_dotenv
# 动手验证：对比聊天接口的 messages 与这里的 input
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587

import os
from openai import OpenAI

input_text = "衣服的质量杠杠的"

# 【理解这一行】创建原生 OpenAI SDK 客户端；接下来要从 SDK 的响应结构取值，而非 LangChain AIMessage。
client = OpenAI(
    # 若没有配置环境变量，请用阿里云百炼API Key将下行替换为：api_key="sk-xxx",
    # 新加坡和北京地域的API Key不同。获取API Key：https://help.aliyun.com/zh/model-studio/get-api-key
    api_key=os.getenv("aliQwen-api"),
    # 以下是北京地域base-url，如果使用新加坡地域的模型，需要将base_url替换为：https://dashscope-intl.aliyuncs.com/compatible-mode/v1
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)

completion = client.embeddings.create(
    model="text-embedding-v4",
    input=input_text
)

print(completion.model_dump_json())