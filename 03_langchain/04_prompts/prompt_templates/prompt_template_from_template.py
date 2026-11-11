# ============================================================================
# 学习目的：从字符串自动推断模板变量
# 技术讲解：from_template 读取花括号变量，减少手写 input_variables
# 阅读路线：创建模板 → format 填充 role/question → 换一个主题模板
# 当前代码要注意：这是提示词字符串生成，不会调用模型或自动执行生成的代码
# 动手验证：查看 template.input_variables，再故意遗漏一个变量观察错误
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 方式2：使用 from_template 方法实例化提示词模板
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 模板包含两个占位符：{role}表示角色，{question}表示问题
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template = PromptTemplate.from_template("你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}")

# 使用指定的角色和问题参数来格式化模板，生成最终的提示词字符串
# role: 工程师角色描述
# question: 具体的技术问题
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt = template.format(role="python开发",question="快速排序怎么写？")

# 输出生成的提示词
print(prompt)

print("\n\n")


# 使用 from_template 方法实例化提示词模板
template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。")
# 使用模板生成提示
prompt = template.format(topic="量子力学",type="详细")
print(prompt)  # 请给我一个关于量子力学的详细解释。

