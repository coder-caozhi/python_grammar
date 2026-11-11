# ============================================================================
# 学习目的：使用 LangChain embedding 接口编码单文本和多文本
# 技术讲解：embed_query 返回一个向量，embed_documents 返回向量列表
# 阅读路线：创建编码器 → 单句编码 → 多句编码 → 检查数量与维度
# 当前代码要注意：本例未显式加载 .env，也未传自定义 aliQwen-api；默认凭据来源需与集成包要求对应
# 动手验证：比较 len(query_result) 与 len(doc_results)，解释二者分别统计什么
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
https://bailian.console.aliyun.com/cn-beijing/?tab=api#/api/?type=model&url=2587654
pip install langchain-community dashscope
"""

from langchain_community.embeddings import DashScopeEmbeddings

# 【理解这一行】创建文本编码器；embedding 是数值向量，不是自然语言回答。
embeddings = DashScopeEmbeddings(
    model="text-embedding-v4",
    # other params...
)

text = "This is a test document."

# 【理解这一行】把单条文本编码成一个向量；通常与查询时的向量化对应。
query_result = embeddings.embed_query(text)
print("文本向量长度：", len(query_result), sep='')
#
# 【理解这一行】把文本列表编码成向量列表；注意样本数与单个向量维度是两个不同长度。
doc_results = embeddings.embed_documents(
    [
        "Hi there!",
        "Oh, hello!",
        "What's your name?",
        "My friends call me World",
        "Hello World!"
    ])
print(doc_results)
print("文本向量数量：", len(doc_results), "，文本向量长度：", len(doc_results[0]), sep='')