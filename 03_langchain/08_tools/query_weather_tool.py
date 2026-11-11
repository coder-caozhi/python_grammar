# ============================================================================
# 学习目的：把 HTTP 查询包装为天气工具
# 技术讲解：工具 loc 输入 → HTTP 参数 → JSON 响应 → JSON 字符串输出
# 阅读路线：@tool 注册 → 读取天气密钥 → httpx.get → 序列化
# 当前代码要注意：底部直接调用意味着 import 本模块也会查询天气；未调用 load_dotenv，须由入口加载配置；未检查 HTTP 错误状态
# 动手验证：说明为什么导入本文件可能触发网络请求
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain_core.tools import tool
import json
import os
import httpx


@tool
def get_weather(loc):
    """
    查询即时天气函数

    :param loc: 必要参数，字符串类型，用于表示查询天气的具体城市名称。
                注意，中国的城市需要用对应城市的英文名称代替，例如如果需要查询北京市天气，
                则 loc 参数需要输入 'Beijing'/'shanghai'。
    :return: OpenWeather API 查询即时天气的结果。具体 URL 请求地址为：
             https://home.openweathermap.org/users/sign_in。
             返回结果对象类型为解析之后的 JSON 格式对象，并用字符串形式进行表示，
             其中包含了全部重要的天气信息。
    """
    # Step 1. 构建请求 URL
    url = "https://api.openweathermap.org/data/2.5/weather"

    # Step 2. 设置查询参数，包括城市名、API Key、单位和语言
    params = {
        "q": loc,
        "appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key
        #"appid": "fc19f7b552b4c1ae467e36fe6955666",  # 从环境变量中读取 API Key
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }

    # Step 3. 发送 GET 请求获取天气数据
    # 【理解这一行】实际 HTTP 请求发生在这里；timeout 限制等待，但仍应检查状态码再解释响应体。
    response = httpx.get(url, params=params, timeout=30)

    # Step 4. 解析响应内容为 JSON 并序列化为字符串返回
    data = response.json()
    #print(json.dumps(data))
    return json.dumps(data)


# 测试
# result = get_weather.invoke("shanghai")
# 【理解这一行】这段位于模块顶层，所以导入本文件也会触发一次 HTTP 查询，不只在直接运行时执行。
result = get_weather.invoke("beijing")
print(result)

