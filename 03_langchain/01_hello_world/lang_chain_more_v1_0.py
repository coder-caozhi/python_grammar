# ============================================================================
# 学习目的：观察统一模型入口创建出的客户端对象
# 技术讲解：客户端对象保存配置；invoke 才发起本例的聊天请求
# 阅读路线：创建 model → 检查 __dict__ → 提取回答 content
# 当前代码要注意：__dict__ 是实现细节，不宜作为稳定业务接口，也不要把配置输出直接分享
# 动手验证：只观察类型和模型名，解释为什么同一客户端可回答不同问题
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# LangChain1.0+版本使用方式,目前主流,多模型共存


# 1.导入依赖
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
import os
# .env文件读取
# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()

# 2.实例化模型
# model = init_chat_model(
#     model="deepseek-chat",
#     model_provider="openai",
#     api_key=os.getenv("DEEPSEEK_API_KEY"),
#     base_url="https://api.deepseek.com"
# )
#
# # 3.调用模型
# print(model.invoke("你是谁").content)
#
# print("*" * 70)

# 4.实例化模型v2
"""
说明：
这里通过 OpenAI 兼容接口连接 DeepSeek，因此显式设置 model_provider="openai"。
"""
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat", # deepseek-chat 对应 DeepSeek-V3.2 的非思考模式
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 5.调用模型v2
print(model.__dict__)
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(model.invoke("你是谁").content)