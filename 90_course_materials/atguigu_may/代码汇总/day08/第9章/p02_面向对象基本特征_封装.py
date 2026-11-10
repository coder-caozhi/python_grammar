"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、所有面向对象的编程语言（Python，Java，C++等）都有面向对象的基本特征：
    （1）封装
    （2）继承
    （3）多态
    但是不同的语言，它们这3个特征实现的具体语法是不一样。思想是相同的。
    
    2、为什么要有封装？如何封装？
    生活中快递：包裹
        （1）方便运输
        （2）保护不被损坏
        （3）隐藏隐私
    代码中：
        （1）隐藏类的实现细节，具体包含哪些属性，就会对属性进行“私有化”，使得类的外面无法直接的简单的访问这个“私有化”的属性
        （2）对属性的数据起到“保护”作用。可以把属性“私有化”之后，通过定义方法来修改和访问这个属性，在方法中就可以加逻辑条件判断
        例如：属性值age，如果没有私有化，使用者可能会对其赋予不符合业务要求的数据。
            def set_age(self, age):
                if age<=1 or age>=150:
                     return
                self.__age = age #self.__age是私有化的
        （3）简化使用。例如：使用list。无需关心它的内部的实现细节、具体的属性，也可以使用好它，通过它给我们提供的各种方法。
        
    3、具体如何实现封装？
    提前说明：
        python与其他语言（Java等）语言不同，其他语句对属性的私有化（封装）特别执着，基本上所有标准的类都要进行属性的私有化。
        但是python是遵循最小封装原则，能不封装的，就不封装，相信人的自觉性更多。
        Python 的设计哲学里有一句经典的话：“We are all consenting adults here”（我们都是成年人），
        意思是 Python 不会强制限制开发者的任何操作，更倾向于 “约定优于强制”。
        
    如果要封装，python中有如下几种形式：
    （1）约定式封装：属性名前面加单个下划线。
"""
# class Person:
#     _home = "地球"
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
#
#     def set_age(self, age):
#         if age <= 1 or age >= 150:
#             return
#         self._age = age
#     def get_age(self):
#         return self._age
#
#     def set_name(self, name):
#         self._name = name
#
#     def get_name(self):
#         return self._name
#
#     @classmethod
#     def get_home(cls):
#         return cls._home
#
#     @classmethod
#     def set_home(cls, home):
#         cls._home = home
#
# #不建议在Person类外面直接操作 _属性，但是你如果非要操作它，也没问题
# # print("访问'私有'的类属性：", Person._home)
# # p = Person("张三", 23)
# # print("访问'私有'的实例属性：",p._name)
# # print("访问'私有'的实例属性：",p._age)
#
# Person.set_home("火星")
# print("通过方法来访问类属性：",Person.get_home())
#
# p = Person("张三", 23)
# p.set_age(25)
# print("通过方法来访问实例属性：",p.get_age())
# print("通过方法来访问实例属性：",p.get_name())

"""
    （2）名称改写式封装：属性前面加了两个下划线
    其他语言中，有private关键字来修饰这种私有的属性，但是python中没有明确的单词。
    __属性  会被改写为  _类名__属性
"""
# class Person:
#     __home = "地球"
#     def __init__(self, name, age):
#         self.__name = name
#         self.__age = age
#
#     def set_age(self, age):
#         if age <= 1 or age >= 150:
#             return
#         self.__age = age
#     def get_age(self):
#         return self.__age
#
#     def set_name(self, name):
#         self.__name = name
#
#     def get_name(self):
#         return self.__name
#
#     @classmethod
#     def get_home(cls):
#         return cls.__home
#
#     @classmethod
#     def set_home(cls, home):
#         cls.__home = home

#尝试直接操作“私有化”的属性
# print("访问'私有化'的类属性：",Person.__home) #报错
# p = Person("张三", 23)
# print("访问'私有'的实例属性：",p.__name) #报错
# print("访问'私有'的实例属性：",p.__age) #报错

#以下语法允许，但是不推荐
# print("访问'私有化'的类属性：",Person._Person__home)
# p = Person("张三", 23)
# print("访问'私有'的实例属性：",p._Person__name)
# print("访问'私有'的实例属性：",p._Person__age)

# #建议使用对应的方法
# Person.set_home("火星")
# print("通过方法来访问类属性：",Person.get_home())
#
# p = Person("张三", 23)
# p.set_age(25)
# print("通过方法来访问实例属性：",p.get_age())
# print("通过方法来访问实例属性：",p.get_name())

"""
    （3）辅助（1）（2），给'私有'的属性提供简单的get/set方法，
    让程序员可以像使用 非私有的属性 那样调用方法，本质上是操作 '私有'的属性。
    @property 
    def 属性名(self):
        return self.__属性名
    @属性名.setter
    def 属性名(self, 变量):
        self.__属性名 = 变量
    @property 
    def 属性名(cls):
        return cls.__属性名
    但是不能给类属性加@属性名.setter，在类外面只能通过，类名._类名__属性 = 新值
"""
class Person:
    __home = "地球"
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @classmethod
    @property #property代表属性
    def home(cls): #等价于get_home方法
        return cls.__home

    # @home.setter（错误）
    # @classmethod
    # def home(cls, home): #等价于set_home方法
    #     cls.__home = home
    #python中没有重载的概念（所以的重载是2个方法或函数名称相同，但是形参列表不同。）
    #在python中如果定义了2个名称相同的方法，后者会把前者覆盖了。像age，name方法，通过装饰器处理了。

    @classmethod
    def set_home(cls, home):
        cls.__home = home

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self,name):
        self.__name = name

    @property#作用，相当于把age()方法与self.__age绑定
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age<=1 or age>=150:
            return
        self.__age = age

print("访问'私有'的类属性：", Person.home) #像之前的非私有属性一样调用方法，变相的操作私有的属性
p = Person("张三", 23)
print("访问'私有'的实例属性：",p.name)
print("访问'私有'的实例属性：",p.age)

# Person.home = "火星" #错误
# Person._Person__home = "火星" #可以
Person.set_home("火星")
print("访问'私有'的类属性：", Person.home)
p.name = "张三丰"
p.age = 30
print("访问'私有'的实例属性：",p.name)
print("访问'私有'的实例属性：",p.age)