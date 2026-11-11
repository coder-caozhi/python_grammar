# ============================================================================
# 学习目的：组合提示词片段形成一个完整模板
# 技术讲解：模板加法合并文本和变量需求，不是多步模型链
# 阅读路线：模板加字符串 → 两个模板相加 → format
# 当前代码要注意：两个示例都是生成一个最终提示词，不是调用模型两次
# 动手验证：对比合并前后 input_variables
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
组合提示词模板

通过将多个子提示（Prompt）按一定逻辑顺序或层级组合起来，形成一个复杂任务的整体 Prompt。
例如实现多消息对话、多阶段任务、多输入源组合等场景。
尤其在，AI产品，你一言我一语，构建最后提示词，有用
"""
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate模板，用于生成介绍某个主题的提示词
# 该模板包含两个占位符：topic（主题）和length（字数限制）
# template1 = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂,内容不超过{length}个字")
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template1 = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂\n") + "内容不超过{length}个字"
# 使用format方法填充模板中的占位符，生成具体的提示词
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt1 = template1.format(topic="LangChain", length=100)
print(prompt1)

# 分别创建两个独立的PromptTemplate模板
prompt_a = PromptTemplate.from_template("请用一句话介绍{topic}，要求通俗易懂\n")
prompt_b = PromptTemplate.from_template("内容不超过{length}个字")
# 将两个模板进行拼接组合
prompt_all = prompt_a + prompt_b
# 填充组合后模板的占位符，生成最终的提示词
prompt2 = prompt_all.format(topic="LangChain", length=200)
print(prompt2)