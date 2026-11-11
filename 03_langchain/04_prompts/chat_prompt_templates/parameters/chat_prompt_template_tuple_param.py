# ============================================================================
# 学习目的：使用角色元组组织多轮消息模板
# 技术讲解：human/ai/system 角色与占位变量组合，保留多轮对话结构
# 阅读路线：构造角色元组 → 传入 name/thing/user_input → 查看消息列表
# 当前代码要注意：历史 AI 消息是你写入的示例上下文，不是本次模型实际生成的结果
# 动手验证：增加一轮 human/ai 元组，再检查消息列表长度
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain_core.prompts import ChatPromptTemplate


# 【理解这一行】构造角色消息模板；消息的顺序与角色会一起传给聊天模型。
chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

# 【理解这一行】把变量值填入消息模板，得到消息列表；这一步本身不访问模型服务。
prompt = chatPromptTemplate.format_messages(name="小谷AI", thing="AI", user_input="7 + 5等于多少")
print(prompt)