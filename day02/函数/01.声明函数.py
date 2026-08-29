# 定义一个无参的函数、
def fun():
    """
    这是一个没有参数和返回值的函数
    :return: 没有返回值
    """
    print("hello function")

# 调用函数
fun()
# 函数也是对象，可以将函数赋值给变量
my_var = fun
my_var()
# 获取函数的文档说明
print(help(fun))
print(fun.__doc__)
# 如何函数没有返回值则获取的是None
print(fun())

# 定义有参和返回值的函数
def add(a, b):
    """
    这是一个求和的函数
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 返回a和b的和
    """
    return a + b
result = add(10, 2)
print(result)

# 声明一个带注释的函数
def my_fun(name:"这是姓名",age:"范围是0-116",gender:int)->"返回值是字典":
    return {"姓名":name,"年龄":age,"性别":gender}

# 获取函数的注释
print(my_fun.__annotations__)
# 调用函数
print(my_fun("蔡徐坤",27,1))
