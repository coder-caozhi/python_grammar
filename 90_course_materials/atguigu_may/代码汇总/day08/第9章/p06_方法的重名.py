"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、如果子父类定义了同名的方法，是什么？
    重写（Override），子类对父类某个方法的功能进行了覆写。
    那么在python中，同一个类中，或父子类中，都不存在重载（Overload）。
    
    2、在python中的重写与其他语言的重写也有所不同？
    在python中，子父类只要“方法名相同”就是重写，不看形参列表等其他的部分。
    在Java中，子父类方法重写的要求很多，不仅仅要求方法名相同，还得看形参列表、返回值类型、权限修饰符（private、protected）都有要求。
    
    3、如果子类重写了父类的方法，
    （1）在子类外面，通过子类对象调用该方法，参数看子类重写的，执行的是子类重写后的代码
    （2）在子类中，如果想要调用父类被重写方法的代码，那么可以通过 super().方法()
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def eat(self,food):
        print(f"{self.name} is eating{food}")

class Student(Person):
    def __init__(self, name, age,score):
    #     self.name = name
    #     self.age = age
        super().__init__(name, age)
        self.score = score

    def eat(self):
        # print(f"{self.name} 吃学生餐")
        super().eat("学生餐")

s = Student("张三",23,100) #对应的是__init__方法
s.eat()