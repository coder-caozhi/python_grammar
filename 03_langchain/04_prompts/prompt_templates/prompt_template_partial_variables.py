# ============================================================================
# 学习目的：提前绑定部分变量并理解绑定时机
# 技术讲解：partial_variables 和 partial 都可预填值；这里传入的是已计算的时间字符串
# 阅读路线：绑定时间 → 填问题 → 等待 → 另一次绑定 → 覆盖 foo
# 当前代码要注意：datetime.now() 在调用当时就执行，不是每次 format 自动刷新；若需动态值应研究 callable 形式
# 动手验证：对同一个 partial 模板连续 format，判断时间会不会变化
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 方式3：部分提示词模板(partial_variables),实例化过程中指定 partial_variables 参数
from langchain_core.prompts import PromptTemplate
from datetime import datetime
import time

# 1 实例化过程中指定 partial_variables 参数
# 创建一个包含时间变量的模板，时间变量使用partial_variables预设为当前时间,然后格式化问题生成最终提示词
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
template1 = PromptTemplate.from_template(
    "现在时间是：{time},请对我的问题给出答案，我的问题是：{question}",
    partial_variables={"time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
)

# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt1 = template1.format(question="今天是几号？")
print(prompt1)

time.sleep(2)  # 程序暂停 2 秒，期间不执行任何代码

# 2 使用 partial 方法指定默认值
template2 = PromptTemplate.from_template("现在时间是：{time},请对我的问题给出答案，我的问题是：{question}")
# 使用 partial 方法指定默认值
# 【理解这一行】预先绑定部分变量，返回仍可继续填充其他变量的模板。
partial = template2.partial(time=datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
prompt2 = partial.format(question="今天是几号？")
print(prompt2)


# 【理解这一行】构造字符串模板；先区分模板对象与 format/invoke 之后得到的提示词。
template3 = PromptTemplate(
    template="{foo} {bar}",
    input_variables=["foo", "bar"],
    partial_variables={"foo": "hello"},  # 预先定义部分变量foo值为hello
)

prompt = template3.format(foo="li4",bar="world")
print(prompt)  # li4 world

prompt = template3.format(bar="world")
print(prompt)  # hello world