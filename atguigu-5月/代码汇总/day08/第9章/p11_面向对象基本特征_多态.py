"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
import math

"""
    1、什么是多态？多态的好处是什么？
    多态：字面意思，多种形态
    在代码层面：一个方法在不同类中的多种实现方式。
    
    多态的好处：python解释器会根据当前对象的类型，来动态的绑定具体的方法实现。
    
    2、如何实现多态？
    
    在python中有2种实现形式：遵循方法的动态绑定机制
    （1）基于继承 + 方法重写：这个实现方式与Java等其他语言一样。只要是某个父类及其子类的对象，就一定有对应的方法。父子类关系耦合度太高。优点：稳定、靠谱。
    （2）鸭子类型的原则：没有继承，只是不同的类之间有同名的方法。很灵活，但是有可能这个对象没有对应的方法，就会报错。
"""
# class Animal:
#     def eat(self):
#         print("吃~~~")
#
# class Dog(Animal):
#     def eat(self):
#         print("吃shi")
#
# class Cat(Animal):
#     def eat(self):
#         print("吃🐭")
#
# def look(animal): #参数类型是不确定，可以接收任意类型的对象
#     #判断animal接收的对象是Animal这个家族，这个系列
#     if isinstance(animal, Animal): #当animal接收的对象是Animal本身类型或者它子类的类型，这个条件都成立
#         print(type(animal))
#         animal.eat() #需要在运行时，根据animal对象的实际的类型，来动态的绑定具体的方法实现
#
# look(Dog())
# look(Cat())


class Dog:
    def eat(self):
        print("吃shi")

class Cat:
    def eat(self):
        print("吃🐭")

class Other:
    def eat(self):
        print("eat...")

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    def area(self):
        p = (self.a * self.b * self.c)/2
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))

def look(animal):
    animal.eat()

look(Triangle(3,4,5))
look(Dog())
look(Cat())
look(Other())
