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



class Person():

    # 定义子类的初始化函数
    def __init__(self,name):
        self.name = name

    # 重写父类的speak函数
    def speak(self):
        print(f"{self.name} 正在唱歌")

    # 定义实例函数
    def thinking(self):
        print(f"{self.name} 正在思考未来")


class Student(Person,Monkey):

    # 独有的实例函数
    def study(self):
        print(f"{self.name} 正在学习Python")

# 创建对象
s = Student("王飞龙")
# 调用继承之Monkey的函数
s.climb()
# 调用继承之Person的thinking函数
s.thinking()
# 调用子类独有的study函数
s.study()
# 调用speak函数
s.speak()