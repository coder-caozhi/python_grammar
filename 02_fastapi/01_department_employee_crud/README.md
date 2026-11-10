# FastAPI + SQLAlchemy 学习项目

根据课件第 3、4、5 章的部门和员工案例编写，涵盖路径和查询参数、请求体校验、依赖注入、ORM 会话、增删改查和一对多关系。默认连接本机 MySQL，数据库名为 `fastapi_db`。需要 Python 3.10 或以上。

## 启动（PowerShell）

```powershell
cd D:\python\python_grammar\02_fastapi\01_department_employee_crud
..\..\.venv\Scripts\python.exe -m pip install -r requirements.txt
..\..\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

启动前请确保 MySQL 服务已启动，且 `fastapi_db` 数据库已创建。打开 http://127.0.0.1:8000/docs 即可操作接口。应用首次启动时会创建缺失的表。

## 练习

1. 在 `/docs` 执行 `POST /departments/`，请求体 `{"name":"研发部"}`，记录返回的部门 id。
2. 执行 `POST /employees/`，例如 `{"name":"张三","age":25,"department_id":1}`，将 1 换成实际 id。
3. 用 `GET /departments/{department_id}` 查看部门和员工，用 `GET /employees/?department_id=1` 按部门筛选。
4. 用 `PATCH /employees/{employee_id}` 传 `{"age":26}` 修改年龄，传 `{"department_id":null}` 解除部门关联。
5. 删除部门后员工保留，部门 id 变为 null。重复部门名返回 409，不存在的记录返回 404，不合法参数返回 422。

## MySQL 配置（对应课件）

项目目录的 `.env` 已设置本机 MySQL 连接。可以参考 `.env.example` 修改主机、端口、用户名、密码和数据库名；`.env` 包含密码，不应提交到版本库。系统环境变量 `DATABASE_URL` 优先于 `.env`。

先在 MySQL 中执行 `CREATE DATABASE IF NOT EXISTS fastapi_db CHARACTER SET utf8mb4;`。启动应用会创建缺失的表，不会创建数据库，也不会迁移已有表结构。密码中的 `@`、`:` 等特殊字符需 URL 编码。设置 `$env:SQL_ECHO='true'` 可查看 SQL。

## 阅读顺序

`database.py`：引擎、Session、依赖注入和异常回滚；`models.py`：表、外键及一对多关系；`schemas.py`：输入校验和输出字段；`main.py`：接口与数据库操作。同步 Session 配合同步 `def` 路由使用。测试命令：`..\..\.venv\Scripts\python.exe -m pytest -q`，测试连接当前配置的 MySQL，创建带随机标识的测试记录，并在结束后删除这些记录。
