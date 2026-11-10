from pydantic import BaseModel, ConfigDict, Field

class DepartmentCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)

class EmployeeCreate(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int | None = Field(default=None, ge=0, le=150)
    department_id: int | None = None

class EmployeeUpdate(BaseModel):
    name: str | None = Field(default=None, min_length=1, max_length=50)
    age: int | None = Field(default=None, ge=0, le=150)
    department_id: int | None = None

class EmployeeRead(EmployeeCreate):
    model_config = ConfigDict(from_attributes=True) # 1.当同时存在对象属性和 `__dict__` 字典时，优先读取对象属性。2.不是自动递归！
    id: int

class DepartmentRead(DepartmentCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    # Field(default_factory=list)这个字段的默认值不是一个共享的固定列表
    # 而是“每次创建这个模型对象时，自动调用 list() 生成一个新的空列表”
    employees: list[EmployeeRead] = Field(default_factory=list)
