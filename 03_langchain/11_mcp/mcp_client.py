# ============================================================================
# 学习目的：辨别本地工具调用与真正 MCP 客户端通信
# 技术讲解：import mcp_server 获得同进程对象，_tools 字典直接找到并调用函数
# 阅读路线：导入注册表 → 查工具 → 本地函数调用 → 天气 HTTP 请求
# 当前代码要注意：这里没有 MCP 会话、JSON-RPC、SSE 或 stdio 传输；不需要先启动另一个模拟 server 进程
# 动手验证：沿 call_get_weather 找出唯一真正访问网络的代码位于哪个函数
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import json
from loguru import logger
# 【理解这一行】这是 Python 本地模块导入，不是连接远程 MCP 服务。
from mcp_server import mcp


class MCPWeatherClient:
    """MCP 天气服务客户端，用于访问 MCPWeatherServer 服务端"""

    def __init__(self, mcp_instance):
        self.mcp_instance = mcp_instance
        self.available_tools = mcp_instance._tools  # 获取服务端已注册的所有工具

    def check_tool_availability(self, tool_name: str) -> bool:
        """检查指定工具是否在服务端已注册"""
        is_available = tool_name in self.available_tools
        if is_available:
            logger.info(f"工具 '{tool_name}' 可用")
        else:
            logger.warning(f"工具 '{tool_name}' 未在服务端注册")
        return is_available

    def call_get_weather(self, city: str) -> str or None:
        """调用服务端的 get_weather 工具，查询指定城市天气"""
        tool_name = "get_weather"
        if not self.check_tool_availability(tool_name):
            return None

        try:
            # 调用服务端已注册的工具函数
            # 【理解这一行】这里从本地字典取函数并调用，没有经过协议传输。
            weather_result = self.available_tools[tool_name](city)
            logger.info(f"成功获取 {city} 天气数据，返回结果长度：{len(weather_result)}")
            return weather_result
        except Exception as exc:
            logger.error(f"调用 {tool_name} 工具失败：{str(exc)}")
            return None


def run_client_demo():
    """客户端演示程序"""
    # 1. 初始化客户端（传入服务端的 mcp 实例）
    logger.info("初始化 MCP 天气客户端...")
    client = MCPWeatherClient(mcp)

    # 2. 调用天气查询工具（支持 Beijing、Shanghai、Guangzhou 等英文城市名）
    target_cities = ["Beijing", "Shanghai"]
    for city in target_cities:
        logger.info(f"\n========== 查询 {city} 天气 ==========")
        weather_data = client.call_get_weather(city)
        if weather_data:
            # 格式化输出结果（可选，方便阅读）
            formatted_data = json.dumps(json.loads(weather_data), indent=4, ensure_ascii=False)
            print(f"格式化天气结果：\n{formatted_data}")
        print("-" * 50)


if __name__ == "__main__":
    logger.info("启动 MCP 天气客户端...")
    # 确保服务端已启动（服务端进程需先运行，客户端才能正常导入 mcp 实例）
    logger.warning("请确认 MCPWeatherServer 服务端已正常启动！")
    run_client_demo()