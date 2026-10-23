"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
    1、比较运算符： 运算结果是True或False
    （1）大于吗 > 
    （2）小于吗 <
    （3）大于或等于吗 >=
    （4）小于或等于吗 <=
    （5）等于吗   ==  比较两个对象的值（数据值或地址值）
        对于内置的int,str等基础类型，它们已经重写了eq的函数，所以它们进行==比较时，会比较数据值
        对于自定义的类型，如果没有重写eq函数，那么它们进行==比较时，等价于is比较，比较的是地址值（关于自定义类型，后面会单独讲解）
    （6）不等于吗 !=
    
    2、身份运算符：is  比较两个对象的地址值
"""
# a = 5
# b = 3
# print(a > b)
# print(a < b)
# print(a >= b)
# print(a <= b)
# print(a == b)
# print(a != b)

"""
    小整数池的范围[-5, 256]
    整数对象可以被共享是因为整数对象不可变
"""
# x = 500
# y = 500
# print(x == y) #比较数据值
# print(x is y) #比较地址值

"""
    字符串也有intern机制，即字符串也有常量池，共享池。
    在python中，两个字符串的字面量值中不包含空格等空白字符的话，内容一样，就会共享。
    例如：
    s1 = "hello"
    s2 = "hello"
    那么s1,s2指向同一个字符串对象"hello"
    
    s1 = "hello world"
    s2 = "hello world"
    那么s1,s2不会共享的，内存中有2个"hello world"
    
    字符串对象可以被共享，也是因为字符串对象不可变。第5章会再讲可变和不可变的问题。
"""
# s1 = "hello"
# s2 = "hello"
# print(s1 == s2)#比较数据值，字符串的内容
# print(s1 is s2)#比较地址值
#
# s1 = "hello world"
# s2 = "hello world"
# print(s1 == s2) #比较数据值，字符串的内容
# print(s1 is s2) #比较地址值

#下面的内容后面会再讲
# class Student:
#     def __init__(self, name, score):
#         self.name = name
#         self.score = score
# s1 = Student("张三",86)
# s2 = Student("张三",86)
# print(s1 == s2) #比较地址值
# print(s1 is s2) #比较地址值