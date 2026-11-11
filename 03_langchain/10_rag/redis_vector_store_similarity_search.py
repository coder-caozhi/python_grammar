# ============================================================================
# 学习目的：根据查询向量检索已有索引并读取分数
# 技术讲解：查询先编码，再与索引向量比较，返回 Document/score 对
# 阅读路线：连接 newsgroups → similarity_search_with_score → 查看结果
# 当前代码要注意：先确保已有索引且编码模型/维度一致；1-score 只有在相应距离定义下才有意义，不是通用概率
# 动手验证：确认配置使用何种距离，再解释分数大小的含义
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

#2. 创建Redis向量存储实例
# 【理解这一行】连接向量存储抽象；真正写入/检索分别在 add_texts 和搜索调用中发生。
vector_store = RedisVectorStore(embeddingsModel,
                                config=RedisConfig(index_name="newsgroups",redis_url="redis://localhost:26379"))

# ========== 查询数据 ==========
# 定义查询文本
query = "我喜欢用什么手机"

#3. 将查询语句向量化，并在Redis中做相似度检索
# 【理解这一行】先编码查询，再返回文档与分数；分数含义需要结合存储的距离度量。
results = vector_store.similarity_search_with_score(query, k=3)

print("=== 查询结果 ===")
for i, (doc, score) in enumerate(results, 1):
    # 【理解这一行】只有确认 score 是对应定义的距离后才可这样变换；这不是概率，也不能套用于所有向量数据库。
    similarity = 1 - score  #  score 是距离，可以转成相似度
    print(f"结果 {i}:")
    print(f"内容: {doc.page_content}")
    print(f"元数据: {doc.metadata}")
    print(f"相似度: {similarity:.4f}")