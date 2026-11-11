# ============================================================================
# 学习目的：用显式 Pydantic 模型定义工具参数结构
# 技术讲解：args_schema 描述参数；Field.description 帮助模型理解每个参数的用途
# 阅读路线：定义 FieldInfo → 装饰加法函数 → 检查元信息 → invoke
# 当前代码要注意：当前 add_number 没有 docstring，也没显式 description；部分版本会在装饰时拒绝创建工具，args_schema 不替代工具描述
# 动手验证：观察需要给工具补充哪类说明才能让模型知道何时使用它
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

from langchain.tools import tool

'''
使用@tool装饰器
装饰器默认使用函数名称作为工具名称，但可以通过参数name_or_callable 来覆盖此设置。
同时，装饰器将使用函数的文档字符串作为工具的描述，因此函数必须提供文档字符串
'''

'''
需求：
定义了一个名为add_number的工具函数，用于执行两个整数相加操作。主要功能包括：

使用Pydantic定义参数模型FieldInfo，指定两个整数参数a和b
通过@tool装饰器将函数注册为LangChain工具，绑定参数schema
打印工具的元信息（名称、参数、描述等）并调用工具执行加法运算并输出结果
'''
from langchain_core.tools import tool
from loguru import logger
from pydantic import BaseModel, Field

# 使用Pydantic定义参数模型FieldInfo，指定两个整数参数a和b
'''
public class FieldInfo {
    private final int a;//第1个参数
    private final int b;//第2个参数
    public FieldInfo(int a, int b) {
        this.a = a;
        this.b = b;
    }
    //=====getter=====
}
'''


class FieldInfo(BaseModel):
    """
    定义加法运算所需的参数信息
    """
    a: int = Field(description="第1个参数")
    b: int = Field(description="第2个参数")


# 通过args_schema定义参数信息，也可以定义name、description、return_direct参数
@tool(args_schema=FieldInfo)
# 【理解这一行】本函数缺少 docstring/显式 description：当前环境 @tool 会在注册阶段报错，不是加法计算出错。
def add_number(a: int, b: int) -> int:
    return a + b


# 打印工具的基本信息
logger.info(f"name = {add_number.name}")
logger.info(f"args = {add_number.args}")
logger.info(f"description = {add_number.description}")
logger.info(f"return_direct = {add_number.return_direct}")

# 调用工具执行加法运算
# 【理解这一行】直接执行工具：传入符合 schema 的参数，返回 Python 函数的计算/查询结果。
res = add_number.invoke({"a": 1, "b": 2})
logger.info(res)

