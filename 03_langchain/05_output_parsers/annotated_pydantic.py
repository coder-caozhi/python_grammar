# ============================================================================
# 学习目的：区分类型元数据与运行时约束
# 技术讲解：Pydantic 读取 Annotated 中的 Field(ge/le)，构造对象时执行校验
# 阅读路线：定义 Age → Person 引用 Age → 传入 188 → 捕获 ValidationError
# 当前代码要注意：age 是普通 int 字段，age2 才附加了 0–150 范围限制
# 动手验证：将 age2 设为 150 和 151，观察边界
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from typing import Annotated
from pydantic import BaseModel, Field, ValidationError

# 用Annotated结合Field设置范围约束，兼具注释和运行时校验能力
Age = Annotated[int, Field(ge=0, le=150, description="年龄，范围0-150")]

class Person(BaseModel):
    name: str
    age: int
    age2: Age

try:
    # 【理解这一行】age2=188 超出 Field 的 le=150，会在构造时触发 ValidationError；age 没有这个范围约束。
    p = Person(name="z3", age=11, age2=188)
    print(p)
except ValidationError as e:
    print("数据校验失败：")
    print(e)