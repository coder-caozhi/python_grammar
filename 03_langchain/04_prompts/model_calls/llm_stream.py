# ============================================================================
# 学习目的：用同步迭代器逐块展示回答
# 技术讲解：stream 返回可迭代分片，不等价于已经拼接完成的回答
# 阅读路线：创建 messages → 获取流 → for chunk → 输出正文
# 当前代码要注意：flush=True 刷新控制台缓冲；分片边界不一定与汉字、词或句子边界一致
# 动手验证：将分片累计到列表，结束后拼接并与屏幕输出比较
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

# 构建消息列表
messages = [
    SystemMessage(content="你叫小问，是一个乐于助人的AI人工助手"),
    HumanMessage(content="你是谁")
]

# 3.流式调用大模型
# 【理解这一行】返回分片迭代对象，需继续遍历才能读出输出；每块不是整段回答。
response = model.stream(messages)
print(f"响应类型：{type(response)}")
# 流式打印结果
for chunk in response:
    # 刷新缓冲区 (无换行符，缓冲区未刷新，内容可能不会立即显示)
    print(chunk.content, end="",flush=True)
print("\n")

