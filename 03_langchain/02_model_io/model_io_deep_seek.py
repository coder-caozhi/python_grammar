# ============================================================================
# 学习目的：认识 DeepSeek 专用适配器与环境配置定位
# 技术讲解：ChatDeepSeek 是供应商集成类；模型名、超时、重试分别控制不同层面
# 阅读路线：load_env 从文件位置向上找配置 → 创建模型 → invoke
# 当前代码要注意：override=True 会覆盖已有同名环境变量；timeout=None 不设置该客户端的请求超时，不能理解为请求一定成功
# 动手验证：在断点观察 env_file 路径与模型类型，不打印密钥值
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install -U langchain-deepseek
import os
from pathlib import Path

from dotenv import load_dotenv


def load_env() -> None:
    """按本文件位置向上查找 .env（load_dotenv() 不传参时，Debug/控制台下会用 os.getcwd()，容易找不到）。"""
    here = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
    for base in (here, Path.cwd()):
        for folder in (base, *base.parents):
            env_file = folder / ".env"
            if env_file.is_file():
                # 【理解这一行】显式文件位置避免工作目录歧义；override=True 会让文件中的值覆盖已有同名环境变量。
                load_dotenv(env_file, encoding="utf-8", override=True)
                return
    # 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
    load_dotenv(encoding="utf-8")


load_env()
from langchain_deepseek import ChatDeepSeek


# 初始化 deepseek
# 为什么不写调用地址：langchain_deepseek/chat_models.py 里已内置默认值
#   - 第 34 行：DEFAULT_API_BASE = "https://api.deepseek.com/v1"
#   - 第 256 行：api_base 字段 default_factory 从环境变量 DEEPSEEK_API_BASE 取值，缺省即 DEFAULT_API_BASE
# 同理第 251 行：api_key 的 default_factory 会自动读环境变量 DEEPSEEK_API_KEY
# 【理解这一行】创建 DeepSeek 专用集成客户端；凭据从环境获取，生成内容由后面的 invoke 发起。
model = ChatDeepSeek(
    model="deepseek-chat",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    # api_base="https://api.deepseek.com",  # 需要覆盖时再显式写
)

# 打印结果（打印 .content 只取文本，直接 print 会输出整个 AIMessage 对象）
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(model.invoke("什么是LangChain?100字以内回答，简洁").content)
