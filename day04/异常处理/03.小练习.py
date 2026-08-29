# 模拟一个登录的操作，假设用户名是admin，密码是123456
class LoginError(Exception):

    # 初始化函数
    def __init__(self, code, message):
        self.code = code
        self.message = message

    # toString
    def __str__(self):
        return f"LoginError(code={self.code}, message={self.message})"

# 定义一个登录的函数
def login(username, password):
    try:
        # 判断用户名是存在
        if "admin" != username:
            # 抛出异常
            raise LoginError(6001,"用户不存在")

        # 判断密码是否正确
        if "123456" != password:
            # 抛出异常
            raise LoginError(6002,"密码不正确")
    except LoginError as e:
        print(f"登录失败：{e}")
    else:
        print("登录成功")
    finally:
        print("登录流程结束，释放连接")


# 调用函数
# 用户不存在
# login("wangfeilong","123456")
# 密码错误
# login("admin","111111")
# 登录成功
login("admin","123456")

