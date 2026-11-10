from uuid import uuid4
from fastapi.testclient import TestClient
from database import SessionLocal, engine
from main import app
from models import Department, Employee


def test_department_employee_workflow():
    # 使用唯一名称，并只清理本次创建的记录。
    name = "测试部门_" + uuid4().hex
    department_id = employee_id = None
    try:
        with TestClient(app) as client:
            response = client.post("/departments/", json={"name": name})
            assert response.status_code == 201
            department_id = response.json()["id"]
            assert client.post("/departments/", json={"name": name}).status_code == 409
            response = client.post("/employees/", json={"name": "张三", "age": 25, "department_id": department_id})
            assert response.status_code == 201
            employee_id = response.json()["id"]
            assert client.get(f"/departments/{department_id}").json()["employees"][0]["id"] == employee_id
            assert len(client.get("/employees/", params={"department_id": department_id}).json()) == 1
            assert client.patch(f"/employees/{employee_id}", json={"age": 26}).json()["age"] == 26
            assert client.post("/employees/", json={"name": "李四", "age": -1}).status_code == 422
            assert client.delete(f"/departments/{department_id}").status_code == 204
            assert client.get(f"/departments/{department_id}").status_code == 404
            assert client.get(f"/employees/{employee_id}").json()["department_id"] is None
            assert client.delete(f"/employees/{employee_id}").status_code == 204
    finally:
        with SessionLocal() as db:
            if employee_id is not None:
                employee = db.get(Employee, employee_id)
                if employee is not None:
                    db.delete(employee)
            if department_id is not None:
                department = db.get(Department, department_id)
                if department is not None:
                    db.delete(department)
            db.commit()
        engine.dispose()
