# ============================================================================
# 学习目的：把 Word 文件转为统一 Document
# 技术讲解：UnstructuredWordDocumentLoader 隐藏底层格式解析，single 汇总文本
# 阅读路线：定位 docx → load → 查看正文和元数据
# 当前代码要注意：需要对应解析依赖；single 不表示可以直接处理所有 Word 版式而不丢结构
# 动手验证：观察表格内容在正文里呈现成什么样
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install langchain_community unstructured[docx]
# pip install -U unstructured
# pip install python-docx
# pip install regex==2026.1.14
from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = UnstructuredWordDocumentLoader(
    # 文件路径
    file_path="assets/alibaba-more.docx",
    # 加载模式:
    #   single 返回单个Document对象
    #   elements 按标题等元素切分文档
    mode="single",
).load()

#print(type(docs))
print(docs)

