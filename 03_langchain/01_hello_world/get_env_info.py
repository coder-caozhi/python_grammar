# ============================================================================
# 学习目的：定位当前 Python 实际导入的 LangChain 版本和安装位置
# 技术讲解：__version__ 看发行版本；__file__ 看模块来源；sys.version 看解释器版本
# 阅读路线：先看两个库的版本，再对照模块路径与 PyCharm 解释器
# 当前代码要注意：安装包所在环境与编辑器选用环境可能不同；本文件不发起模型请求
# 动手验证：切换两套解释器运行，比较版本和路径
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import langchain
import langchain_community
import sys

# 【理解这一行】__version__ 看发行版本；__file__ 看模块来源；sys.version 看解释器版本
print("langchainVersion:  "+langchain.__version__)
print("langchain_communityVersion:  "+langchain_community.__version__)
print("langchainfile:"+langchain.__file__)

print(sys.version)

