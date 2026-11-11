# ============================================================================
# 学习目的：通过 session_id 隔离多个会话
# 技术讲解：store 将会话 ID 映射到不同的 InMemoryChatMessageHistory
# 阅读路线：获取/创建历史 → 注入 history → 调用 → 保存新消息
# 当前代码要注意：这是进程内隔离，不是持久化；重启会丢失 store
# 动手验证：用 user-002 提问同样问题，比较历史是否相互独立
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
可持续记忆（RunnableWithMessageHistory）
"""

from langchain.chat_models import init_chat_model
from langchain_core.chat_history import InMemoryChatMessageHistory  # 内存型消息记录
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
# 设置本地模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)


# 定义全局的“会话存储”，用来保存每个 session 的聊天历史
#    （真实项目中可改为 Redis、SQLite 等）
store = {}

def get_session_history(session_id: str):
    """
    根据 session_id 获取对应的历史消息对象。
    如果不存在则创建一个新的 InMemoryChatMessageHistory。
    """
    # 【理解这一行】每个 session_id 单独创建历史对象，不能把所有用户都映射到同一个列表。
    if session_id not in store:
        # 【理解这一行】创建进程内消息容器；只保存消息，不会自行调用模型，重启后不保留。
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# 定义 Prompt 模板
#     - system: 给模型设定角色
#     - MessagesPlaceholder: 历史消息将注入这里
#     - human: 当前用户输入
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
prompt = ChatPromptTemplate.from_messages([
    ("system", "你是一个友好的中文助理，会根据上下文回答问题。"),
    MessagesPlaceholder("history"),
    ("human", "{question}")
])


#构建基本链：Prompt → LLM → 输出解析
# 【理解这一行】把支持的文本/消息输出变成文本，方便下一步传递；消息元数据不会作为正文保留。
memory_chain = prompt | llm | StrOutputParser()

# -----------------------------------------------------
# 将链包装为支持记忆的版本
# 【理解这一行】在原链外包一层历史读写；输入键、历史键必须与提示词一致。
with_history = RunnableWithMessageHistory(
    memory_chain,              # 原始链
    get_session_history,       # 获取历史函数
    input_messages_key="question",  # 对应 prompt 输入的 key
    history_messages_key="history", # 对应 MessagesPlaceholder 的变量名
)

# -----------------------------------------------------
# 模拟一个会话，用 session_id 区分不同用户
cfg = {"configurable": {"session_id": "user-001"}}

# 第一次提问：告诉模型“我叫张三”
print("用户：我叫张三。")
# 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
print("AI：", with_history.invoke({"question": "我叫张三。"}, cfg))

# 第二次提问：让模型回忆前面的对话
print("\n 用户：我叫什么？")
print("AI：", with_history.invoke({"question": "我叫什么？"}, cfg))