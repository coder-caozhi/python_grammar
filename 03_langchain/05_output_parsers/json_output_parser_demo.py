# ============================================================================
# 学习目的：把模型 JSON 文本解析成 Python 数据
# 技术讲解：提示词约定 q/a 字段，JsonOutputParser 执行 JSON 解析
# 阅读路线：构造 JSON 要求 → 模型回复 → parser.invoke
# 当前代码要注意：本例期望得到 dict，但合法 JSON 也可以是 list；解析成功不代表字段内容符合业务要求
# 动手验证：观察返回值有没有 q/a，思考还需怎样检查字段
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
JsonOutputParser，即JSON输出解析器，
是一种用于将大模型的自由文本输出转换为结构化JSON数据的工具。

本案例是：指定提示词指明返回 json 格式
"""

from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model
from loguru import logger

# 创建聊天提示模板，包含系统角色设定和用户问题输入
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
chat_prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个{role}，请简短回答我提出的问题，结果返回json格式，q字段表示问题，a字段表示答案。"),
    ("human", "请回答:{question}")
])

# 使用指定的角色和问题生成具体的提示内容
# 【理解这一行】模板 invoke 接收变量字典并产生 PromptValue；同名方法不代表在调用模型。
prompt = chat_prompt.invoke({"role": "AI助手", "question": "什么是LangChain，简洁回答100字以内"})
logger.info(prompt)

# 初始化模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 调用模型获取回答结果
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
result = model.invoke(prompt)
logger.info(f"模型原始输出:\n{result}")

print("*" *  60)


# 创建JSON输出解析器实例
# 【理解这一行】解析 JSON 文本为 Python 数据；格式要求与业务字段校验是不同层面的事情。
parser = JsonOutputParser()
# 调用解析器处理结果数据，将输入转换为JSON格式的响应
# 【理解这一行】解析器处理上游结果，输出类型由所选解析器决定；这里没有新增模型推理。
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")
logger.info("\n")
# 打印类型
logger.info(f"结果类型: {type(response)}") # <class 'dict'>