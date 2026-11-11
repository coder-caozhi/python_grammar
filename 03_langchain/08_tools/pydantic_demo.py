# ============================================================================
# 学习目的：理解严格类型、默认值和校验异常
# 技术讲解：StrictInt 不接收需要转换的值；age 有默认值 0
# 阅读路线：合法 User → 查看 id 类型 → 非法 User → 捕获错误
# 当前代码要注意：id='42' 与 id=42 在严格模式中不同；原错误文本可能来自旧 Pydantic 版本
# 动手验证：分别传入字符串 '42' 和整数 42 比较
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from pydantic import BaseModel, ValidationError, StrictInt


# 【理解这一行】StrictInt 不接收需要转换的值；age 有默认值 0
class User(BaseModel):
    #id: int
    id: StrictInt  # 改用严格整数类型，拒绝类型转换
    name: str
    age: int = 0  # 可给默认值

try:
    # 自动把字符串转成 int
    #u = User(id="41", name="z3") #  自动把字符串转成 int，可以通融。id: int
    u = User(id=42, name="z3")# 传错类型就报错 id: StrictInt
except ValidationError as e:
    print(e)
print(u.id, type(u.id))  # 42 <class 'int'>

print()
print()


try:
    User(id="abc", name="Bob") # 传错类型就报错 id: StrictInt
except ValidationError as e:
    print(e)
"""
1 validation error for User
id
  value is not a valid integer (type=type_error.integer)
"""

