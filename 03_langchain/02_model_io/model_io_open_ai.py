# ============================================================================
# 学习目的：认识 OpenAI 原生 SDK 的聊天响应结构
# 技术讲解：原生 SDK 的 choices[0].message.content 与 LangChain 的 AIMessage.content 不同
# 阅读路线：建立 OpenAI 客户端 → chat.completions.create → 从 choices 取正文
# 当前代码要注意：本例使用 OpenAI 兼容的 DeepSeek 服务，未使用 LangChain 的模型包装
# 动手验证：与 model_io_chat_open_ai.py 对比输入和返回结构
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# Please install OpenAI SDK first: `pip install openai`
import os
from dotenv import load_dotenv
from openai import OpenAI

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()

# 【理解这一行】创建原生 OpenAI SDK 客户端；接下来要从 SDK 的响应结构取值，而非 LangChain AIMessage。
# api_key 与 base_url 必须成对考虑：这里是"用 OpenAI 官方 SDK 去连 DeepSeek 的兼容接口"，
# 所以 base_url 必须改，否则请求会打到 api.openai.com 而认证失败（401）。
# 若 api_key 为 None，SDK 会转去读 OPENAI_API_KEY，仍然读不到就抛 Missing credentials。
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)

# 【理解这一行】chat.completions.create 是原生 SDK 发起**一次**对话请求的入口，
# 它返回的是一个 ChatCompletion 响应对象，而不是文本本身。
response = client.chat.completions.create(
    # model 决定远端用哪个模型；deepseek-chat 是 DeepSeek 的非思考模式模型名。
    model="deepseek-chat",
    # messages 是一个"角色消息列表"，按顺序累积上下文，等价于 LangChain 的 message 列表：
    #   system —— 设定模型的行为规则（提示性质，不是代码级权限控制）
    #   user   —— 本次用户输入
    # 注意这里是普通的 dict，不是 LangChain 的 SystemMessage / HumanMessage 对象。
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello,你是谁"},
    ],
    # stream=False 表示等模型整段生成完再一次性返回；
    # 置为 True 则返回分片迭代对象，需要 for 循环逐块消费 chunk.choices[0].delta.content。
    stream=False
)

# 【理解这一行】取值链路的每一层含义：
#   response  → ChatCompletion 响应对象
#   .choices  → 列表，一次请求通常只返回 1 个候选；n 参数可要求多个
#   [0]       → 第 1 个候选
#   .message  → 该候选的完整消息对象（含 role / content）
#   .content  → 真正的文本内容，可能为 None（例如模型只返回工具调用时）
#
# 【对比 LangChain】同样的信息在 LangChain 里是一条 AIMessage：
#   response.content                       → 正文
#   response.response_metadata             → 模型名、token 用量、finish_reason 等
#   原生 SDK 对应的是 response.model / response.usage / response.choices[0].finish_reason
print(response.choices[0].message.content)

# 【动手练习】把上面的 print 换成下面几行，观察原生响应的完整结构：
# print(response.model)                          # 实际使用的模型名
# print(response.usage)                          # prompt / completion / total tokens
# print(response.choices[0].finish_reason)       # stop 表示正常结束
# print(response.choices[0].message.role)        # assistant
