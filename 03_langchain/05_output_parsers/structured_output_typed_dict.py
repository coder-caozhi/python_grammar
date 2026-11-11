# ============================================================================
# 学习目的：使用模型包装器请求结构化结果
# 技术讲解：TypedDict 描述嵌套 animals 列表；with_structured_output 根据模型支持构造结构化调用
# 阅读路线：定义 Animal/AnimalList → 包装模型 → invoke → 字典
# 当前代码要注意：TypedDict 本身不提供 Pydantic 式运行时校验；具体结构化策略取决于集成和模型能力
# 动手验证：逐项检查 animals 中是否都有 animal 和 emoji
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from typing import TypedDict, Annotated
from langchain.chat_models import init_chat_model

# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

class Animal(TypedDict):
    animal: Annotated[str, "动物"]
    emoji: Annotated[str, "表情"]

class AnimalList(TypedDict):
    animals: Annotated[list[Animal], "动物与表情列表"] # List<Animal>

messages = [{"role": "user", "content": "任意生成三种动物，以及他们的 emoji 表情"}]

# 【理解这一行】根据 schema 包装模型输出；具体策略和支持程度取决于供应商与模型集成。
llm_with_structured_output = llm.with_structured_output(AnimalList)
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
resp = llm_with_structured_output.invoke(messages)
print(resp)


