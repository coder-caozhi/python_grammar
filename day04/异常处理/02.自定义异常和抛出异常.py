# 自定义一个异常类
class LoginError(Exception):
    pass
try:
    # 手动抛出异常
    # raise ZeroDivisionError("出现了除0的异常")
    raise LoginError("出现了自定义异常")
except Exception as e:
    print(f"出现了异常，异常信息是：{e}")
finally:
    print("程序执行结束")