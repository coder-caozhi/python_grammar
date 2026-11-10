"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
Python允许在定义类的时候，定义一个特殊的 __slots__变量，（了解）
    - __slots__用来限制该类的实例能拥有的实例变量。
      - 实例变量可以是实例属性，也可以是通过实例对象名.实例变量 = types.MethodType(函数名,实例对象名)方式动态添加的实例方法
    - __slots__对类属性、类方法和静态方法、以及其他方式定义和添加的实例方法没有限制。
    - __slots__仅对当前类生效，对其子类无效。
"""
# class Person:
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age,gender):
#         self.name = name
#         self.age = age
#         self.gender = gender
#
# # p1 = Person("张三",23,"男") #错误

# class Person:
#     __slots__ = ('name', 'age')
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# p1 = Person("张三",23)
# p1.gender = "男" #动态增加实例属性

# class Person:
#     __slots__ = ('name', 'age') #name当实例属性用
#
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def name(self): #name是实例方法，他们不能重名
#         print("姓名")
