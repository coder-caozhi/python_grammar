# ============================================================================
# 学习目的：从聊天响应提取文本，便于下游处理
# 技术讲解：PromptValue → AIMessage → StrOutputParser → str
# 阅读路线：模板填值 → 模型输出 → parser.invoke → 检查类型
# 当前代码要注意：不是把任意 Python 对象 str() 一遍；它处理 LangChain 支持的文本/消息输出，不能当作万能序列化器
# 动手验证：比较解析前的消息元数据与解析后保留的信息
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
字符串解析器StrOutputParser
它是LangChain中最简单的输出解析器，它可以简单地将任何输入转换为字符串。
从结果中提取content字段转换为字符串输出。
"""
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model
from loguru import logger

# 创建聊天提示模板，包含系统角色设定和用户问题输入
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}，请简短回答我提出的问题"),
        ("human", "请回答:{question}")
    ]
)

# 使用指定的角色和问题生成具体的提示内容
# 【理解这一行】模板 invoke 接收变量字典并产生 PromptValue；同名方法不代表在调用模型。
prompt = chat_prompt.invoke({"role": "AI助手", "question": "什么是LangChain，简洁回答100字以内"})
logger.info(prompt)

# 初始化聊天模型
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
# 创建字符串输出解析器，用于解析模型返回的结果
# 【理解这一行】把支持的文本/消息输出变成文本，方便下一步传递；消息元数据不会作为正文保留。
parser = StrOutputParser()

# 打印解析后的结构化结果
# 【理解这一行】解析器处理上游结果，输出类型由所选解析器决定；这里没有新增模型推理。
response = parser.invoke(result)
logger.info(f"解析后的结构化结果:\n{response}")
logger.info("\n")
# 打印类型
logger.info(f"结果类型: {type(response)}")