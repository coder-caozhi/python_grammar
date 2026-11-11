# ============================================================================
# 学习目的：用角色消息列表向聊天模型传递上下文
# 技术讲解：system 指定规则，user 提出问题；聊天接口返回 AIMessage
# 阅读路线：消息字典列表 → chatLLM.invoke → response.content
# 当前代码要注意：角色提示是模型输入，不是代码层面的访问控制
# 动手验证：给 messages 增加一条历史 assistant 消息，说明顺序的作用
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
chatLLM = ChatOpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    model="deepseek-chat",
    # other params...
)

messages = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "你是谁？"}]

# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
response = chatLLM.invoke(messages)

print(response.content)