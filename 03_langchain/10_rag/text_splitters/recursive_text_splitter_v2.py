# ============================================================================
# 学习目的：观察分块重叠和手工重建文本的假设
# 技术讲解：把每段文本包装为 Document，再尝试去除重复部分拼接
# 阅读路线：split_text → 包装文档 → text[30:] 去重 → 与原文比较
# 当前代码要注意：固定裁掉 30 个字符只在实际重叠恰为 30 时成立，不是通用还原算法
# 动手验证：换成包含段落分隔符的文本，检查还原比较是否仍成立
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document

# 原始文本内容
content = (
    "大模型RAG（检索增强生成）是一种结合生成模型与外部知识检索的技术，通过从大规模文档或数据库中检索相关信息，"
    "辅助生成模型以提升回答的准确性和相关性。其核心流程包括用户输入查询、系统检索相关知识、"
    "生成模型基于检索结果生成内容，并输出最终答案。RAG的优势在于能够弥补生成模型的知识盲区，"
    "提供更准确、实时和可解释的输出，广泛应用于问答系统、内容生成、客服、教育和企业领域。"
    "然而，其也面临依赖高质量知识库、可能的响应延迟、较高的维护成本以及数据隐私等挑战。")

# 定义递归文本分割器
# 【理解这一行】chunk_size 是目标块大小，overlap 保留上下文重叠；本例 len 统计字符，不是 token。
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=30,
    length_function=len
)

# 核心：先调用split_text分割为字符串列表
# 【理解这一行】输入一个字符串，返回多个字符串片段；这里还没有 Document 包装。
splitter_texts = text_splitter.split_text(content)
# 手动转换为Document对象，保证内容完整
# 【理解这一行】正文放 page_content，来源等附加信息放 metadata；两者用途不同。
splitter_documents = [Document(page_content=text) for text in splitter_texts]

# 拼接所有分割后的内容（剔除重叠部分）验证完整性
full_content = ""
for text in splitter_texts:
    if full_content:
        # 【理解这一行】固定去掉 30 字符是假设，不保证递归分隔后的每对块实际重叠都是 30。
        full_content += text[30:]  # 剔除重叠的30个字符后拼接
    else:
        # 【理解这一行】固定去掉 30 字符是假设，不保证递归分隔后的每对块实际重叠都是 30。
        full_content += text

# 打印验证结果
print(f"原始文本大小：{len(content)}，原始内容：\n{content}\n")
print(f"分割文档数量：{len(splitter_documents)}\n")
for idx, splitter_document in enumerate(splitter_documents, 1):
    print(f"第{idx}个文档 - 大小：{len(splitter_document.page_content)}, 内容：{splitter_document.page_content}\n")

# 最终完整性验证
print(f"拼接后文本大小：{len(full_content)}")
print(f"是否与原始文本完全一致：{full_content == content}")
print(f"拼接后完整内容：\n{full_content}")
