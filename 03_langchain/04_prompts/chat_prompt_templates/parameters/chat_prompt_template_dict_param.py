# ============================================================================
# 学习目的：用 role/content 字典声明聊天消息模板
# 技术讲解：字典是一种消息表示，模板会把变量填入对应角色的内容
# 阅读路线：from_messages 接收字典列表 → format_messages → 输出消息
# 当前代码要注意：模板变量的名称必须与传入键一致；这里没有模型调用
# 动手验证：把 name 换成另一个值，观察只改变了哪条消息
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
列表参数格式是dict类型

	dict 构成的列表，格式为[{“role”:... , “content”:...}]
chat_prompt = ChatPromptTemplate(
    [
        {"role": "system", "content": "你是AI助手，你的名字叫{name}。"},
        {"role": "user", "content": "请问：{question}"}
    ]
)
"""

from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，用于构建AI助手的对话上下文
# 该模板包含两个消息：AI助手的自我介绍和用户问题
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
chat_prompt = ChatPromptTemplate.from_messages(
    [
        {"role": "system", "content": "你是AI助手，你的名字叫{name}。"},
        {"role": "user", "content": "请问：{question}"}
    ]
)

# 格式化聊天提示模板，填充具体的助手名称和问题内容
# 参数name: AI助手的名字
# 参数question: 用户提出的问题
# 返回值: 格式化后的消息列表
# 【理解这一行】把变量值填入消息模板，得到消息列表；这一步本身不访问模型服务。
message = chat_prompt.format_messages(name="小问", question="什么是LangChain")

# 打印格式化后的消息内容
print(message)