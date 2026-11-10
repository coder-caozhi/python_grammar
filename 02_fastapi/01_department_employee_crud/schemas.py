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
    model_config = ConfigDict(from_attributes=True)
    id: int
class DepartmentRead(DepartmentCreate):
    model_config = ConfigDict(from_attributes=True)
    id: int
    employees: list[EmployeeRead] = Field(default_factory=list)
