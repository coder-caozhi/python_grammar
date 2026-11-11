# ============================================================================
# 学习目的：认识新版 Agent 创建方式与结构化结果
# 技术讲解：create_agent 同时配置工具和 response_format，结构化结果放在 structured_response
# 阅读路线：工具 → WeatherCompareOutput → Agent → 调用 → 输出结构化字段
# 当前代码要注意：当前仍传旧式 input；新版通常应使用 messages 状态输入，不能保证该例直接运行；工具注解 dict 实际返回 JSON 字符串
# 动手验证：与 agent_react 的 messages 输入格式对照，指出接口迁移差异
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
import json
import httpx
from typing import TypedDict

from langchain.agents import create_agent
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI


# 1.Tool 定义
@tool
def get_weather(loc: str) -> dict:
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称。
                注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，
                则 loc 参数需要输入 'Beijing'/'shanghai'。
    :return: OpenWeather API 查询即时天气的结果。
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": loc,
        "appid": os.getenv("OPENWEATHER_API_KEY"),
        "units": "metric",
        "lang": "zh_cn"
    }
    # 【理解这一行】实际 HTTP 请求发生在这里；timeout 限制等待，但仍应检查状态码再解释响应体。
    response = httpx.get(url, params=params, timeout=30)
    data = response.json()
    #print(json.dumps(data, ensure_ascii=False, indent=2))
    # 【理解这一行】json.dumps 返回 str，与函数签名的 -> dict 不一致；注解不会自动把字符串转为字典。
    return json.dumps(data, ensure_ascii=False)



# 2 结构化输出（推荐）
class WeatherCompareOutput(TypedDict):
    beijing_temp: float
    shanghai_temp: float
    hotter_city: str
    summary: str


# 3 模型（OpenAI Compatible）
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
model = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
)


# 4 创建Agent
# 【理解这一行】创建能够执行工具循环的 Agent；模型可提出工具调用，执行器负责运行并回填结果。
agent = create_agent(
    model=model,
    tools=[get_weather],
    system_prompt=(
        "你是天气助手。"
        "当用户询问多个城市天气时，"
        "你需要分别调用工具获取数据，并进行比较分析。"
    ),
    response_format=WeatherCompareOutput,
)

# 5 调用Agent
# 【理解这一行】这里仍用旧式 input；请对照 agent_react.py 的 {"messages": [...]}，本次仅讲解未改接口。
result = agent.invoke(
    {"input": "请问今天北京和上海的天气怎么样，哪个城市更热？"}
)
print(result)

print()

print(json.dumps(result["structured_response"], ensure_ascii=False, indent=2))