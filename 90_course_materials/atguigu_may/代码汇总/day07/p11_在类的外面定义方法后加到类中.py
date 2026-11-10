"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    了解：把在类外面定义的一个函数，直接赋值给类的方法名，可以避免重复定义。
"""

def show(): #没有固定的参数，而且它的定义不在类中，所以，可以不加@staticmethod
    print("我是一个人")

class Person:
    say_hello = show #把show函数当做对象赋值给say_hello这个方法名

Person.say_hello()