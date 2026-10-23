"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、演示多继承
    在python中，子类可以从多个父类中延续/继承成员，包括属性和方法。
    
    这些父类是混入类，只有单一功能，而且多个父类之间的功能不重叠。
"""
# 定义父类
class Flyable: #Flyable通常不会自己new对象，等着被继承
    """
    飞行能力类
    注意：使用此类的子类需要提供 name 属性
    """
    def fly(self): #这个方法是给子类继承用的
        print(f"{self.name} 正在飞行")

# 定义父类
class Swimming:
    """
    游泳能力类
    注意：使用此类的子类需要提供 name 属性
    """
    def swim(self):
        print(f"{self.name} 正在游泳")

# 定义父类
class Walkable:
    """
    行走能力类
    注意：使用此类的子类需要提供 name 属性
    """
    def walk(self):
        print(f"{self.name} 正在行走")

# 定义父类
class Bird:
    """鸟类基类"""
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print(f"{self.name} 在鸣叫")

#定义子类
class Duck(Bird,Flyable,Walkable,Swimming):
    def catch_fish(self):
        print(f"{self.name}在抓鱼")

d = Duck("唐老鸭")
d.swim()
d.walk()
d.fly()
d.make_sound()
d.catch_fish()