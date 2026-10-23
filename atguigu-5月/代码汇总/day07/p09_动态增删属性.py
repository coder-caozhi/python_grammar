"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    了解python中的动态增删属性、方法等成员。
    
    Java：静态语言，类的成员在编写代码的时候就是确定的，即在运行之前是确定，不会改变的。
    Python、Javascript：动态语言，类的成员在运行时可能动态地增加、删除。一般不建议在运行时动态增删成员。但如果需要，python支持。
    
    1、动态增删属性
    （1）类属性
        增加类属性：类名.新类属性 = 值
        删除类属性：del 类名.类属性
    （2）实例属性
        增加实例属性：对象.新实例属性 = 值
        删除实例属性：del 对象.实例属性
"""
# class Person:
#     pass
#
# #测试
# #动态地给Person类增加类属性
# Person.home = "地球"
# print("新增的类属性：", Person.home)
#
# #动态地给Person的对象增加实例属性
# p1 = Person()
# p2 = Person()
# p1.name = "张三" #只给p1对象增加了实例属性，与其他对象无关
# print("p1对象新增的name属性：",p1.name)
# # print("p2对象的name属性：",p2.name) #错误

class Person:
    home = "地球"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"

# print("Person类的类属性：", Person.home)
# del Person.home
# print("Person类的类属性：", Person.home)

p1 = Person("张三",23)
p2 = Person("李四",24)
print("p1的信息：",p1)
print("p2的信息：",p2)

del p1.name #只删除p1对象的name属性，与p2对象无关

print("p2的信息：",p2)
print("p1的信息：",p1)
