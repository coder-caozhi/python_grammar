"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    dir()函数是用于列出某个模块、某个函数、某个对象的成员列表
"""
a = 1
b = 2
# print(dir()) #列出当前模块的成员

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self):
        print(f"{self.name} eats {self.age} times.")

# p = Person("张三",23)
# print(dir(p))

def add(x,y): #x,y是局部变量，不属于函数对象的成员
    return x+y

print(dir(add))

# print(add.x) #不能在add函数之外使用x局部变量，所以x不是成员