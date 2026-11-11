# ============================================================================
# 学习目的：把会话历史放入 Redis 并串联交互问答
# 技术讲解：RedisChatMessageHistory 按 session_id 存储；RunnableWithMessageHistory 自动读写
# 阅读路线：输入问题 → 按 ID 取历史 → 模型 → 保存历史 → 下一轮
# 当前代码要注意：端口是 26379；redis_client.save() 是服务器级同步持久化，不是仅保存当前会话，可能阻塞服务
# 动手验证：解释停掉 Python 再启动后历史为什么可能仍存在
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain.chat_models import init_chat_model
from langchain_community.chat_message_histories import RedisChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnableConfig
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
import redis  #导入原生redis库，pip install redis==5.3.1
from loguru import logger

REDIS_URL = "redis://localhost:26379"
# 创建原生Redis客户端,decode_responses 控制 Redis 返回数据的类型：False 返字节串，True 返字符串
redis_client = redis.Redis.from_url(REDIS_URL, decode_responses=True)

# 设置本地模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 创建提示模板
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
prompt = ChatPromptTemplate.from_messages([
    MessagesPlaceholder("history"),
    ("human", "{question}")
])

def get_session_history(session_id: str) -> RedisChatMessageHistory:
    """获取或创建会话历史（使用 Redis）"""
    # 创建 Redis 历史对象
    # 【理解这一行】历史读写转到 Redis，session_id 决定会话归属；需先有可用服务。
    history = RedisChatMessageHistory(
        session_id=session_id,
        url=REDIS_URL,
        # ttl=3600  # 注释：关闭自动过期，避免重启后数据被清理
    )

    return history

# 创建带历史的链
# 【理解这一行】在原链外包一层历史读写；输入键、历史键必须与提示词一致。
chain = RunnableWithMessageHistory(
    prompt | llm,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# 配置
# session_id 就是登录大模型的各自帐户，类似登录手机号码，各不相同
config = RunnableConfig(configurable={"session_id": "user-001"})

# 主循环
print("开始对话（输入 'quit' 退出）")
while True:
    question = input("\n输入问题：")
    if question.lower() in ['quit', 'exit', 'q']:
        break

    # 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
    response = chain.invoke({"question": question}, config)
    logger.info(f"AI回答:{response.content}")

    # 等同于redis-cli的SAVE命令，强制写入dump.rdb
    # 【理解这一行】SAVE 会同步保存 Redis 实例数据；不是只写当前聊天记录，生产用法应另行设计持久化策略。
    redis_client.save()