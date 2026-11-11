# ============================================================================
# 学习目的：理解 RedisVectorStore 写入文本和元数据
# 技术讲解：索引配置定义存储位置；add_texts 会调用 embedding 并返回记录 ID
# 阅读路线：先单独编码展示 → 配置索引 → add_texts → 打印 ID
# 当前代码要注意：前面的 embeddings 并未传给 add_texts，写入时会再次编码；输出写前5个实际切片为10个
# 动手验证：解释一次演示为什么可能产生两轮 embedding 请求
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


from langchain_redis import RedisConfig, RedisVectorStore
from langchain_community.embeddings import DashScopeEmbeddings
import os

# 初始化 Embedding 模型
# 1. 初始化阿里千问 Embedding 模型
# 【理解这一行】创建文本编码器；embedding 是数值向量，不是自然语言回答。
embeddingsModel = DashScopeEmbeddings(
    model="text-embedding-v3",  # 支持 v1 或 v2
    dashscope_api_key=os.getenv("aliQwen-api")  # 从环境变量读取
)

# ========== 存储数据 ==========
# 定义待处理的文本数据列表
texts = [
    "我喜欢吃苹果",
    "苹果是我最喜欢吃的水果",
    "我喜欢用苹果手机",
]
# query_result = embeddings.embed_query(texts)
# print(query_result)


# 获取文本向量
# 使用embedding模型将文本转换为向量表示
# 【理解这一行】把文本列表编码成向量列表；注意样本数与单个向量维度是两个不同长度。
embeddings = embeddingsModel.embed_documents(texts)

# 打印结果
# 遍历并打印每个文本及其对应的向量信息
for i, vec in enumerate(embeddings, 1):
    print(f"文本 {i}: {texts[i-1]}")
    print(f"向量长度: {len(vec)}")
    print(f"前5个向量值: {vec[:10]}\n")

# 定义每条文本对应的元数据信息
metadata = [{"segment_id": "1"}, {"segment_id": "2"}, {"segment_id": "3"}]

# 配置Redis连接参数和索引名称
# 【理解这一行】配置索引名称与服务地址；写入和检索必须使用兼容的模型及向量维度。
config = RedisConfig(
    index_name="newsgroups",
    redis_url="redis://localhost:26379",
)

# 创建Redis向量存储实例
# 【理解这一行】连接向量存储抽象；真正写入/检索分别在 add_texts 和搜索调用中发生。
vector_store = RedisVectorStore(embeddingsModel, config=config)

# 将文本和元数据添加到向量存储中
# 【理解这一行】add_texts 自己编码文本，未使用前面已算好的 embeddings；所以本例有重复编码开销。
ids = vector_store.add_texts(texts, metadata)

# 打印前5个存储记录的ID
print(ids[0:5])