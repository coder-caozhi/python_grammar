# ============================================================================
# 学习目的：把多角色模板填充为可交给模型的消息列表
# 技术讲解：元组中的角色和内容分别决定消息类型及模板变量
# 阅读路线：定义四条消息 → format_messages 替换变量 → 模型回答
# 当前代码要注意：format_messages 本身不调用模型；后面的 llm.invoke 才请求远端
# 动手验证：打印每条消息的 type 和 content，检查角色顺序
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
使用ChatPromptTemplate构造方法直接实例化
实例化时需要传入messages: Sequence[MessageLikeRepresentation]
messages 参数支持如下格式：
	tuple 构成的列表，格式为[(role, content)]
	dict 构成的列表，格式为[{“role”:... , “content”:...}]
	Message 类构成的列表
"""

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model
from langchain_core.prompts import ChatPromptTemplate


def get_deepseek_api_key() -> str:
    """读取 DeepSeek API Key。"""
    candidates = [os.getenv("DEEPSEEK_API_KEY")]
    for value in candidates:
        if value:
            return value
    raise RuntimeError(
        "未配置 DeepSeek API Key。请在项目根目录的 .env 文件中设置 "
        "DEEPSEEK_API_KEY。"
    )


# 【理解这一行】构造角色消息模板；消息的顺序与角色会一起传给聊天模型。
chatPromptTemplate = ChatPromptTemplate(
    [
        ("system", "你是一个AI开发工程师，你的名字是{name}。"),
        ("human", "你能帮我做什么?"),
        ("ai", "我能开发很多{thing}。"),
        ("human", "{user_input}"),
    ]
)

# 【理解这一行】把变量值填入消息模板，得到消息列表；这一步本身不访问模型服务。
prompt = chatPromptTemplate.format_messages(
    name="小谷AI", thing="AI", user_input="7 + 5等于多少"
)

print(prompt)

api_key = get_deepseek_api_key()
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=api_key,
    base_url="https://api.deepseek.com",
)
print()
print("======================")

# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
result = llm.invoke(prompt)
print(result)
print(result.content)