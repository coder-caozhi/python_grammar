"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    1、python中函数的特点：
        python是一切皆对象，在python中定义了一个函数，也相当于有一个函数对象诞生了。
        只要是对象就有类型，函数是function类型。
    
    2、如何理解函数是对象，或函数是数据类型
    （1）函数对象可以被赋值给一个变量
    （2）函数对象可以被作为返回值返回
    （3）函数对象也可以被当成参数传递
    
    3、python中这种特性被称为 面向函数编程，函数是一等公民，即遵循函数编程的范式。
"""
# p = print #右边print是一个函数，函数对象print被赋值给了p变量，相当于p变量也是一个函数
# p("hello") #调用p函数，实现print函数的功能

#定义一个函数
# def get_function(operator):
#     #在python中还可以出现函数的嵌套定义
#     def add(x,y):
#         return x + y
#     def sub(x,y):
#         return x - y
#     def mul(x,y):
#         return x * y
#     match operator:
#         case "+":
#             return add   #求和的函数
#         case "-":
#             return sub   #求差的函数
#         case "*":
#             return mul   #求乘积的函数
#         case _:
#             return None
#
# fun = get_function("+") # fun变量得到一个函数，这里得到的是add函数
# print(fun(5, 6))
#
# fun = get_function("*")
# print(fun(5, 6))

# #定义一个函数
# def calculate(func, x,y): #func是一个参数，准备用来接收一个函数，该函数可以接收2个值进行计算
#     return func(x,y)
#
# def add(x,y):
#     return x + y
# def sub(x,y):
#     return x - y
# def mul(x,y):
#     return x * y
#
# # print(calculate(add,5,6)) #把add函数传给func参数，即func参数等价于add函数
# # print(calculate(sub,5,6)) #把sub函数传给func参数，即func参数等价于sub函数
#
# # print(calculate(add(),5,6)) # add()表示调用add函数，add函数调用时需要2个参数值，这里缺参数值，报错、

"""
    函数对象也可以被作为容器中的元素
"""

def add(x,y):
    return x + y
def sub(x,y):
    return x - y
def mul(x,y):
    return x * y
funcs = [add,sub,mul]
for func in funcs:
    print(func(5,6))