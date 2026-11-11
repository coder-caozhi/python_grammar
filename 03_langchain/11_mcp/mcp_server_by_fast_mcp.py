# ============================================================================
# 学习目的：认识真正 FastMCP 的工具、资源和提示词注册
# 技术讲解：tool 暴露可调用能力；resource 暴露可读取数据；prompt 暴露提示词模板
# 阅读路线：创建 FastMCP → 三种装饰器注册 → stdio 启动
# 当前代码要注意：stdio 通常由客户端启动子进程并通过标准输入输出通信，不能当作普通打印脚本；旧 pywin32 错误记录不代表当前环境
# 动手验证：比较 add、get_greeting、greet_user 分别属于哪种能力
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install mcp
# pip install pywin32
from mcp.server.fastmcp import FastMCP

# 创建 MCP 实例
# 【理解这一行】创建 SDK 服务对象；装饰器负责登记能力，run 负责启动选定传输。
mcp = FastMCP("Demo")

# 为 MCP 实例添加工具
@mcp.tool()
def add(a: int, b: int) -> int:
    return a + b

# 为 MCP 实例添加资源
@mcp.resource("greeting://default")
def get_greeting() -> str:
    return "Hello from static resource!"

# 为 MCP 实例添加提示词
@mcp.prompt()
def greet_user(name: str, style: str = "friendly") -> str:
    styles = {
        "friendly": "写一句友善的问候",
        "formal": "写一句正式的问候",
        "casual": "写一句轻松的问候",
    }
    return f"为{name}{styles.get(style, styles['friendly'])}"

if __name__ == "__main__":
    # 【理解这一行】stdio 用来与客户端交换协议消息；运行后等待输入是服务工作方式，不是普通脚本卡住。
    mcp.run(transport="stdio")


"""
import pywintypes
ModuleNotFoundError: No module named 'pywintypes'


方案 2：等待 pywin32 适配 Python 3.13（被动，无需改动环境）
如果不想降级 Python 版本，可以等待 pywin32 官方发布支持 Python 3.13 系列的版本：
"""