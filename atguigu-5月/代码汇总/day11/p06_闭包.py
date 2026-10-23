"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、python中的函数可以嵌套定义，这就会产生一个问题：
    (1)内层函数会使用外层函数的局部变量
    (2)内层函数会被返回到外层函数的外面使用
    
    2、函数调用有2个动作
    （1）入栈：函数被调用时，会在栈内存开辟一块独立的内存空间，用于存储该函数的局部变量和操作数栈等信息。
    （2）出栈：函数调用结束，会自动回收该函数占用的栈内存空间。
    
    3、函数的原则：先定义后使用，不调用不执行，调用一次执行一次。
    
    4、什么是闭包？
    构建闭包的条件：
        - 外部函数内定义一个内部函数。
        - 内部函数用到外部函数中的变量。
        - 外部函数将内部函数作为返回值返回到外部函数外面使用。

    5、面试题：闭包函数与普通函数有什么区别？答：闭包构成的条件
    闭包函数的__closure__属性不是None，普通函数的__closure__属性为None。

"""
def outer():
    a = 1
    b = 2

    def inner(): #不调用不执行
        # print("外层函数的局部变量a = ", a)
        # print("外层函数的局部变量b = ", b)
        print("hello")

    return inner #返回内层函数对象inner

if __name__ == "__main__":
    func = outer() #得到是一个函数对象，是outer中的函数对象inner
    print(func.__closure__)

    # print(func.__closure__[0].cell_contents)
    # print(func.__closure__[1].cell_contents)

    # print(func)
    # func() #调用func函数，等价于调用 inner()