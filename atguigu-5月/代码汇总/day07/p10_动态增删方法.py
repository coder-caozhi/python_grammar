"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    2、动态增删方法（了解）
    （1）静态方法
        动态增加静态方法：类名.新静态方法名 = 函数名
        动态删除静态方法：del 类名.静态方法
    （2）类方法
        动态增加类方法：类名.新类方法名 = 函数名 （要求在类外面定义的函数上面必须加@classmethod）
        动态删除类方法：del 类名.类方法
    （3）实例方法
        动态增加实例方法：
            A：实例对象名.新实例方法名 = types.MethodType(函数名,实例对象名)  OK，只给一个对象增加实例方法
            B：类名.新实例方法名 = types.MethodType(函数名,实例对象名)  语法对，逻辑是错误的
            C：类名.新实例方法名 = 函数名       OK，给这个类的所有对象增加实例方法
            
        动态删除类方法：
            A：del 类名.实例方法(所有对象的该实例方法都被删除了)
            B：del 对象.实例方法（只删除一个对象的实例方法，
              它仅限于 用 “实例对象名.新实例方法名 = types.MethodType(函数名,实例对象名)“方式增加的实例方法才可以这么做
"""
import types

# class Person:
#     pass
#
# def show(): #没有固定的参数，而且它的定义不在类中，所以，可以不加@staticmethod
#     print("我是一个人")
#
# @classmethod
# def show_home(cls):#类方法必须加@classmethod，无论它在不在类中，因为加@classmethod,python解释器才会帮我们把类的引用（地址）传给cls
#     print("我住在：",cls.home)
#
# def eat(self,food):
#     print(f"{self.name}在吃{food}")
#
# def drink(self,things):
#     print(f"{self.name}正在喝{things}")
#
# def sleep(self):
#     print(f"{self.name}正在睡觉...")
#
# #动态地给Person类增加静态方法
# Person.say_hello = show #演示方法名与函数名不一致（可以）
# Person.say_hello()
#
# #动态地给Person类增加类方法
# Person.home = "地球" #动态给类加了类属性
# Person.show_home = show_home #演示方法名与函数名一致（可以）
# Person.show_home()
#
# p1 = Person()
# p2 = Person()
# p1.name = "柴林燕" #动态给类加了实例属性
# p2.name = "孙艺萌" #动态给类加了实例属性
#
#
# p1.eat = types.MethodType(eat,p1) #只给p1对象增加实例方法，与p2无关
# p1.eat("海鲜")
# # p2.eat("汉堡") #报错
#
# """
#     Person.drink = types.MethodType(drink,p1) 看起来像是给Person增加了实例方法drink，好像是所有对象都有drink方法。
#     但是drink(self,things):第一个参数self，被绑定给p1，无论是哪个对象在调用drink方法，self都是p1。
#     所以，这种写法，语法上没有报错，但是逻辑上是有问题的。
# """
# Person.drink = types.MethodType(drink,p1)
# p1.drink("奶茶")
# p2.drink("咖啡")
#
#
# Person.sleep = sleep
# p1.sleep()
# p2.sleep()

print("=" * 50)
class Person:
    home = "地球"
    def __init__(self, name):
        self.name = name

    @staticmethod #在类中定义静态方法，必须写@staticmethod，否则报错
    def show():
        print("我是一个人")

    @classmethod
    def show_home(cls):#类方法必须加@classmethod，无论它在不在类中，因为加@classmethod,python解释器才会帮我们把类的引用（地址）传给cls
        print("我住在：",cls.home)

    def eat(self,food):
        print(f"{self.name}在吃{food}")




#删除类的静态方法
# Person.show()
# del Person.show #删除类的静态方法
# Person.show() #报错

#删除类的类方法
# Person.show_home()
# del Person.show_home #删除类的类方法
# Person.show_home()

#删除类的实例方法
p1 = Person("张三")
p2 = Person("李四")
p1.eat("海鲜")
p2.eat("汉堡")

# del p1.eat #错误 ，因为这个eat方法是属于Person类所有对象都有的方法
del Person.eat #删除Person类的实例方法eat，所有对象都没有eat方法

# p1.eat("海鲜") #报错
# p2.eat("汉堡")#报错


def drink(self,things): #它不在类中
    print(f"{self.name}正在喝{things}")

p1.drink = types.MethodType(drink,p1) #单独给p1对象增加的drink方法
p1.drink("奶茶")

del p1.drink #OK，因为drink方法只属于p1这一个对象

p1.drink("奶茶")