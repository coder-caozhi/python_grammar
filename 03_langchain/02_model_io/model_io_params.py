# ============================================================================
# 学习目的：观察 temperature 对重复生成的影响
# 技术讲解：temperature 调节采样随机性，不是答案正确率或稳定性的保证
# 阅读路线：配置同一模型 → 同一问题调用三次 → 比较措辞
# 当前代码要注意：模型输出可能相同也可能不同，不能用一次实验断言温度必然造成某种结果
# 动手验证：比较较低和较高温度下的重复输出，并记录变化而不是预设结论
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
模型参数演示
"""
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model

# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    temperature=2.0

)

# 3.调用模型
for x in range(3):
    # 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
    print(model.invoke("写一句关于春天的词,14字以内").content)