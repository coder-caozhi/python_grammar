"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    1、什么是匿名函数？
    没有名字的函数。
    
    有名字的函数的语法格式：
    def 函数名(形参列表)：
        函数体语句
        
    匿名的函数的语法格式：
    lambda 形参列表 : 函数体语句
    
    通常情况下，匿名函数的函数体不会太复杂，通常都是只有一个表达式。
   
"""
# add = lambda x, y: x + y  #右边是一个匿名函数，左边是一个变量
# print(add(1, 2))

# def calculate(func,x,y): #func是一个参数
#     return func(x,y)
#
# print(calculate(lambda x, y: x + y,1,2)) #lambda x, y: x + y一个匿名函数，作为实参给func赋值


# #定义一个函数
# def get_function(operator):
#     match operator:
#         case "+":
#             return lambda a,b :a + b #求和的函数
#         case "-":
#             return lambda a,b :a - b    #求差的函数
#         case "*":
#             return lambda a,b :a * b    #求乘积的函数
#         case _:
#             return None
#
# f1 = get_function("+")
# print(f1(1,2))
#
# print(get_function("-")(8,6)) #get_function("-")得到一个函数，得到 lambda a,b :a - b，
#                                     #(8,6)，调用匿名函数，把8和6赋值给a,b，求a-b


funcs = [lambda a,b :a + b, lambda a,b :a - b, lambda a,b :a * b]
for func in funcs:
    print(func(5,6))

