# ============================================================================
# 学习目的：把普通函数嵌入 LCEL 并观察中间结果
# 技术讲解：RunnableLambda 包装函数；LCEL 也能把合适的普通 callable 转为 Runnable
# 阅读路线：第一条链输出 → debug_print 改为 input 字典 → 第二条链
# 当前代码要注意：debug_print 不只是打印，还改变数据结构；若忘记 return 下游将收到 None
# 动手验证：比较显式 debug_node 与直接放函数的两种写法
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
RunnableLambda-函数链
将普通Python函数融入Runnable流程.
"""
from langchain.chat_models import init_chat_model
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableLambda
from loguru import logger
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.0,
    base_url="https://api.deepseek.com"
)


# 一个简单的打印函数，调试用
def debug_print(x):
    logger.info(f"中间结果:{x}")
    # 【理解这一行】这个 return 是数据适配的关键：下游模板要的是 input 字典，不能只打印却不返回。
    return {"input": x}

# 子链1提示词
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
prompt1 = ChatPromptTemplate.from_messages([
    ("system", "你是一个知识渊博的计算机专家，请用中文简短回答"),
    ("human", "请简短介绍什么是{topic}")
])
# 子链1解析器
# 【理解这一行】把支持的文本/消息输出变成文本，方便下一步传递；消息元数据不会作为正文保留。
parser1 = StrOutputParser()
# 子链1：生成内容
chain1 = prompt1 | model | parser1

# 子链2提示词
prompt2 = ChatPromptTemplate.from_messages([
    ("system", "你是一个翻译助手，将用户输入内容翻译成英文"),
    ("human", "{input}")
])
# 子链2解析器
parser2 = StrOutputParser()

# 子链2：翻译内容
chain2 = prompt2 | model | parser2
# 创建一个可运行的调试节点，用于打印中间结果
# 【理解这一行】让普通 Python 函数遵循 Runnable 接口，便于接入 invoke/管道。
debug_node = RunnableLambda(debug_print)

# 构建完整的处理链，将chain1、调试打印和chain2串联起来
full_chain = chain1 | debug_print | chain2

# 调用复合链
# 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
result1 = full_chain.invoke({"topic": "langchain"})
logger.info(f"最终结果111:{result1}")


# 构建完整的处理链，将chain1、调试打印和chain2串联起来
full_chain = chain1 | debug_node | chain2

# 调用复合链
result2 = full_chain.invoke({"topic": "langchain"})
logger.info(f"最终结果222:{result2}")
