# ============================================================================
# 学习目的：把 JSON 数据按 jq 表达式提取为文档
# 技术讲解：jq_schema='.' 选择整个对象；text_content=False 允许非字符串内容序列化
# 阅读路线：读取 JSON → jq 选取 → 转 Document
# 当前代码要注意：False 不表示跳过正文，而是允许所选值不是原始字符串；可能需要 jq 依赖
# 动手验证：修改 jq 选择字段前，先查看 sample.json 结构
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install jq
from langchain_community.document_loaders import JSONLoader

# 提取所有字段
# 【理解这一行】读取素材并返回 Document 列表；检查 page_content 与 metadata 的职责。
docs = JSONLoader(
    file_path="assets/sample.json",  # 文件路径
    jq_schema=".",  # 提取所有字段
    text_content=False,  # 提取内容是否为字符串格式
).load()

print(docs)
