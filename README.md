# Python 与 AI 应用开发学习仓库

统一存放 Python 基础 → FastAPI → LangChain → LangGraph 的学习代码。

| 目录 | 学习内容 |
| --- | --- |
| [00_docs](00_docs/README.md) | 命名规范、路径对照、迁移检查 |
| [01_python_basics](01_python_basics/README.md) | 语法、容器、函数、面向对象、文件、调试与综合练习 |
| [02_fastapi](02_fastapi/README.md) | 部门员工 CRUD；路由、参数与 ORM 课堂练习 |
| [03_langchain](03_langchain/README.md) | 模型、提示词、解析器、LCEL、记忆、工具、RAG、MCP、Agent |
| [04_langgraph](04_langgraph/README.md) | 后续学习预留，目前尚无学习代码 |
| [90_course_materials](90_course_materials/README.md) | 尚硅谷五月课程原始代码，对照课件使用 |

## 如何使用

PyCharm 打开 `D:\python\python_grammar`。基础和 FastAPI 继续使用根目录 `.venv\Scripts\python.exe`；LangChain 运行配置选择 `03_langchain\.venv\Scripts\python.exe`。两套环境独立，避免依赖互相影响。

运行普通练习时，将工作目录设为脚本所在目录；文件读写、JSON/YAML 提示词和 RAG 素材仍与示例放在一起。

```powershell
cd D:/python/python_grammar/01_python_basics/01_syntax
../../.venv/Scripts/python.exe ./01_变量.py
```

在 PyCharm 中也可以直接运行具体脚本。数据库、网络调用及故意报错的课程案例请先阅读代码。

FastAPI 启动示例：

```powershell
cd D:\python\python_grammar\02_fastapi\01_department_employee_crud
..\..\.venv\Scripts\python.exe -m uvicorn main:app --reload
```

LangChain 的 `.env`、`.env.example` 和原 `requirements.txt` 放在 `03_langchain`。原依赖清单仅覆盖部分入门示例，且代码同时包含 0.3 与 1.0 示例；不代表全部章节可在同一版本下直接运行。

新增学习代码先选择主题目录，再新增 `13_topic_name` 这样的章节；具体规则见 [命名规范](00_docs/naming_conventions.md)。
