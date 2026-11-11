# ============================================================================
# 学习目的：理解 invoke 与 stream 的返回形式区别
# 技术讲解：invoke 给完整消息；stream 给可逐项消费的消息分片
# 阅读路线：创建客户端 → 普通调用 → 使用 HumanMessage 流式调用
# 当前代码要注意：文件名是 Ollama，但当前 base_url 指向 DeepSeek；这里没有连接本机 Ollama
# 动手验证：对照实际 base_url 判断请求去了哪里
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

#pip install langchain-community
#pip install dashscope
# 如果报错，强制重装 cffi（解决模块损坏、缓存残留问题，优先推荐）
# pip install --upgrade --force-reinstall cffi

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
chatLLM = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com",
    streaming=True,
    # other params...
)
# 打印结果
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(chatLLM.invoke("你是谁"))

print("*" * 60)

# 【理解这一行】返回分片迭代对象，需继续遍历才能读出输出；每块不是整段回答。
res = chatLLM.stream([HumanMessage(content="你好，你是谁")], streaming=True)
for r in res:
    print("chat resp:", r.content)
