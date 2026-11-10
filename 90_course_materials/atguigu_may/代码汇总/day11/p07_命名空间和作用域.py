"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、不同范围的标识符（包括变量、函数、类等名称），会在各自的命名空间对应的字典中记录，能找到就可以使用，找不到就会报NameError错误。
    命名空间分为3层：如果你现在是在函数中
    （1）函数的局部命名空间
    （2）找模块命名空间
    （3）内置的命名空间
"""
# a = 1
# b = 3
# def func():
#     b = 2
#     max = 4 #优先于内置函数max
#     print(f"{b = }")
#     print(f"{a = }")
#     nums = [1,2,3]
#     # print(max(nums)) #错误
#
# func()

"""
    2、作用域
    python中有四个作用域：
    （1）内层函数的局部位置（Local）
    （2）外层函数的局部位置（Enclosing）
    （3）模块全局位置（Global）
    （4）内置的全局位置（Built-in）
    
    内层可以使用外层，外层不能使用内层。
"""
x = 1  # 全局变量

def outer():
    # 在函数中定义变量，会开启新的变量作用域

    # E (Enclosing): 闭包，因为y被内部函数inner使用，且inner被返回到outer之外，所以y被保存在闭包中
    y = 2  # 外层函数变量，在整个outer函数中都可以访问

    # 在外部函数体中定义内部函数
    def inner():
        # 在函数中定义变量，会开启新的变量作用域
        # L (Local): 函数内部变量
        z = 3  # 局部变量，仅限于inner函数内部访问
        print(f"在inner中访问局部变量z的值是：{z}")  # 访问局部变量
        print(f"在inner中访问嵌套变量y的值是：{y}")  # 访问外层函数变量
        print(f"在inner中访问全局变量x的值是：{x}")  # 访问全局变量
        print(f"在inner中访问内建函数print")  # 访问内建函数

    # print(f"在outer中访问内层函数变量z的值是：{z}") # 报错
    print(f"在outer中访问局部变量y的值是：{y}")
    print(f"在outer中访问全局变量x的值是：{x}")
    print(f"在outer中访问内建函数print")

    return inner

func = outer()
print("*"*20)
func()