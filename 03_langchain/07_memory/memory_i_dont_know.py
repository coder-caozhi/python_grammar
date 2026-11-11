# ============================================================================
# 学习目的：用反例理解无状态聊天请求
# 技术讲解：同一客户端实例不代表每次请求自动附带上轮聊天内容
# 阅读路线：第一次自我介绍 → 第二次询问姓名 → 检查实际发送的提示词
# 当前代码要注意：第二次没有提供历史，所以回答不能可靠依赖第一轮；旧 Qwen 输出只是历史示例
# 动手验证：对比两次 chain.invoke 各自的 question
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================


from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
# 设置本地模型
# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
llm = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    temperature=0.0,
    base_url="https://api.deepseek.com"
)

# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
prompt = PromptTemplate.from_template(
    "请回答我的问题：{question}"
)
# 创建字符串输出解析器
# 【理解这一行】把支持的文本/消息输出变成文本，方便下一步传递；消息元数据不会作为正文保留。
parser = StrOutputParser()

# 构建链式调用
chain = prompt | llm | parser

# 执行链式调用
# 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
print(chain.invoke({"question": "我叫张三，你叫什么?"}))

print(chain.invoke({"question": "你知道我是谁吗?"}))

"""
你好，张三！我叫通义千问（Qwen），是阿里云研发的超大规模语言模型。很高兴认识你！😊
我不知道你是谁。我是一个AI助手，没有能力识别或获取用户的身份信息。如果你有任何问题需要帮助，我会很乐意为你提供支持！

解释：
我们刚刚在本地程序，前一轮对话告诉大语言模型的信息，下一轮就被“遗忘了”。
但如果我们使用使用 Qwen 聊天时，它能记住多轮对话中的内容，这Qwen网页版实现了历史记忆功能
"""