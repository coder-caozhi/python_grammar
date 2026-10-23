"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    1、在python中有一类方法，被称为魔法方法，
    （1）他们的方法名非常特殊，__方法名__，即有2个下划线开头且2个下划线结尾。例如：__init__
    （2）这些魔法方法不是程序员手动调用，而是当对应的“动作”发生时，自动调用，即这些魔法方法与具体的行为绑定在一起。
    
    2、所有类的根父类是object，这些魔法方法在object类中定义，我们自己的类可以重新实现它们。
    如何打开object类的“源文件”？快捷键Ctrl  + N打开搜索框，输入object类名，打开对应的模块文件builtins
    
    2、常见的魔法方法：
    （1）__str__(self)：默认实现会返回 <类名 object at 0x内存地址>。被str(对象)、print(对象)、format(对象)隐式调用。如果重写，一般面向用户（简洁友好可读）。
    （2）__repr__(self)：默认实现会返回 <类名 object at 0x内存地址>。被repr(对象)、Python 交互式解释器直接输入对象、调试工具隐式调用。
    如果重写，面向开发者（准确可还原）。 缺__str__时会自动调用__repr__，缺__repr__时则返回默认的内存地址格式。
    
    当我们用print(对象)打印一个对象时，那么会自动调用  print(对象.__str__())，如果想要更加优化的信息，需要重写__str__()方法。
    当我们用str(对象)类型转换时，那么会自动调用  str(对象.__str__())，如果想要更加优化的信息，需要重写__str__()方法。
    当我们用print(对象)、str(对象)等对对象进行字符串处理时，优先找该类的__str__()方法，如果没找到，继续找该类的__repr__()，
    如果仍然没找到，就找它父类的__str__()。。。。。最后找到object类中，默认返回<类名 object at 0x内存地址>。  

"""
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     # def __str__(self):
#     #     return f"姓名：{self.name}，成绩：{self.score}"
#
#     def __repr__(self):
#         return f"({self.name=}，{self.score=})"
#
# s1 = Student("张三",89)
# s2 = Student("李四",96)
# print(s1)
# print(s2)
# #
# # # info = "s1的信息：" + s1 #报错，因为s1不是字符串，不能与字符串直接拼接
# # info  = "s1的信息：" + str(s1)
# # print(info)
#
# students_list = [s1,s2]
# print(students_list) # 首先，print(students_list.__str__()) ，在list类型中__str__()，它是调用每一个元素的__repr__()方法来将元素信息拼接起来的。

"""
    （2）__eq__()：这就是控制对象 “相等性判断（==）” 的核心方法。绝大多数情况下，自定义类都需要重写__eq__()。
    默认继承自object类的__eq__()方法，其逻辑是判断两个对象是否是内存中的同一个实例（即比较内存地址，等价于is运算符）。
    
    类似的还有：__ge__()、__gt__()、__le__()、__lt__()、__ne__()等
    eq 对应的是 == 
    ne 对应的是 !=
    ge 对应的是 >=
    gt 对应的是 >
    le 对应的是 <=
    lt 对应的是 < 
"""
# class Student:
#     def __init__(self,name,score):
#         self.name = name
#         self.score = score
#
#     def __eq__(self,other):
#         return self.name == other.name and self.score == other.score
#         #self.name == other.name  等价于 str.__eq__(self.name, other.name) 找str类的__eq__方法
#         #self.score == other.score  等价于 int.__eq__(self.score, other.score) 找int类的__eq__方法
#         #str,int等类型都已经重写过__eq__方法，用于比较具体的数据值
#
#     def __ge__(self,other):
#         return self.score >= other.score
#
# s1 = Student("张三",89)
# s2 = Student("张三",89)
# print(s1 is s2) #比较2个对象的地址值
# print(s1 == s2)#比较2个对象的地址值 还是 2个对象的属性值，要看你是否重写了__eq__方法。默认与is的功能一样
#               # 等价于 Student.__eq__(s1,s2)
#
# print(s1 >= s2)

"""
（1）__new__(cls, *args, **kwargs)：对象实例化时第一个调用的方法。需要调用super().__new__(cls)创建实例对象，并返回实例对象。一般不会重写它。
（2）__init__(self, 实例属性参数)：类的实例初始化方法。它通常都会重写，只要这个类有实例属性需要初始化。
                又称为，构造函数。
（3）__del__(self)： 对象的销毁器，定义了当对象被垃圾回收时的行为。使用 del xxx 时不会主动调用 del() ，除非此时引用计数==0。通常也不会重写它。
"""
# class Student:
#     @classmethod
#     def __new__(cls, *args, **kwargs):#它是一个类方法
#         print("一个Student对象被创建了")
#         return super().__new__(cls) #super()找父类的xx成员，这里找父类__new__()方法
#                                                 #此时咱们没写Student的父类是谁，默认的父类就是object，而object的__new__()没有那么多参数的
#     def __init__(self,name=None,score=None): #它是一个实例方法，用于为刚刚用__new__()方法创建的对象进行初始化，为对象的实例属性赋初始值
#         print(f"Student对象{self=}正在初始化了")
#         self.name = name
#         self.score = score
#
#     def __del__(self):
#         print(f"学生对象{self=}正在被销毁")
#
# s1 = Student()
# print(s1)
#
# del s1 #删除对象（了解）
#
# # print(s1) #无法再使用s1

"""
（4）__getattribute__(self, name)：属性访问拦截器，定义了属性被访问前的操作。name是指属性名（name参数名可以自己命名）。
    必须使用 super().__getattribute__(name)来避免无限递归。
    super().__getattribute__(name)获取的就是属性值，最后必须返回属性值。
（5）__setattr__(self, name, value)：属性赋值拦截器，定义了属性被赋值前的操作。
        name是指属性名，value是给属性的值（name和value可以自己命名）。
        必须使用super().__setattr__(name,value)来避免无限递归。
        一般不会重写它。
    
"""
# class Student:
#     def __init__(self, name, age):
#         #下面的2行代码就是在为属性赋值
#         self.name = name
#         self.age = age
#
#     def __setattr__(self, name, value): #name代表属性名，value代表属性值
#         # print(f"{name}属性正在被赋值为{value}")
#         super().__setattr__(name, value) #必须加上这句代码才能确保赋值动作真正的完成
#
#     def __str__(self):
#         return f"姓名：{self.name}，年龄：{self.age}" #这句代码，正在访问属性值
#
#     def __getattribute__(self, name):
#         print(f"{name}属性值正在被获取")
#         return super().__getattribute__(name)
#
# s1 = Student("张三",23)
# print(s1)
# print("s1的name：",s1.name) #这句代码，正在访问属性值

"""
    小结：
        如上的魔法方法，大家重点掌握：__init__，__str__/__repr__，__eq__系列。
                    其余的了解一下：__new__，__del__，__getattribute__，__setattr__等
"""

"""
    补充：哈希有关的问题（了解）
    在python中默认情况下，对象的哈希值是以内存地址来代替的。
    如果自定义的类，重写了__eq__方法，那么默认的__hash__方法就失效了，就无法用内存地址来代表哈希值，如果此时还想要对象支持哈希操作，必须重写__hash__方法。
"""
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'Student(name={self.name}, age={self.age})'

    def __eq__(self, other):
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))

s1 = Student("张三", 23)
s2 = Student("李四", 24)
s3 = Student("张三", 23)
set_demo = {s1, s2, s3} #集合set代表数据结构是哈希表。集合存储每一个元素时，需要获取元素的哈希值，
                    # 然后与p（p是比哈希表中数组的长度小的最大的质数）做%运算，得到存储位置，数组的索引。
                    #set集合的元素不重复
                    #不重复：（1）哈希值不同（2）两个对象__eq__结果是False
                    #如果两个对象哈希值不同，直接认为是不同的对象；如果两个对象的哈希值相同，就用__eq__判断，为False认为不同，为True认为相同。
print(set_demo)

print(hash(s1)) #当我们调用内置函数hash(对象)，等价于调用  对象.__hash__()
print(hash(s3))

