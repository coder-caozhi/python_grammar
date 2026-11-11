# ============================================================================
# 学习目的：一次提交多个独立问题
# 技术讲解：batch 返回与输入顺序对应的结果列表；不表示把问题合并成一个聊天上下文
# 阅读路线：questions 列表 → batch → zip 配对问题与回答
# 当前代码要注意：同步 batch 通常可并发执行请求，不能等同于一个 for 中的逐次 invoke
# 动手验证：修改 questions 数量，检查响应列表长度
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 1.导入依赖
import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage,SystemMessage
#通过 python-dotenv 库读取 env 文件中的环境变量，并加载到当前运行的环境中
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()

# 2.实例化模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 问题列表
questions = [
    "什么是redis?简洁回答，字数控制在100以内",
    "Python的生成器是做什么的？简洁回答，字数控制在100以内",
    "解释一下Docker和Kubernetes的关系?简洁回答，字数控制在100以内"
]

# 批量调用大模型 model.batch()
# 【理解这一行】批量处理多个独立输入，得到按输入顺序排列的结果列表。
response = model.batch(questions)
print(f"响应类型：{type(response)}")
print()
for q, r in zip(questions, response):
    print(f"问题：{q}\n回答：{r.content}\n")