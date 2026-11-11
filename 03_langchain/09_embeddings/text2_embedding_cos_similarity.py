# ============================================================================
# 学习目的：用向量夹角比较文本语义
# 技术讲解：余弦相似度是点积除以两个向量长度乘积，通常越大方向越相近
# 阅读路线：三段文本分别编码 → 收集向量 → 两两计算 → 比较水果与手机语义
# 当前代码要注意：当前实现未处理零向量；若任一 API 失败，embeddings 变短可能导致索引错误；实际使用 numpy 而非 sklearn
# 动手验证：先用 [1,0] 与 [0,1] 手算结果，理解公式再看模型向量
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
把文本转换成向量有什么用呢？
最核心的作用是可以通过向量之间的计算，来分析文本与文本之间的相似性。
计算的方法有很多种，其中用得最多的是向量余弦相似度。
Python语言中提供了一个库sklearn，可以很方便的计算向量之间的余弦相似度
"""

import dashscope
import os
from http import HTTPStatus
import numpy as np


# 准备输入文本数据
texts = [
    '我喜欢吃苹果',
    '苹果是我最喜欢吃的水果',
    '我喜欢用苹果手机'
]

# 获取每个文本的embedding向量
embeddings = []
# 假如要处理图片，请参考https://bailian.console.aliyun.com/cn-beijing/?productCode=p_efm&tab=doc#/doc/?type=model&url=2842587
for text in texts:
    input_data = [{'text': text}]
    resp = dashscope.MultiModalEmbedding.call(
        model="multimodal-embedding-v1",
        api_key=os.getenv("aliQwen-api"),
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
        input=input_data
    )

    if resp.status_code == HTTPStatus.OK:
        embedding = resp.output['embeddings'][0]['embedding']
        embeddings.append(embedding)

# 计算余弦相似度
def cosine_similarity(vec1, vec2):
    # 计算两个向量的余弦相似度
    dot_product = np.dot(vec1, vec2)
    norm_vec1 = np.linalg.norm(vec1)
    norm_vec2 = np.linalg.norm(vec2)
    # 【理解这一行】公式：cos(a,b)=点积/(范数乘积)；零向量会造成除零，不能把此实现当作已处理所有边界。
    return dot_product / (norm_vec1 * norm_vec2)

# 比较所有文本之间的相似度
print("文本相似度比较结果:")
print("=" * 60)

for i in range(len(texts)):
    for j in range(i+1, len(texts)):
        # 【理解这一行】这里假定每个 API 调用都成功；失败会导致向量列表与 texts 不再一一对应。
        similarity = cosine_similarity(embeddings[i], embeddings[j])
        print(f"文本{i+1} vs 文本{j+1}:")
        print(f"  文本{i+1}: {texts[i]}")
        print(f"  文本{j+1}: {texts[j]}")
        print(f"  余弦相似度: {similarity:.4f}")
        print("-" * 40)
