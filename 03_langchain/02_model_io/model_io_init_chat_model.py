# ============================================================================
# 学习目的：把配置查找和模型初始化连接成完整调用路径
# 技术讲解：Path(__file__) 定位脚本；init_chat_model 通过 provider 创建具体适配器
# 阅读路线：查找 .env → 检查 DEEPSEEK_API_KEY → 初始化 → 提问
# 当前代码要注意：load_dotenv 默认搜索起点与脚本/调试/交互场景有关；旧说明中的“始终从 cwd 开始”不适用于所有情况
# 动手验证：解释为什么显式传入 env_file 比依赖工作目录更容易定位问题
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 1.导入依赖
import os
from pathlib import Path

from dotenv import load_dotenv


def load_env() -> None:
    """
    加载 .env 文件。

    坑：load_dotenv() 默认只从**当前工作目录**（os.getcwd()）开始向上查找 .env，
    而不是从本文件所在目录查找。
    在 PyCharm 控制台 / 项目根目录下运行时，工作目录是 D:\\python\\python_grammar，
    那里没有 .env，于是 os.getenv("DEEPSEEK_API_KEY") 返回 None，
    最终抛出 OpenAIError: Missing credentials...
    """
    # __file__ 在交互式控制台（Python Console）中可能不存在，需要做兼容
    here = Path(__file__).resolve().parent if "__file__" in globals() else Path.cwd()
    for base in (here, Path.cwd()):  # 先按本文件位置找，再按工作目录找
        for folder in (base, *base.parents):
            env_file = folder / ".env"
            if env_file.is_file():
                # 【理解这一行】显式加载已找到的文件；默认 load_dotenv 的搜索规则会随脚本/调试/交互场景有所不同。
                load_dotenv(env_file, override=True)
                return
    # 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
    load_dotenv()  # 兜底：交给 python-dotenv 自己搜索


load_env()

from langchain.chat_models import init_chat_model

# 2.实例化模型
api_key = os.getenv("DEEPSEEK_API_KEY")
if not api_key:
    raise RuntimeError(
        "没有读取到 DEEPSEEK_API_KEY。请确认 D:\\python\\python_grammar\\03_langchain\\.env 中配置了："
        "DEEPSEEK_API_KEY=sk-xxxx"
    )

# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

# 3.调用模型
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(model.invoke("你是谁").content)