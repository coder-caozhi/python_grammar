# ============================================================================
# 学习目的：把模型选工具、工具执行、结果转述组合成链
# 技术讲解：bind_tools 只声明工具；解析 tool_calls 后，管道里的 get_weather 才真正执行
# 阅读路线：用户问题 → 模型生成工具参数 → 解析 → 天气工具 → 第二次模型转述
# 当前代码要注意：模型未选择该工具时解析可能得不到参数；导入 query_weather_tool 还会先执行它的顶层测试调用
# 动手验证：沿链记录每一段收到的是消息、参数字典还是天气字符串
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import os
from dotenv import load_dotenv

# 【理解这一行】把 .env 配置加载到进程环境；不传路径时要注意调试/交互运行的搜索起点。
load_dotenv()
from langchain_core.output_parsers import JsonOutputKeyToolsParser, StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from loguru import logger
from query_weather_tool import get_weather

# 初始化大语言模型实例
# 【理解这一行】创建 OpenAI 兼容聊天客户端：model 是远端模型，base_url 才决定请求服务地址。
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

# 将模型与工具绑定，使其能够调用 get_weather 工具
# 【理解这一行】把工具名称、描述和参数 schema 提供给模型；绑定本身不会执行工具函数。
llm_with_tools = llm.bind_tools([get_weather])

# 创建解析器，用于提取工具调用结果中的 JSON 数据
parser = JsonOutputKeyToolsParser(key_name=get_weather.name, first_tool_only=True)

# 构建工具调用链：模型 -> 解析器 -> 调用天气工具
# 【理解这一行】模型只提出调用与参数；parser 取出参数后，末尾工具节点才执行真实 HTTP 查询。
get_weather_chain = llm_with_tools | parser | get_weather
# print(get_weather_chain.invoke("你好， 请问北京的天气怎么样？"))
# 定义输出提示模板，将 JSON 天气数据转换为自然语言描述
# 【理解这一行】从花括号占位符推断所需变量；得到的仍是模板，而不是模型回答。
output_prompt = PromptTemplate.from_template(
    """你将收到一段 JSON 格式的天气数据{weather_json}，请用简洁自然的方式将其转述给用户。
    以下是天气 JSON 数据：
    请将其转换为中文天气描述，例如：
    “北京现在天气：多云，气温 28℃，体感有点闷热（约 32℃），湿度 75%，微风（东南风 2 米/秒），
    能见度很好，大约 10 公里。建议穿短袖短裤。适合做户外运动。"
    """
)

# 创建字符串输出解析器
# 【理解这一行】把支持的文本/消息输出变成文本，方便下一步传递；消息元数据不会作为正文保留。
output_parser = StrOutputParser()

# 构建最终输出链：提示模板 -> 模型 -> 输出解析器
output_chain = output_prompt | llm | output_parser

# 构建完整的处理链：天气查询链 ->将天气数据包装为字典格式 -> 输出链
# 【理解这一行】把天气 JSON 字符串包装成 weather_json 字典，匹配第二个提示词模板。
full_chain = get_weather_chain | (lambda x: {"weather_json": x}) | output_chain

# 执行完整链路，查询上海天气并打印结果
# 【理解这一行】从入口运行整条链；沿每一段核对上一步输出能否满足下一步输入。
result = full_chain.invoke("请问北京今天的天气如何？")
logger.info(result)

