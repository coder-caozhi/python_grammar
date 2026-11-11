# ============================================================================
# 学习目的：切分已有 Document 并保留来源信息
# 技术讲解：split_documents 接受 Document 列表，输出仍是 Document 列表
# 阅读路线：加载 rag.txt → 设置长度/重叠 → 切分 → 查看 metadata
# 当前代码要注意：length_function=len 统计字符而不是模型 token；依赖 Unstructured 解析环境
# 动手验证：比较切分前后的来源 metadata 是否保留
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

"""
分割文档对象
RecursiveCharacterTextSplitter不仅可以分割纯文本，还可以直接分割Document对象
"""
# pip install python-magic-bin
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_unstructured import UnstructuredLoader

# 1.创建文档加载器，进行文档加载
loader = UnstructuredLoader("rag.txt")
# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
documents = loader.load()

# 2.定义递归文本分割器
# 创建RecursiveCharacterTextSplitter实例，用于将文档分割成指定大小的文本块
# chunk_size: 每个文本块的最大字符数为100
# chunk_overlap: 相邻文本块之间的重叠字符数为30
# length_function: 使用len函数计算文本长度
# 【理解这一行】chunk_size 是目标块大小，overlap 保留上下文重叠；本例 len 统计字符，不是 token。
text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=30, length_function=len)

# 3.分割文本
# 使用文本分割器将加载的文档分割成多个较小的文档片段
# 【理解这一行】输入和输出都是 Document 列表，切分正文时保留来源元数据。
splitter_documents = text_splitter.split_documents(documents)

# 输出分割后的文档信息
print(f"分割文档数量：{len(splitter_documents)}")

for splitter_document in splitter_documents:
    print(f"文档片段：{splitter_document.page_content}")
    print(f"文档片段大小：{len(splitter_document.page_content)}, 文档元数据：{splitter_document.metadata}")

