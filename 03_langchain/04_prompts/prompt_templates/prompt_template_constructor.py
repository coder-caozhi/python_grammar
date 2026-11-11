# ============================================================================
# 学习目的：显式声明模板字符串与变量集合
# 技术讲解：input_variables 描述格式化时需要的键，format 生成字符串
# 阅读路线：构造 role/question 模板 → 填值 → 模型调用 → 产品模板复用
# 当前代码要注意：本文件前半段会访问模型，后半段产品模板只是本地格式化
# 动手验证：列出两个模板各自需要哪些键
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain.chat_models import init_chat_model
# 方式1：使用构造方法实例化提示词模板
from langchain_core.prompts import PromptTemplate

# 创建一个PromptTemplate对象，用于生成格式化的提示词模板
# 该模板包含两个变量：role（角色）和question（问题）
# 【理解这一行】构造字符串模板；先区分模板对象与 format/invoke 之后得到的提示词。
template = PromptTemplate(
    template="你是一个专业的{role}工程师，请回答我的问题给出回答，我的问题是：{question}",
    input_variables=['role', 'question']
)

# 使用模板格式化具体的提示词内容
# 将role替换为"python开发"，question替换为"冒泡排序怎么写？"
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
prompt = template.format(role="python开发",question="冒泡排序怎么写,只要代码其它不要，简洁")

# 输出格式化后的提示词内容
print(prompt)# 你是一个专业的python开发工程师，请回答我的问题给出回答，我的问题是：冒泡排序怎么写,只要代码其它不要，简洁



# 【理解这一行】统一初始化入口：provider 选择适配器，model/base_url 指定实际模型与服务端。
model = init_chat_model(
    model="deepseek-chat",
    model_provider="openai",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
# 【理解这一行】同步调用模型并等待完整消息；本例使用 content 取正文，也可观察响应元数据。
result = model.invoke(prompt)
print(result.content)
print("\n\n")



# 使用构造方法实例化提示词模板
template = PromptTemplate(
    template="请评价{product}的优缺点，包括{aspect1}和{aspect2}。",
    input_variables=["product", "aspect1", "aspect2"],
)

# 使用模板生成提示词带有关键字参数的用法
prompt_1 = template.format(product="智能手机", aspect1="电池续航", aspect2="拍照质量")
prompt_2 = template.format(product="笔记本电脑", aspect1="处理速度", aspect2="便携性")

print(prompt_1)  # 请评价智能手机的优缺点，包括电池续航和拍照质量。
print(prompt_2)  # 请评价笔记本电脑的优缺点，包括处理速度和便携性。
