# ============================================================================
# 学习目的：通过 DashScope 原生 SDK 生成文本向量
# 技术讲解：TextEmbedding.call 返回状态码、向量数据和用量等结构
# 阅读路线：设置 input_text → 调用 → HTTPStatus.OK 时打印
# 当前代码要注意：未显式传密钥或加载 .env；依赖 SDK 的环境配置，失败分支目前没有输出
# 动手验证：找到响应中的向量字段，而不是把整个响应当作数值向量
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587

import dashscope
from http import HTTPStatus

# 【理解这一行】TextEmbedding.call 返回状态码、向量数据和用量等结构
input_text = "衣服的质量杠杠的"

resp = dashscope.TextEmbedding.call(
    model="text-embedding-v4",
    input=input_text,
)

if resp.status_code == HTTPStatus.OK:
    print(resp)


