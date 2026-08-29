# 声明函数
def get_info(name, age):
    print(f"您的姓名是：{name}，您今年{age}岁了")

# 位置参数：实参的个数与位置必须与形参一致
get_info("吴亦凡",35)
get_info(27,"蔡徐坤")

# 关键字参数
get_info(age=24, name="王飞龙")

# 默认参数：默认参数可传可不传，传了使用传入的值，不传则使用默认值
def get_user(name, age, gender="男"):
    print(f"您的姓名是：{name}，您的年龄是：{age}，您的性别是：{gender}")

# 调用函数
get_user("刘备",30)
get_user("孙尚香",16,"女")

"""
    可变参数
        *args：多个参数将封装成一个元组，可以不放最后，如果后面有普通参数必须使用关键字传参
        **kwargs：多个参数将封装成一个字典，必须放最后
"""
def fun(a, *args):
    print(f"第一个参数是：{a}")
    print(f"剩下的参数是：{args}")

def fun1(a, *args, b):
    print(f"第一个参数是：{a}")
    print(f"剩下的参数是：{args}")
    print(f"可变参数后面的参数值是：{b}")

# 调用函数
fun(1,2,3,4,5)
fun1(1,2,3,4,5,b=6)

def fun2(a,**kwargs):
    print(f"第一个参数是：{a}")
    print(f"剩下的参数是：{kwargs}")

# 调用函数
fun2(1,name="赵云",role="五虎上将")

# **kwargs后面不能有参数，必须放在最后
# def fun3(a,**kwargs,b):


