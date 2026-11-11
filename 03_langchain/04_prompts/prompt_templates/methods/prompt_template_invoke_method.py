# ============================================================================
# 学习目的：把模板作为 Runnable 使用
# 技术讲解：invoke 接收变量字典并返回 PromptValue，可转文本或消息
# 阅读路线：模板 → invoke → to_string → to_messages
# 当前代码要注意：同名 invoke 作用取决于对象：这里是模板，不是模型网络请求
# 动手验证：解释 PromptValue 为什么便于后续连接聊天模型
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
invoke() 是 LangChain Expression Language（LCEL 的统一执行入口，用于执行任意可运行对象（Runnable ）。返回的是一个 PromptValue 对象，
可以用 .to_string() 或 .to_messages() 查看内容
"""
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板中包含两个占位符：{role}表示角色，{question}表示问题
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

# 使用invoke方法填充模板中的占位符，生成具体的提示词
# 参数：字典类型，包含role和question两个键值对
# 返回值：PromptValue对象，包含了格式化后的提示词
# 【理解这一行】模板 invoke 接收变量字典并产生 PromptValue；同名方法不代表在调用模型。
prompt = template.invoke({"role": "python开发", "question": "冒泡排序怎么写？"})

# 打印PromptValue对象及其类型
print(prompt)
print(type(prompt))
print()

# 将PromptValue对象转换为字符串并打印
# to_string()方法将PromptValue转换为可读的字符串格式
print(prompt.to_string())
print(type(prompt.to_string()))
print()

print(prompt.to_messages())
print(type(prompt.to_messages()))
