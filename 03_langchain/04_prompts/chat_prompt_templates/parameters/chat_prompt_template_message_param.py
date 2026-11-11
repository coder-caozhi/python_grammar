# ============================================================================
# 学习目的：区分已经构造好的消息与可格式化的消息模板
# 技术讲解：SystemMessage/HumanMessage 实例是具体消息，不会自动把内容中的花括号变成模板字段
# 阅读路线：创建消息实例 → 放入 ChatPromptTemplate → format_messages → 检查内容
# 当前代码要注意：本例的 {name}、{question} 会保留为字面文本；要替换可改用角色元组或 MessagePromptTemplate，当前代码未改动
# 动手验证：与 tuple_param 案例比较最终消息中的花括号是否消失
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
message 类型

System/Human/AIMessage 是 langchain 中用于构建不同角色的一个类。
它通常用于创建聊天消息的一部分，特别是当你构建一个多轮对话的 prompt 模板时，区分系统、AI、和人类消息
"""
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.prompts import ChatPromptTemplate

# 创建聊天提示模板，用于构建AI助手的对话上下文
# 该模板包含两个消息：AI助手的自我介绍和用户问题
# 【理解这一行】关键区别：传入的是具体消息对象；下面 content 中的花括号不会按模板变量替换。
chat_prompt = ChatPromptTemplate(
    [
        SystemMessage(content="你是AI助手，你的名字叫{name}。"),
        HumanMessage(content="请问：{question}")
    ]
)

# 格式化聊天提示模板，填充具体的助手名称和问题内容
# 参数name: AI助手的名字
# 参数question: 用户提出的问题
# 返回值: 格式化后的消息列表
# 【理解这一行】把变量值填入消息模板，得到消息列表；这一步本身不访问模型服务。
message = chat_prompt.format_messages(name="亮仔", question="什么是LangChain")

# 打印格式化后的消息内容
print(message)