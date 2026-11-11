# ============================================================================
# 学习目的：决定 CSV 哪些列进入正文、哪些列成为元数据
# 技术讲解：CSVLoader 默认按行生成 Document；content_columns/metadata_columns 控制信息归属
# 阅读路线：第一次默认加载 → 第二次指定列 → 比较 Document
# 当前代码要注意：title/author 被放入 metadata 不等于它们一定会进入模型提示词；依赖实际 CSV 列名
# 动手验证：逐项对比两次加载的 page_content 与 metadata
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install langchain_community
from langchain_community.document_loaders.csv_loader import CSVLoader

# 加载所有列
# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = CSVLoader(
    file_path="assets/sample.csv",  # 文件路径
).load()  # 返回List[Document]

print(docs)

# 加载部分列
docs = CSVLoader(
    file_path="assets/sample.csv",  # 文件路径
    metadata_columns=["title", "author"],  # 将指定列作为元数据
    content_columns=["content"],  # 将指定列作为内容
).load()  # 返回List[Document]

print(docs)
