# ============================================================================
# 学习目的：提取 PDF 文本并观察来源元数据
# 技术讲解：PyPDFLoader 将 PDF 转为文档；plain 是文本提取布局模式
# 阅读路线：打开 PDF → load → 检查页文本和 metadata
# 当前代码要注意：plain 不等于 OCR；扫描图片型 PDF 可能没有可提取文字，页划分以当前加载器设置为准
# 动手验证：查找每条结果的页码或来源字段
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install langchain_community
from langchain_community.document_loaders import PyPDFLoader

# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = PyPDFLoader(
    # 文件路径，支持本地文件和在线文件链接，如"https://arxiv.org/pdf/alg-geom/9202012"
    file_path="assets/sample.pdf",
    # 提取模式:
    #   plain 提取文本
    #   layout 按布局提取
    extraction_mode="plain",
).load()

print(docs)
