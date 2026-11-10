from contextlib import asynccontextmanager
from typing import Annotated
from fastapi import Depends, FastAPI, HTTPException, Query, Response
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session, selectinload
import models
from database import Base, engine, get_db
from schemas import DepartmentCreate, DepartmentRead, EmployeeCreate, EmployeeRead, EmployeeUpdate

@asynccontextmanager
async def lifespan(app: FastAPI):
    # 教学项目启动时建表；已有表结构不会自动迁移。
    Base.metadata.create_all(bind=engine)
    yield

app = FastAPI(title="部门与员工管理", description="FastAPI 和 SQLAlchemy 课件综合练习", lifespan=lifespan)
Db = Annotated[Session, Depends(get_db)]

def find_department(db: Session, id: int):
    value = db.scalar(select(models.Department).options(selectinload(models.Department.employees)).where(models.Department.id == id))
    if value is None:
        raise HTTPException(404, "部门不存在")
    return value

def find_employee(db: Session, id: int):
    value = db.get(models.Employee, id)
    if value is None:
        raise HTTPException(404, "员工不存在")
    return value

def commit(db: Session):
    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(409, "数据冲突：请检查名称或关联数据") from exc

@app.get("/", tags=["基础"])
def home():
    return {"message": "欢迎学习 FastAPI 与 SQLAlchemy", "docs": "/docs"}

@app.post("/departments/", response_model=DepartmentRead, status_code=201, tags=["部门"])
def create_department(data: DepartmentCreate, db: Db):
    obj = models.Department(name=data.name)
    db.add(obj); commit(db); db.refresh(obj)
    return obj

@app.get("/departments/", response_model=list[DepartmentRead], tags=["部门"])
def list_departments(db: Db, skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100)):
    return db.scalars(select(models.Department).options(selectinload(models.Department.employees)).order_by(models.Department.id).offset(skip).limit(limit)).all()

@app.get("/departments/{department_id}", response_model=DepartmentRead, tags=["部门"])
def read_department(department_id: int, db: Db):
    return find_department(db, department_id)

@app.put("/departments/{department_id}", response_model=DepartmentRead, tags=["部门"])
def update_department(department_id: int, data: DepartmentCreate, db: Db):
    obj = find_department(db, department_id)
    obj.name = data.name
    commit(db); db.refresh(obj)
    return obj

@app.delete("/departments/{department_id}", status_code=204, tags=["部门"])
def delete_department(department_id: int, db: Db):
    db.delete(find_department(db, department_id)); commit(db)
    return Response(status_code=204)

@app.post("/employees/", response_model=EmployeeRead, status_code=201, tags=["员工"])
def create_employee(data: EmployeeCreate, db: Db):
    if data.department_id is not None:
        find_department(db, data.department_id)
    obj = models.Employee(**data.model_dump())
    db.add(obj); commit(db); db.refresh(obj)
    return obj

@app.get("/employees/", response_model=list[EmployeeRead], tags=["员工"])
def list_employees(db: Db, department_id: int | None = None, skip: int = Query(0, ge=0), limit: int = Query(20, ge=1, le=100)):
    statement = select(models.Employee)
    if department_id is not None:
        statement = statement.where(models.Employee.department_id == department_id)
    return db.scalars(statement.order_by(models.Employee.id).offset(skip).limit(limit)).all()

@app.get("/employees/{employee_id}", response_model=EmployeeRead, tags=["员工"])
def read_employee(employee_id: int, db: Db):
    return find_employee(db, employee_id)

@app.patch("/employees/{employee_id}", response_model=EmployeeRead, tags=["员工"])
def update_employee(employee_id: int, data: EmployeeUpdate, db: Db):
    obj = find_employee(db, employee_id)
    changes = data.model_dump(exclude_unset=True)
    if "name" in changes and changes["name"] is None:
        raise HTTPException(422, "姓名不能为 null")
    if changes.get("department_id") is not None:
        find_department(db, changes["department_id"])
    for key, value in changes.items():
        setattr(obj, key, value)
    commit(db); db.refresh(obj)
    return obj

@app.delete("/employees/{employee_id}", status_code=204, tags=["员工"])
def delete_employee(employee_id: int, db: Db):
    db.delete(find_employee(db, employee_id)); commit(db)
    return Response(status_code=204)
