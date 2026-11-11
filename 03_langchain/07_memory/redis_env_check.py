# ============================================================================
# 学习目的：检查 Python Redis 客户端包能否导入
# 技术讲解：包能导入与 Redis 服务可连接是两回事
# 阅读路线：查看版本 → try 内再次 import → 输出信息
# 当前代码要注意：文件最前面已 import redis，缺包时会先在那里失败；本文件没有执行 ping 或连接测试
# 动手验证：指出要检查服务连通性还缺哪一步
# 阅读建议：在下方关键语句打断点，观察参数、返回类型和下一步接收的数据。
# ============================================================================

# pip install redis==5.3.1

# 尝试导入 redis 包
import redis

# 验证包版本（无报错即为导入成功）
# 【理解这一行】包能导入与 Redis 服务可连接是两回事
print(redis.__version__)

# 极简 redis 导入测试脚本
try:
    # 导入 redis 包
    import redis
    print("✅ redis 包导入成功！")
    print(f"✅ redis 包版本：{redis.__version__}")
except ModuleNotFoundError:
    print("❌ 未找到 redis 包，请先安装！")
except Exception as e:
    print(f"❌ redis 包导入异常：{e}")

"""
5.3.1
✅ redis 包导入成功！
✅ redis 包版本：5.3.1
"""