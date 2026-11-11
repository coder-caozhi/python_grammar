# ============================================================================
# 学习目的：区分聊天模板的三种输出形式
# 技术讲解：format_messages 返回消息列表；invoke 返回 ChatPromptValue；format 返回文本
# 阅读路线：创建模板 → 依次调用三个方法 → 比较输出结构
# 当前代码要注意：文件前部把 from_messages 描述成替换方法；实际 from_messages 是构造模板，format_messages 才填充变量
# 动手验证：比较三种结果的 type，并说明模型可接受哪种输入
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
from_messages
作用：将模板变量替换后，直接生成消息列表（List[BaseMessage]），
一般包含：SystemMessage``HumanMessage``AIMessage
常用场景：用于手动查看或调试 Prompt 的最终“消息结构”或者自己拼接进 Chain。

实例化时需要传入messages: Sequence[MessageLikeRepresentation]
messages 参数支持如下格式：
	tuple 构成的列表，格式为[(role, content)]
template = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)
	dict 构成的列表，格式为[{“role”:... , “content”:...}]
chat_prompt = ChatPromptTemplate(
    [
        {"role": "system", "content": "你是AI助手，你的名字叫{name}。"},
        {"role": "user", "content": "请问：{question}"}
    ]
)
	Message 类构成的列表
"""

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，包含系统角色设定和用户问题格式
# 系统消息定义了AI助手的角色，人类消息定义了用户问题的格式
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
chat_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是一个{role}，请回答我提出的问题"),
        ("human", "请回答:{question}")
    ]
)

# 格式化聊天提示模板，填充角色和问题参数
# 参数role: 指定AI助手的角色身份
# 参数question: 用户提出的具体问题
# 返回值: 格式化后的消息列表
#prompt_value = chat_prompt.format_messages(role="python开发工程师", question="冒泡排序怎么写")
# 【理解这一行】把变量值填入消息模板，得到消息列表；这一步本身不访问模型服务。
prompt_value = chat_prompt.format_messages(**{"role": "python开发工程师", "question": "堆排序怎么写"})
# 打印格式化后的提示消息
print(prompt_value)

print()
# 使用指定的角色和问题参数填充模板，生成具体的提示内容
# role: 指定AI扮演的角色
# question: 用户提出的具体问题
# 【理解这一行】模板 invoke 接收变量字典并产生 PromptValue；同名方法不代表在调用模型。
prompt_value2 = chat_prompt.invoke({"role": "python开发工程师", "question": "堆排序怎么写"})
# 输出生成的提示内容
print(prompt_value2.to_string())

print()

# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt_value3 = chat_prompt.format(**{"role": "python开发工程师", "question": "快速排序怎么写"})
# 输出生成的提示内容
print(prompt_value3)


# llm = init_chat_model(
#     model="deepseek-chat",
#     model_provider="openai",
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )
# print()
# print("======================")
#
# result = llm.invoke(prompt_value)
# print(result)
# print(result.content)