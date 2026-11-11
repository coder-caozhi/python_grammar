# ============================================================================
# 学习目的：把文本向量写入 Redis 并检索相近文档
# 技术讲解：Document 保存正文与元数据；embedding 编码文本；retriever 返回相关 Document
# 阅读路线：构造文档 → from_documents 编码入库 → k=2 检索
# 当前代码要注意：需要支持向量检索的 Redis；重复运行可能新增数据，普通 Redis 键值能力不等于已具备搜索索引
# 动手验证：对比检索结果的 page_content 和 metadata
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install langchain-community dashscope redis redisvl
import os
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis
from langchain_core.documents import Document

# 1. 初始化阿里千问 Embedding 模型
# 【理解这一行】创建文本编码器；embedding 是数值向量，不是自然语言回答。
embeddings = DashScopeEmbeddings(
    model="text-embedding-v3",  # 支持 v1 或 v2
    dashscope_api_key=os.getenv("aliQwen-api")  # 从环境变量读取
)


# 2. 准备要向量化的文本（Document 列表）
texts = [
    "通义千问是阿里巴巴研发的大语言模型。",
    "Redis 是一个高性能的键值存储系统，支持向量检索。",
    "LangChain 可以轻松集成各种大模型和向量数据库。"
]
# 【理解这一行】正文放 page_content，来源等附加信息放 metadata；两者用途不同。
documents = [Document(page_content=text, metadata={"source": "manual"}) for text in texts]

# 3. 连接到 Redis 并存入向量（自动调用 embeddings 嵌入）
# 【理解这一行】对文档编码并写入向量存储，可能请求远端 embedding 服务并修改 Redis 数据。
vector_store = Redis.from_documents(
    documents=documents,
    embedding=embeddings,
    redis_url="redis://localhost:26379",  # 替换为你的 Redis 地址
    index_name="my_index11",               # 向量索引名称
)

# 4. （可选）后续可直接用于检索
# 【理解这一行】把向量存储转换为检索器；k 控制期望返回的相关文档数量。
retriever = vector_store.as_retriever(search_kwargs={"k": 2})
# 【理解这一行】检索器接收查询字符串，返回相关 Document；不是直接生成自然语言回答。
results = retriever.invoke("LangChain 和 Redis 怎么结合？")
for res in results:
    print(res.page_content)

