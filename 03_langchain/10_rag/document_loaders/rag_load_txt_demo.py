# ============================================================================
# 学习目的：从最简单的文本文件理解 Document
# 技术讲解：page_content 放正文，metadata 保存来源等信息
# 阅读路线：设置文件路径与编码 → TextLoader.load → 输出
# 当前代码要注意：assets 路径相对工作目录；编码要与文件实际保存格式一致
# 动手验证：打印 docs[0].page_content 和 docs[0].metadata
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


# pip install langchain_community
from langchain_community.document_loaders import TextLoader

# 返回List[Document]
file_path = "assets/sample.txt"  # 文件路径
encoding = "utf-8"  # 文件编码方式

# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = TextLoader(file_path, encoding).load()

print(docs)
# [Document(metadata={'source': 'asset/sample.txt'}, page_content='...')]
