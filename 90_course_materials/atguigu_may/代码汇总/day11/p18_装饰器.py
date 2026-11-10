"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import math

"""
    装饰器之前提到过：@property，@classmethod，@staticmethod等
    1、什么是装饰器？
    装饰器允许在不修改原有函数代码的基础上，动态地增加或修改函数的功能。
    装饰器本质上是一个接收函数作为输入并返回一个新的包装过后的函数的对象。
    
    2、装饰器的定义方式一：
    def 装饰器名称(func): #装饰器函数的参数接收被装饰的函数，func是参数名，自己取，但是作用是固定的，用于被装饰的函数。
        def inner(参数): #inner名称自己取。这里的(参数)列表与被装饰函数的参数列表一致
            # 添加功能
            value = func(参数) #value值是被装饰函数的返回值
            # 添加功能
            return value #返回被装饰函数的返回值
        return inner #返回内部函数inner，上面叫inner，这里就叫inner
"""
#需求：
# #定义一个被装饰函数
# def get_sqrt(x):
#     return math.sqrt(x)
#
# #测试
# if __name__ == "__main__":
#     print(get_sqrt(9))
#     print(get_sqrt(-9)) #如果传入负数，希望求它绝对值的平方根
#     print(get_sqrt("9")) #如果是字符串，希望把它转为整数，然后求平方根
#     print(get_sqrt("-9"))

# #定义一个被装饰函数
# def get_sqrt(x):
#     return math.sqrt(x)
#
# #定义装饰器函数
# def get_absolute(func):
#     def inner(x):
#         x = abs(x) #内置函数，abs求绝对值
#         return func(x)
#     return inner
#
# #如何使用装饰器函数对被装饰函数进行装饰
# #方式一：手动装饰
# # f = get_absolute(get_sqrt)
# # print(f(9))
# # print(f(-9))
#
# get_sqrt = get_absolute(get_sqrt) #使用原来的函数名接收包装过的函数对象，get_sqrt函数功能增强了
# print(get_sqrt(9))
# print(get_sqrt(-9))

#定义装饰器函数
def get_absolute(func):
    def inner(x):
        x = abs(x) #内置函数，abs求绝对值
        return func(x)
    return inner

#定义装饰器函数2
def get_num(func):
    def inner(x):
        x = int(x)
        return func(x)
    return inner

#如何使用装饰器函数对被装饰函数进行装饰
#方式二：@装饰器 标记在被装饰函数的上面
#定义一个被装饰函数
@get_num
@get_absolute
def get_sqrt(x):
    return math.sqrt(x)


print(get_sqrt(9))
print(get_sqrt(-9))
print(get_sqrt("9"))
print(get_sqrt("-9"))

"""
    如果有多个装饰器装饰同一个函数时，那么顺序有要求：
    把装饰的过程，看成一个包裹的过程，最里面的是被装饰函数，
    装饰过程与执行过程是反着的。
    从外到内执行，装饰的顺序是由内到外
    
    @get_num   （执行1）    （装饰2）
    @get_absolute（执行2） （装饰1）
    def get_sqrt(x):（执行3）
"""
