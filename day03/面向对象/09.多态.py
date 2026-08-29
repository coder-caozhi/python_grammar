from random import randint


class Animal:
    # 定义一个eat的函数
    def eat(self):
        print("大动物吃小动物")

class Dog:
    # 定义一个eat的函数
    def eat(self):
        print("狗吃骨头")

class Cat:
    # 定义一个eat的函数
    def eat(self):
        print("猫吃鱼")

class Pig:
    # 定义一个eat的函数
    def eat(self):
        print("猪吃饲料")

class Bird:
    # 定义一个fly的函数
    def fly(self):
        print("我是一只小小鸟，我想要飞，取怎么也飞不高嗷嗷")

# 定义一个函数
def action(animal):
    animal.eat()

# 实例化对象
a = Animal()
d = Dog()
c = Cat()
p = Pig()
b = Bird()

# 调用action函数
action(a)
action(d)
action(c)
action(p)
action(b)
