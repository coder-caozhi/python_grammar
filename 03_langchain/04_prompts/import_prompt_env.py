# ============================================================================
# 学习目的：认识提示词类和四类消息对象
# 技术讲解：模板负责生成消息；System/Human/AI/ToolMessage 是具体消息
# 阅读路线：查看导入类 → 创建消息列表 → 检查 ToolMessage 的关联 ID
# 当前代码要注意：本例的工具消息只是手工构造，未真实调用工具；真实对话需与对应 tool_call_id 匹配
# 动手验证：说明为什么 ToolMessage 需要 tool_call_id
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain_core.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import FewShotPromptTemplate
from langchain_core.prompts import (
    ChatMessagePromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

from langchain.messages import SystemMessage, HumanMessage, AIMessage, ToolMessage


# 【理解这一行】模板负责生成消息；System/Human/AI/ToolMessage 是具体消息
messages = [
    SystemMessage(content="你是一位乐于助人的智能小助手"),
    HumanMessage(content="你好，请你介绍一下你自己"),
    AIMessage(content="我是一名人工智能助手，请问您有什么想问的嘛?"),
    # ToolMessage - 用于工具调用场景
    ToolMessage(
        tool_call_id="call_abc123",  # 关联的工具调用ID
        content='{"population": 21540000, "area": "16410平方公里"}',  # 工具执行结果
    )
]

print(messages)