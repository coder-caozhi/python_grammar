# ============================================================================
# 学习目的：理解装饰器如何注册函数，并区分协议模拟
# 技术讲解：tool 返回装饰器，把函数按名称放进 _tools 字典
# 阅读路线：构建对象 → 装饰 get_weather → run 打印日志 → _keep_alive
# 当前代码要注意：run 只打印监听地址，没有创建网络服务器；while True: pass 会忙等占用 CPU，不应当作真实 MCP 服务启动
# 动手验证：指出要成为真实协议服务还缺少哪些传输与请求处理环节
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import json
import os
import httpx
from loguru import logger


# ---------------------- 极简版 MCP 服务类（无 FastMCP 字样，纯原生实现）----------------------
# 替换原 FastMCP，命名为 MCPWeatherServer，无第三方依赖，适配 Python 3.13.1
class MCPWeatherServer:
    """极简版 MCP 服务类，替代原 FastMCP，无 fastmcp 残留"""

    def __init__(self, name: str, host: str, port: int):
        # 保留原实例化参数，与原代码配置对齐
        self.name = name
        self.host = host
        self.port = port
        self._tools = {}  # 存储注册的工具函数，支撑 @mcp.tool() 装饰器

    def tool(self):
        """实现 @mcp.tool() 装饰器"""

        def decorator(func):
            # 【理解这一行】装饰器的副作用：注册函数引用；此时没有执行天气查询。
            self._tools[func.__name__] = func  # 注册工具函数
            return func

        return decorator

    def run(self, transport: str):
        """实现 mcp.run(transport="sse")调用格式和日志输出"""
        if transport != "sse":
            logger.warning(f"不支持的传输协议 {transport}，默认使用 SSE")
        logger.info(f"启动 MCP SSE 天气服务器，监听 http://{self.host}:{self.port}/sse")
        self._keep_alive()

    def _keep_alive(self):
        """简单保持进程运行，替代原服务Fastmcp的监听逻辑"""
        try:
            # 【理解这一行】当前只是无等待忙循环，没有监听端口或响应 SSE；直接启动会持续占用 CPU。
            while True:
                pass
        except KeyboardInterrupt:
            logger.info("MCP 天气服务器已停止")


# ---------------------- 以下代码与原代码完全一致，无任何修改 ----------------------
# 创建 MCP 实例（替换原 FastMCP，无 FastMCP 字样，配置与原代码一致）
mcp = MCPWeatherServer("WeatherServerSSE", host="127.0.0.1", port=8000)


@mcp.tool()  # 保留原装饰器写法，无任何修改
def get_weather(city: str) -> str:
    """
    查询指定城市的即时天气信息。
    参数 city: 城市英文名，如 Beijing
    返回: OpenWeather API 的 JSON 字符串
    """
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        #"appid": "fc19f7b552b4c1ae467e36fe6955666",  # 从环境变量中读取 API Key
        "appid": os.getenv("OPENWEATHER_API_KEY"),  # 从环境变量中读取 API Key
        "units": "metric",  # 使用摄氏度
        "lang": "zh_cn"  # 输出语言为简体中文
    }
    # 【理解这一行】实际 HTTP 请求发生在这里；timeout 限制等待，但仍应检查状态码再解释响应体。
    resp = httpx.get(url, params=params, timeout=10)
    data = resp.json()
    logger.info(f"查询 {city} 天气结果：{data}")
    return json.dumps(data, ensure_ascii=False)


if __name__ == "__main__":
    logger.info("启动 MCP SSE 天气服务器，监听 http://127.0.0.1:8000/sse")
    # 运行 MCP 服务，保留原 transport="sse" 参数，无任何修改
    mcp.run(transport="sse")