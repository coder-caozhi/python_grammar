# ============================================================================
# 学习目的：手工维护用户与 AI 消息的完整历史
# 技术讲解：history.messages 是再次请求时发送的上下文，不是模型权重发生变化
# 阅读路线：添加用户消息 → invoke 历史 → 保存 AI 回复 → 下一轮
# 当前代码要注意：内存记录随进程结束丢失；每轮发送全部历史会增加上下文长度和 token 使用
# 动手验证：数一数两轮结束后 history.messages 应有几条
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory
from loguru import logger
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
# 设置本地模型，不使用深度思考
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


# 创建内存聊天历史记录实例，用于存储对话消息
# 【理解这一行】创建进程内消息容器；只保存消息，不会自行调用模型，重启后不保留。
history = InMemoryChatMessageHistory()

# 添加用户消息到聊天历史记录
# 【理解这一行】把当前用户输入加入历史；下一次模型调用需发送该历史才会看到它。
history.add_user_message("我叫张三，我的爱好是学习")

# 调用语言模型处理聊天历史中的消息
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
ai_message = llm.invoke(history.messages)

# 记录并输出AI回复的内容
logger.info(f"第一次回答\n{ai_message.content}")

# 将AI回复添加到聊天历史记录中
# 【理解这一行】把模型实际回复写回历史，保持 user/ai 的多轮顺序。
history.add_message(ai_message)

# 添加新的用户消息到聊天历史记录
history.add_user_message("我叫什么？我的爱好是什么？")

# 再次调用语言模型处理更新后的聊天历史
ai_message2 = llm.invoke(history.messages)

# 记录并输出第二次AI回复的内容
logger.info(f"第二次回答\n{ai_message2.content}")

# 将第二次AI回复添加到聊天历史记录中
history.add_message(ai_message2)

# 遍历并输出所有聊天历史记录中的消息内容
for message in history.messages:
    logger.info(message.content)