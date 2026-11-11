# ============================================================================
# 学习目的：理解消息对象和流式响应的配合
# 技术讲解：HumanMessage 表示用户消息；分片内容需要在循环中消费
# 阅读路线：构造客户端 → invoke → stream → chunk.content
# 当前代码要注意：文件名是 Qwen，但现有配置使用 DeepSeek；不能将此文件当作通义千问接入证据
# 动手验证：找出决定供应商地址和模型名称的两行参数
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

#pip install langchain-community
#pip install dashscope

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
    streaming=True,
    base_url="https://api.deepseek.com",
    # other params...
)
# 打印结果
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
print(chatLLM.invoke("你是谁"))

print("*" * 60)

# 【理解这一行】返回分片迭代对象，需继续遍历才能读出输出；每块不是整段回答。
res = chatLLM.stream([HumanMessage(content="你好，你是谁")])
for r in res:
    print("chat resp:", r.content)
