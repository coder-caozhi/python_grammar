# ============================================================================
# 学习目的：用 YAML 保存可复用的提示词模板
# 技术讲解：加载得到的是模板对象，填入变量后才得到最终字符串
# 阅读路线：过滤指定警告 → 读取 YAML → format
# 当前代码要注意：过滤警告不会修复依赖兼容问题；工作目录要能找到 prompt.yaml
# 动手验证：对比 JSON 版本的配置字段与最终结果
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

import warnings
warnings.filterwarnings("ignore",
                        message="Core Pydantic V1 functionality isn't compatible with Python 3.14")

# 方式2：外部加载Prompt,将 prompt 保存为 yaml
from langchain_core.prompts import load_prompt

# 【理解这一行】从文件加载提示词配置；相对路径以当前工作目录为基准。
template = load_prompt("prompt.yaml", encoding="utf-8")
# 【理解这一行】用关键字参数填充模板变量，结果是字符串；变量名必须对应模板中的占位符。
print(template.format(name="年轻人", what="滑稽"))
# 请年轻人讲一个滑稽的故事


