# 基本语法

# 只处理一种异常
try:
    # 会出除0的异常
    # num = 10 / 0
    print("执行try中的代码")
except ZeroDivisionError as e:
    print(f"出现了异常，异常信息是：{e}")
else:
    print("不出现异常时才会执行的代码")
finally:
    print("不管程序是否出现异常都要执行的代码")

# 同时处理多种异常
try:
    # 会出除0的异常
    # num = 10 / 0
    # 出现一个其他异常
    # print(num)
    # 数字与字符串相加
    str = 5 + "hello"
    print(str)
    print("执行try中的代码")
except (ZeroDivisionError,NameError) as e:
    print(f"出现了异常，异常信息是：{e}")
except TypeError as e:
    print(f"出现了类型异常，异常信息是：{e}")
except Exception as e:
    # 兜底处理
    print(f"出现了其他异常，异常信息是：{e}")
else:
    print("不出现异常时才会执行的代码")
finally:
    print("不管程序是否出现异常都要执行的代码")