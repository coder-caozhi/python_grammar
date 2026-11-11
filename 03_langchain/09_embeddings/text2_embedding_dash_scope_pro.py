# ============================================================================
# 学习目的：观察多模态 embedding 接口的请求和响应结构
# 技术讲解：input 使用记录列表；返回对象含 output/usage/request_id
# 阅读路线：构造文本记录 → MultiModalEmbedding.call → 提取元信息 → JSON 展示
# 当前代码要注意：虽然接口支持多模态，本例只输入文本；模型名、鉴权参数及区域支持须以所装 SDK/服务为准，不能仅凭旧注释判定
# 动手验证：比较原生响应与整理后的 result 字典
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import dashscope
import json
import os
from http import HTTPStatus

# Embedding 文本向量化

# 调用多模态embedding模型接口进行向量编码
# https://bailian.console.aliyun.com/?productCode=p_efm&tab=model#/model-market/all?capabilities=ME
# 【理解这一行】input 使用记录列表；返回对象含 output/usage/request_id
resp = dashscope.MultiModalEmbedding.call(
    model="tongyi-embedding-vision-plus",  # 支持 v1 或 v2
    dashscope_api_key=os.getenv("aliQwen-api"),  # 从环境变量读取
    input=[{"text": "尚硅谷AI"}]
)

result = "";

# 处理模型返回结果，提取关键信息并格式化输出
if resp.status_code == HTTPStatus.OK:
    result = {
        "status_code": resp.status_code,
        "request_id": getattr(resp, "request_id", ""),
        "code": getattr(resp, "code", ""),
        "message": getattr(resp, "message", ""),
        "output": resp.output,
        "usage": resp.usage
    }
    print(json.dumps(result, ensure_ascii=False, indent=4))

print("=================================")
print()

# result 就是你已经拿到的完整 dict
# embedding_values = result["output"]["embeddings"][0]["embedding"]
# print(embedding_values)
# print("=================================")
# print("=================================")
# # 只打印 embedding 数组
# print(json.dumps(embedding_values, ensure_ascii=False))


