"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']

    1、with是什么作用
    with是用于自动关闭资源对象，简化资源对象的使用的代码。
    资源对象：IO对象，数据库连接对象，网络连接对象，线程池对象，进程池对象......
    
    2、语法结构
    with 资源对象的创建 as 资源对象的别名:
        资源对象的使用代码
    
    凡是在with后面创建的资源对象，在使用后都会自动关闭，无论其是否发生异常。
    通常需要配合try结构使用，但是不是必须。
"""
# from keyword import kwlist
# print(kwlist)

#从hello.txt文件中读取内容
#不使用with
# fr = open("hello.txt","r",encoding="utf-8")
# data = fr.read()
# print(data)
# fr.close()
#上面的代码，如果发生异常，关闭是没有进行的
# from io import UnsupportedOperation
# fr = None
# try:
#     fr = open("hello.txt","w",encoding="utf-8")
#     data = fr.read()
#     print(data)
# except FileNotFoundError:
#     print("文件不存在")
# except PermissionError:
#     print("没有权限读取文件")
# except UnsupportedOperation:
#     print("读写操作错误")
# finally:
#     if fr:
#         fr.close()
#         print("fr正确关闭了吗？", fr.closed)
#     else:
#         print("fr都未正确创建")

#使用with
# from io import UnsupportedOperation
# fr = None
# try:
#     # with open("hello.txt","w",encoding="utf-8") as fr:
#     with open("hello.txt","r",encoding="utf-8") as fr:
#         data = fr.read()
#         print(data)
# except FileNotFoundError:
#     print("文件不存在")
# except PermissionError:
#     print("没有权限读取文件")
# except UnsupportedOperation:
#     print("读写操作错误")
# finally:
#     if fr:
#         # fr.close() #不需要手动close()
#         print("fr正确关闭了吗？", fr.closed)
#     else:
#         print("fr都未正确创建")


#最终版简化代码
try:
    with open("hello.txt","r",encoding="utf-8") as fr:
        data = fr.read()
        print(data)
except FileNotFoundError:
    print("文件不存在")
except PermissionError:
    print("没有权限读取文件")
except UnsupportedOperation:
    print("读写操作错误")

