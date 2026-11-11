# ============================================================================
# 学习目的：把模板立即转换成字符串
# 技术讲解：format 接收关键字参数并返回 str
# 阅读路线：from_template → format(role=..., question=...) → 查看 type
# 当前代码要注意：format 只是填空，不执行模型调用
# 动手验证：与 invoke_method 案例比较返回类型
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板包含两个占位符：{role}表示角色，{question}表示问题
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template = PromptTemplate.from_template(
    "你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

# 使用指定的角色和问题参数来格式化模板，生成最终的提示词字符串
# role: 工程师角色描述
# question: 具体的技术问题
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt = template.format(role="python开发",question="二分查找算法怎么写？")

# 输出生成的提示词
print(prompt)
print(type(prompt))