# Python 综合练习：个人记账本

这个项目用标准库实现，可以新增、查看、统计和删除支出，并将数据保存到 SQLite。目标是围绕一个真实的小业务，从头跟敲并理解常用 Python 写法；它是生产风格的教学示例，不是覆盖所有生产需求的财务系统。

## 准备和运行

需要 Python 3.10 或更高版本，无需安装第三方包。在 PowerShell 中进入本目录：

```powershell
cd D:\python\python_grammar\01_python_basics\06_practice
..\..\.venv\Scripts\python.exe --version
..\..\.venv\Scripts\python.exe expense_tracker.py --help
..\..\.venv\Scripts\python.exe expense_tracker.py add --help
```

以上命令使用仓库中的虚拟环境。如果你已配置其他 Python 3.10+，也可以将 `..\..\.venv\Scripts\python.exe` 换成 `python` 或 `py -3`。默认数据库是本目录下 `data/expenses.db`，程序首次运行时自动创建；数据会保留，删除操作会实际删除记录。

```powershell
..\..\.venv\Scripts\python.exe expense_tracker.py add 35.50 餐饮 --date 2026-11-01 --note 午餐
..\..\.venv\Scripts\python.exe expense_tracker.py add 12.00 交通 --date 2026-11-02 --note 地铁
..\..\.venv\Scripts\python.exe expense_tracker.py list
..\..\.venv\Scripts\python.exe expense_tracker.py list --month 2026-11
..\..\.venv\Scripts\python.exe expense_tracker.py summary --month 2026-11
..\..\.venv\Scripts\python.exe expense_tracker.py --verbose delete 1
```

`--db` 和 `--verbose` 是全局参数，需要放在 `add`、`list` 等子命令之前。可指定单独的数据库做练习，例如：

```powershell
..\..\.venv\Scripts\python.exe expense_tracker.py --db practice.db add 9.90 饮料
..\..\.venv\Scripts\python.exe expense_tracker.py --db practice.db list
```

## 建议的跟敲顺序

1. 从导入、常量、异常类开始，跟敲金额和日期校验函数。留意类型注解、`try/except`、`raise ... from` 和 f-string。
2. 跟敲 `Expense`，理解数据类、属性、类方法和实例对象。
3. 跟敲 `ExpenseRepository`，理解类、方法、列表推导式、参数化 SQL、事务和 `finally` 关闭连接。
4. 跟敲筛选和统计函数，理解生成器、循环、字典、排序、匿名函数、解包和内置函数。
5. 最后跟敲命令行解析和 `main`，理解分支、集合成员判断、返回值及程序入口。运行上面的命令，观察数据库中的数据是否持续存在。
6. 尝试错误输入：金额 `-1`、`1.234` 或日期 `2026-02-30`，观察报错；再试一个不存在的记录 ID。

可以设置断点跟踪 `main` → `repository.add` → SQLite，再跟踪 `list` 中记录从数据库行变成对象的过程。进阶练习：添加按分类筛选、编辑备注或导出 CSV；每完成一项，先用独立数据库验证正常和错误输入。

覆盖的是常用语法和标准库组合，不刻意堆砌全部语言特性；异步、多线程、网络服务等主题可以在后续独立练习。


## 更简单的基础练习：学生成绩管理

先跟敲 `student_basics.py`：它只用变量、类型转换、函数、类、列表、条件、循环和基础异常处理，不需要安装依赖。程序退出后数据不会保存。

```powershell
..\..\.venv\Scripts\python.exe student_basics.py
```

运行后可以添加几个学生、查看列表、计算平均分并按姓名查找。试着输入字母或超出 0～100 的成绩，观察程序如何提示并重新输入。建议完成后自行增加“删除学生”功能。
