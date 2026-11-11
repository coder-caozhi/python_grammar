# ============================================================================
# 学习目的：把最小模型调用组织成可复用的函数和入口
# 技术讲解：配置校验、日志、异常处理、普通响应与流式分片各负其责
# 阅读路线：init_llm_client 检查配置 → main 调用 → stream 迭代 → 捕获异常
# 当前代码要注意：流式输出的 chunk 不是完整回答；本例兜底捕获 Exception 不代表所有错误都属于 LangChainException
# 动手验证：指出配置缺失和远端请求失败分别进入哪条处理路径
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# 导入必要的库
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv
from langchain_core.exceptions import LangChainException

# 加载.env文件中的环境变量（指定编码，避免中文乱码）
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv(encoding='utf-8')

# 配置日志（可选，便于调试）
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def init_llm_client() -> ChatOpenAI:
    """
    初始化LLM客户端（封装成函数，提高复用性）

    Returns:
        ChatOpenAI: 初始化后的LLM客户端实例
    """
    # 1. 读取环境变量并做非空校验
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise ValueError("环境变量 DEEPSEEK_API_KEY 未配置，请检查 .env 文件")

    # 2. 初始化LLM客户端（参数命名规范，添加注释）
    # 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
    llm = ChatOpenAI(
        model="deepseek-chat",  # 模型名称
        api_key=api_key,
        base_url="https://api.deepseek.com",
        temperature=0.7,  # 可选：添加温度参数，控制输出随机性
        max_tokens=2048  # 可选：限制输出长度，避免超限
    )
    return llm


def main():
    """主函数：封装核心逻辑，符合Python工程化规范"""
    try:
        # 初始化客户端
        llm = init_llm_client()
        logger.info("LLM客户端初始化成功")

        # 调用模型（问题用变量存储，提高可读性）
        question = "你是谁"
        # 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
        response = llm.invoke(question)

        # 格式化输出结果（而非直接打印原始对象）
        logger.info(f"问题：{question}")
        logger.info(f"回答：{response.content}")

        print("====================以下是流式输出,另一种调用方式")
        print("*" * 50)
        # 【理解这一行】返回分片迭代对象，需继续遍历才能读出输出；每块不是整段回答。
        responseStream = llm.stream("介绍下langchain，300字以内")
        for chunk in responseStream:
            print(chunk.content,end="")
    # 捕获具体异常（而非宽泛的Exception）
    except ValueError as e:
        logger.error(f"配置错误：{str(e)}")
    except LangChainException as e:
        logger.error(f"模型调用失败：{str(e)}")
    except Exception as e:
        logger.error(f"未知错误：{str(e)}")


# 脚本入口（符合Python规范，避免导入时执行代码）
if __name__ == "__main__":
    main()