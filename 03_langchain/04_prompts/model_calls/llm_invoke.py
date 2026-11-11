# ============================================================================
# 学习目的：学习一次同步聊天调用的输入输出
# 技术讲解：invoke 接受消息序列并等待完整 AIMessage；content_blocks 是结构化内容视图
# 阅读路线：system 规则 → human 问题 → invoke → 打印内容
# 当前代码要注意：system 提示不能保证模型绝不回答范围外问题；content 不总是单一纯文本类型
# 动手验证：比较 response、content 和 content_blocks
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

# List<Messages>


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
    SystemMessage(content="你是一个法律助手，只回答法律问题，超出范围的统一回答，非法律问题无可奉告"),
    HumanMessage(content="简单介绍下广告法，一句话告知50字以内")
    #HumanMessage(content="2+3等于几?")
]

# 3.调用模型
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
response = model.invoke(messages)  # ainvoke
print(f"响应类型：{type(response)}")
# 打印结果
print(response.content)
print(response.content_blocks)
