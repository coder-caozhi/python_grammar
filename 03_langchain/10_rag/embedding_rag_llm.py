# ============================================================================
# 学习目的：串起加载、检索和回答的完整 RAG 数据流
# 技术讲解：问题分成两路：检索 context 与原样保留 question，再填模板交给模型
# 阅读路线：Word → 切分 → Redis → retriever → context/question → prompt → llm
# 当前代码要注意：本例算出 texts 后却把 documents 入库，切分结果没有用上；context 是 Document 列表，未显式拼接正文
# 动手验证：找出应在哪个位置接入 texts，以及如何把检索结果转换为纯文本
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install unstructured
# pip install docx2txt
# pip install python-docx
from langchain.chat_models  import  init_chat_model
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain_community.document_loaders import Docx2txtLoader
from langchain_core.prompts import PromptTemplate
from langchain_classic.text_splitter import CharacterTextSplitter
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import DashScopeEmbeddings
from langchain_community.vectorstores import Redis

# 没有使用RAG，直接查询大模型，出现歧义，上课时先给学生演示before情况，没有用RAG
'''llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
response=llm.invoke("00000是什么意思")
print(response.content)'''

# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

prompt_template = """
    请使用以下提供的文本内容来回答问题。仅使用提供的文本信息，
    如果文本中没有相关信息，请回答"抱歉，提供的文本中没有这个信息"。

    文本内容：
    {context}

    问题：{question}

    回答：
    "
"""

# 【理解这一行】构造字符串模板；先区分模板对象与 format/invoke 之后得到的提示词。
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# 1. 初始化阿里千问 Embedding 模型
# 【理解这一行】创建文本编码器；embedding 是数值向量，不是自然语言回答。
embeddings = DashScopeEmbeddings(
    model="text-embedding-v3",  # 支持 v1 或 v2
    dashscope_api_key=os.getenv("aliQwen-api")  # 从环境变量读取
)

# 4. 加载文档
# 4.1 TextLoader 无法处理 .docx 格式文件，专门用于加载纯文本文件的（如 .txt）
# loader = TextLoader("alibaba-more.docx", encoding="utf-8")

# 4.2 LangChain提供了Docx2txtLoader专门用于加载.docx文件，先通过pip install docx2txt
loader = Docx2txtLoader("alibaba-java.docx")  # 直接传入文件路径即可
# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
documents = loader.load()

# 5. 分割文档
# 【理解这一行】配置字符分块策略；必须把 split_documents 的结果接入入库流程才会真正使用分块。
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0, length_function=len)
# 【理解这一行】输入和输出都是 Document 列表，切分正文时保留来源元数据。
texts = text_splitter.split_documents(documents)

print(f"文档个数:{len(texts)}")

# 6. 创建向量存储
# 连接到 Redis 并存入向量（自动调用 embeddings 嵌入）
# 【理解这一行】这里传入原 documents 而非上面切出的 texts：当前入库流程没有使用分块结果。
vector_store = Redis.from_documents(
    documents=documents,
    embedding=embeddings,
    redis_url="redis://localhost:26379",  # 替换为你的 Redis 地址
    index_name="my_index3",  # 向量索引名称
)

# 【理解这一行】把向量存储转换为检索器；k 控制期望返回的相关文档数量。
retriever = vector_store.as_retriever(search_kwargs={"k": 2})

# 8. 创建Runnable链
# 【理解这一行】字典的两条分支接收同一个问题；retriever 给 Document 列表，Passthrough 保留问题字符串。
rag_chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
)

# 9. 提问
question = "00000和A0001分别是什么意思"
# 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
result = rag_chain.invoke(question)
print("\n问题:", question)
print("\n回答:", result.content)