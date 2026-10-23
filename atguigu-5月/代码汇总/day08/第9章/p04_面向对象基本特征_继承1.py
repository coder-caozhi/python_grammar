"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、为什么要继承？
    生活中：财产继承、基因继承、文化传承
        （1）延续性  （2）扩展性/突变/改良
    代码中：
        （1）代码的复用性：子类可以使用父类已经声明过的属性、方法等成员
        （2）代码的扩展/重写：子类可以扩展自己的新成员，或对父类的方法进行重写
        （3）逻辑意义上 子类与父类有一个is-a的关系。
            Student is a Person.  学生这个分类是属于人这个大的分类的一个分支，派别。
            
    2、继承
    继承的优点：
        1. 代码复用：父类的通用逻辑只写一次，所有子类直接复用，减少冗余；
        2. 功能扩展：子类可通过新增方法 / 重写方法快速扩展功能，符合 “开闭原则”（对扩展开放，对修改关闭）；
        3. 结构清晰：通过继承梳理类之间的层级关系，代码结构更直观。
        
    继承的缺点：
        1. 耦合度高：子类和父类强关联，父类的修改会直接影响所有子类，增加维护成本；
        2. 多继承复杂：多继承会导致 MRO、菱形继承等问题，代码可读性和可维护性下降；（python有多继承，Java只有单继承）
        3. 灵活性低：继承是静态的，编译时确定，无法动态改变继承关系。
        
    3、如何继承？
    class 子类名(父类名):
        子类的成员
    class 子类名(父类名1,父类名2,父类名3):
        子类的成员
"""
# #演示单继承
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f"{self.name} is eating.")
#
# class Student(Person):
#     pass
#
# s = Student("张三", 23)
# s.eat()
# print("学生对象的属性：",s.name)
# print("学生对象的属性：",s.age)

# #演示单继承
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def eat(self):
#         print(f"{self.name} is eating.")
#
# class Student(Person):
#     def __init__(self, name, age,score):
#     #     self.name = name
#     #     self.age = age
#         super().__init__(name, age)
#         self.score = score
#
#     def study(self):
#         print(f"{self.name} is studying.")
#
# s = Student("张三", 23, 89)
# s.eat()
# s.study()
# print("学生对象的属性：",s.name)
# print("学生对象的属性：",s.age)
# print("学生对象的属性：",s.score)
