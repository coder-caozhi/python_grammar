"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、利用MRO原则，完成复杂的实例初始化为属性初始化问题
"""
# 定义父类
class Animal:
    """动物类"""
    def __init__(self, name, **kwargs):
        print("Animal父类构造方法")
        self.name=name
        super().__init__(**kwargs) #加这句话的意义是什么？为Animal后面的其他父类继续初始化
        #super代表object？？
        #super也有可能不是直接代表object，因为子类的父类除了Animal之外，后面还有其他的父类

# 定义父类
class Fish(Animal):
    """鱼类类"""
    def __init__(self, name=None, **kwargs): #**kwargs可变参数，接收0~n个键值对 key=value的参数
        print("Fish父类构造方法")
        super().__init__(name,**kwargs)  # 传递剩余参数， **kwargs叫做解包传参，把kwargs中接收的多个键值对拆开再传给下一个__init__
        #super，如果单纯从Fish的关系出发，应该是指Animal
        #super，这里是从子类RoboticFish开始搜索过来的，所以super应该是看RoboticFish的父类们，super是
# 定义父类
class Person(Animal):
    """人类类"""
    def __init__(self, name=None, gender=None, **kwargs):
        print("Person父类构造方法")
        self.gender = gender
        super().__init__(name,**kwargs)  # 传递剩余参数
        #super代表Animal

# class A:
#     def __init__(self, a,b,c):
#         self.a = a
#         self.b = b
#         self.c = c

# 定义子类
class RoboticFish(Fish, Person):
    """鱼形机器人类"""
    def __init__(self, name, gender, power_capacity):
        print("RoboticFish子类构造方法")
        self.power_capacity = power_capacity
        super().__init__(name=name,  gender=gender)
        #super表示先找Fish

    def __str__(self):
        return f"鱼形机器人名字：{self.name}，性别：{self.gender}，电量：{self.power_capacity}"

# 测试
# 查看方法解析顺序MRO
print(RoboticFish.__mro__)
r = RoboticFish("落雁", "女",98)
print(r)