# ============================================================================
# 学习目的：分两次完成变量绑定
# 技术讲解：partial 返回一个仍可继续格式化的新模板
# 阅读路线：预填 role → 得到 partial → 填 question → 文本
# 当前代码要注意：预填变量并不意味着已经得到最终字符串
# 动手验证：打印 partial.input_variables，确认只剩哪些待填项
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
partial()方法可以格式化部分变量，并且继续返回一个模板，通常在部分提示词模板场景下使用
"""
from langchain_core.prompts import PromptTemplate

# 创建模板对象，定义提示词模板格式
# 模板包含两个占位符：role（角色）和 question（问题）
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

# 使用partial方法固定role参数为"python开发"
# 返回一个新的模板对象，其中role参数已被绑定
# 【理解这一行】预先绑定部分变量，返回仍可继续填充其他变量的模板。
partial = template.partial(role="python开发")

# 打印partial对象及其类型信息
print(partial)
print(type(partial))
print()

# 使用format方法填充question参数，生成最终的提示词字符串
# 此时所有占位符都已填充完毕，返回完整的提示词文本
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt = partial.format(question="冒泡排序怎么写？")

# 输出生成的提示词
print(prompt)
print(type(prompt))