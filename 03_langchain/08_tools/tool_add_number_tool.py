# ============================================================================
# 学习目的：把普通加法函数封装成可描述的工具
# 技术讲解：@tool 根据函数名、docstring、类型注解生成工具名称、描述和参数 schema
# 阅读路线：装饰函数 → invoke 字典 → 查看工具元信息
# 当前代码要注意：工具自身可直接执行，不需要先调用大模型；模型绑定是另一步
# 动手验证：比较普通函数调用方式和工具 invoke 的参数形式
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


from langchain.tools import tool

@tool
def add_number(a: int, b: int) -> int:
    """两个整数相加"""
    return a + b

# 【理解这一行】直接执行工具：传入符合 schema 的参数，返回 Python 函数的计算/查询结果。
result = add_number.invoke({"a": 1, "b": 12})
print(result)

print()

print(f"{add_number.name=}\n{add_number.description=}\n{add_number.args=}")
# add_number.name='add_number'
# add_number.description='两个整数相加'
# add_number.args={'a': {'title': 'A', 'type': 'integer'}, 'b': {'title': 'B', 'type': 'integer'}}


