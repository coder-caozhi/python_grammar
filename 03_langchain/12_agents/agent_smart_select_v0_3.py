# ============================================================================
# 学习目的：理解旧式 Agent 与执行器的职责分工
# 技术讲解：create_tool_calling_agent 组织模型与工具消息；AgentExecutor 驱动执行循环
# 阅读路线：工具定义 → scratchpad 模板 → agent → executor → input
# 当前代码要注意：本例 appid 是写死的值而非注释所说的环境读取；不要复制到公开资料；多次工具调用不保证实际并行
# 动手验证：追踪 agent_scratchpad 为什么需要回填工具执行结果
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import json
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
import httpx
from langchain_openai import ChatOpenAI
from langchain_classic.agents import create_tool_calling_agent
from langchain_classic.agents import AgentExecutor
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

'''
多工具并行调用,一次性发起了同一个外部函数的两次调用请求并将最后结果聚合
一次问题 → 多工具调用 → 聚合回答
'''


@tool
def get_weather(loc):
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称。
                注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，
                则 loc 参数需要输入 'Beijing'/'shanghai'。
    :return: OpenWeather API 查询即时天气的结果。具体 URL 请求地址为：
             https://api.openweathermap.org/data/2.5/weather。
             返回结果对象类型为解析之后的 JSON 格式对象，并用字符串形式进行表示，
             其中包含了全部重要的天气信息。
    """
    # Step 1. 构建请求 URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Step 2. 设置查询参数，包括城市名、API Key、单位和语言
    params = {
        "q": loc,
        #"appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key
        "appid": "fc19f7b552b4c1ae467e36fe69556668",  # 从环境变量中读取 API Key
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }

    # Step 3. 发送 GET 请求获取天气数据
    # 【理解这一行】实际 HTTP 请求发生在这里；timeout 限制等待，但仍应检查状态码再解释响应体。
    response = httpx.get(url, params=params,timeout=30)

    # Step 4. 解析响应内容为 JSON 并序列化为字符串返回
    data = response.json()
    print(json.dumps(data))
    return json.dumps(data)


# 初始化模型实例，用于处理自然语言任务
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 创建聊天提示模板，定义agent的对话结构和角色
# 【理解这一行】根据角色消息描述创建模板；具体变量稍后在 format_messages/invoke 时填入。
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "你是天气助手，请根据用户的问题，给出相应的天气信息"),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)

# 定义可用工具列表，包含获取天气信息的工具函数
tools = [get_weather]

# 创建工具调用agent，整合语言模型、工具和提示模板。该agent能够根据用户问题调用相应工具获取天气信息
# 【理解这一行】创建旧式工具调用 Agent 逻辑；后续还需要 AgentExecutor 驱动执行。
agent = create_tool_calling_agent(llm, tools, prompt)

# 创建agent执行器，负责协调agent和工具的执行流程
# agent参数指定要执行的agent实例
# tools参数提供agent可调用的工具列表
# verbose参数设置为True，启用详细输出模式便于调试
# 【理解这一行】驱动旧式 Agent 的多步执行，调用工具并把观察结果反馈给模型。
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# 执行agent，处理用户关于北京和上海天气的查询请求
# 【理解这一行】运行 Agent 执行流程；区分旧式 input 与新版 messages 状态格式，观察工具调用记录。
result = agent_executor.invoke({"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"})

# 输出执行结果
print(result)