# ============================================================================
# 学习目的：把已有聊天历史插入指定位置
# 技术讲解：MessagesPlaceholder 接收消息序列；普通变量接收内容值
# 阅读路线：system → memory 消息序列 → 当前 question
# 当前代码要注意：默认的显式占位符要求提供 memory；它本身不会保存历史，需要调用方提供
# 动手验证：传入空列表和两条消息，比较最终消息数量
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
如果我们不确定消息何时生成，也不确定要插入几条消息，比如在提示词中添加聊天历史记忆这种场景，
可以在ChatPromptTemplate添加MessagesPlaceholder占位符，在调用invoke时，在占位符处插入消息。

显式使用MessagesPlaceholder
"""

from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# 构建一个 ChatPromptTemplate，包含多种消息类型：
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
prompt = ChatPromptTemplate.from_messages([
    # 添加一条系统消息，设定 AI 的角色或行为准则
    ("system", "你是一个资深的Python应用开发工程师，请认真回答我提出的Python相关的问题"),
    # 插入 memory 占位符，用于填充历史对话记录（如多轮对话上下文）
    MessagesPlaceholder("memory"),
    # 添加一条用户问题消息，用变量 {question} 表示
    ("human", "{question}")
])

# 调用 prompt.invoke 来格式化整个 Prompt 模板
# 传入的参数中：
# - memory：是一组历史消息，表示之前的对话内容（多轮上下文）
# - question：是当前用户的问题
# 【理解这一行】模板 invoke 接收变量字典并产生 PromptValue；同名方法不代表在调用模型。
prompt_value = prompt.invoke({
    "memory": [
        # 用户第一轮说的话
        HumanMessage("我的名字叫亮仔，是一名程序员111"),
        # AI 第一轮的回应
        AIMessage("好的，亮仔你好222")
    ],
    # 当前问题：结合上下文，测试模型是否记住了用户名字
    "question": "请问我的名字叫什么？"
})

# 打印生成的完整 prompt 文本，格式化后的聊天记录
print(prompt_value.to_string())
