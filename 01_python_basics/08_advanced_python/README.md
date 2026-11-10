# Python 高阶用法：从迭代到异步

学习目标：理解数据怎样逐项产生、参数怎样打包传递、多个等待任务怎样并发运行。使用 Python 3.10+ 标准库，无需安装第三方依赖，不访问网络或数据库，不修改磁盘数据。

## 学习顺序

| 顺序 | 文件 | 重点与案例 |
| --- | --- | --- |
| 1 | [iterator_basics.py](iterator_basics.py) | iter / next、自定义倒计时、可重复遍历与一次性消费 |
| 2 | [generator_pipeline.py](generator_pipeline.py) | yield 的暂停恢复、生成器表达式、yield from、订单过滤汇总 |
| 3 | [packing_unpacking.py](packing_unpacking.py) | 星号赋值、*args / **kwargs、参数种类、配置合并与重复键错误 |
| 4 | [async_basics.py](async_basics.py) | 协程、await、create_task、gather、顺序与并发等待 |
| 5 | [async_task_control.py](async_task_control.py) | 并发数量限制、超时取消、finally 清理、部分失败 |
| 6 | [async_generator.py](async_generator.py) | async for、模拟流式回答、提前停止与资源关闭 |

## 运行

在 PyCharm 中选择根项目 `.venv/Scripts/python.exe`，直接运行某个文件。每个案例都有 main 入口，导入文件不会自动执行案例。

PowerShell：

```powershell
cd D:\python\python_grammar\01_python_basics\08_advanced_python
..\..\.venv\Scripts\python.exe iterator_basics.py
..\..\.venv\Scripts\python.exe generator_pipeline.py
..\..\.venv\Scripts\python.exe packing_unpacking.py
..\..\.venv\Scripts\python.exe async_basics.py
..\..\.venv\Scripts\python.exe async_task_control.py
..\..\.venv\Scripts\python.exe async_generator.py
```

正常结束会打印“案例检查通过”。代码中的 assert 是学习用自检，请不要使用 `python -O` 运行。预期错误会被捕获并解释；异步耗时因机器负载不同而变化。

## 学习方法

先预测输出，再运行；在 next、yield、await 前后打断点，观察局部变量和执行顺序。每个文件末尾有一道改写练习，先自己完成，再检查输出或添加 assert。

| 容易混淆的概念 | 区别 |
| --- | --- |
| 可迭代对象 / 迭代器 | 前者能提供迭代器；后者记录遍历位置并提供 next。迭代器也是可迭代对象。 |
| 生成器 / 列表 | 生成器按需产生值，通常一次性消费；列表保存元素，可以重复遍历。 |
| 定义中的 * / 调用中的 * | 定义时收集参数；调用时展开已有数据。 |
| 协程对象 / 任务 | 调用 async def 创建协程对象；create_task 将协程交给事件循环调度。 |
| await / 并发 | 连续 await 两个调用通常是顺序等待；要并发需先调度多个任务。 |
| 并发 / CPU 并行 | 这里演示同一事件循环中等待的重叠，不是多核计算加速。 |

与后续学习的联系：FastAPI 的 async 路由涉及 await；批量模型调用涉及并发限制与超时；流式模型回答涉及异步迭代。这里先掌握标准库行为，再阅读框架封装。
