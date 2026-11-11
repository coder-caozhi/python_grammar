# ============================================================================
# 学习目的：按元素读取 Markdown 内容和结构信息
# 技术讲解：elements 模式倾向于为标题、段落等元素生成文档记录
# 阅读路线：文件 → UnstructuredMarkdownLoader → Document 列表
# 当前代码要注意：元素切分不等于固定长度 RAG 分块；仍可能需要后续 splitter
# 动手验证：比较不同文档记录中的 category 元数据
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install langchain_community unstructured[md]
from langchain_community.document_loaders import UnstructuredMarkdownLoader

# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = UnstructuredMarkdownLoader(
    # 文件路径
    file_path="assets/sample.md",
    # 加载模式:
    #   single 返回单个Document对象
    #   elements 按标题等元素切分文档
    mode="elements",
).load()

print(docs)
