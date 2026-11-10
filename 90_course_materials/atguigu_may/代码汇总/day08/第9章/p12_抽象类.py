"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、什么是抽象类？
    （1）抽象类本身不能直接实例化，即不能直接创建对象，它存在的意义是用来被子类继承的。
    （2）抽象类可以包含抽象方法。抽象方法是指没有具体方法体的方法。
    
    2、如何定义抽象类？
    （1）继承abc.ABC： abc代表abstract class
    （2）抽象方法上面需要加一个装饰器 @abc.abstractmethod
    
    3、子类继承抽象类之后，必须重写它的所有抽象方法。之后创建子类对象，调用方法即可。
"""
import abc
class Person(abc.ABC):
    @abc.abstractmethod
    def eat(self):
        pass

    def drink(self):
        print("喝水")

class Student(Person):
    def eat(self):
        print("吃学生餐")

# p = Person()
# p.eat()

s = Student()
s.eat()
s.drink()