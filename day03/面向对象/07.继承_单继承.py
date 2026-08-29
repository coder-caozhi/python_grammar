class Monkey:

    # 定义初始化函数
    def __init__(self,name):
        self.name = name

    # 实例函数
    def climb(self):
        print(f"{self.name} 在攀爬")

    # 实例函数
    def speak(self):
        print(f"{self.name} 在啊啊啊大叫")



class Person(Monkey):

    # 定义子类的初始化函数
    def __init__(self,name,age):
        # 调用父类的初始化函数
        super().__init__(name)
        self.age = age

    # 重写父类的speak函数
    def speak(self):
        print(f"{self.name} 正在唱歌")

    # 定义实例函数
    def study(self):
        print(f"{self.name} 正在思考未来")



# 创建对象
p = Person("王飞龙",24)
# 调用继承的climb函数
p.climb()
# 调用重写的speak函数
p.speak()
# 调用扩展的study函数
p.study()