"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    1、如何理解异常对象的传递
"""
# def a():
#     print("a函数开始调用")
#     b() #等价于这句代码也发生异常，导致a函数调用异常结束，并且会把这个异常对象传递给调用者
#     print("a函数调用结束")
#
# def b():
#     print("c函数开始调用")
#     c() #等价于这句代码也发生异常，导致b函数调用异常结束，并且会把这个异常对象传递给调用者
#     print("c函数调用结束")
#
# def c():
#     print("c函数开始调用")
#     raise Exception("这是一个异常对象") #会导致c函数调用异常结束，并且会把这个异常对象传递给调用者
#     print("c函数调用结束")
#
# a() #等价于这句代码也发生异常，导致主函数调用异常结束，并且会把这个异常对象传递给调用者（python解释器），程序就挂了

# def a():
#     print("a函数开始调用1")
#     b()
#     print("a函数调用结束2")
#
# def b():
#     print("c函数开始调用3")
#     c()
#     print("c函数调用结束4")
#
# def c():
#     try:
#         print("c函数开始调用5")
#         raise Exception("这是一个异常对象6")
#         print("c函数调用结束7")
#     except Exception as e:
#         print(e)
#     #如果这里处理了异常，那么调用者对发生异常是无感的。因为此时c()不会把异常对象传递给b()
#
# a()

def a():
    print("a函数开始调用1")
    b()
    print("a函数调用结束2")

def b():
    try:
        print("c函数开始调用3")
        c()
        print("c函数调用结束4")
    except Exception as e:
        print(e)

def c():
    print("c函数开始调用5")
    raise Exception("这是一个异常对象6")
    print("c函数调用结束7")


a()
