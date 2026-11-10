"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、什么是异常和错误？
    在python中异常和错误也是用对象表示。
    可以分为（1）语法错误：SyntaxError：停下来修正语法即可
         （2）其他的异常：
            一种情况，可以通过条件判断避免
            另一种情况，无法避免（网络中断，磁盘空间不足，权限不够等）
            使用try-except结构来处理
            
    2、如果不处理，任意异常和错误都会导致程序崩溃
"""
# print('hello) #故意缺省'

#从控制台输入2个整数，然后求它们的商
a_str = input("请输入被除数的整数：")
b_str = input("请输入除数的整数：")
if a_str.isdigit() and b_str.isdigit():
    a = int(a_str)
    b = int(b_str)
    if b:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("除数不能为0")
else:
    print("被除数和除数必须是整数")
