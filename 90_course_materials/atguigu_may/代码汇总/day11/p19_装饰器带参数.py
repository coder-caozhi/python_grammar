"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、如果装饰器需要带参数，那么定义格式如下：
    def 装饰器(参数列表1): 这个参数是装饰器的参数
        def middle(func): #func用于接收被装饰的函数
            def inner(参数列表2): #被装饰函数的参数列表
                新增的功能
                value = func(参数列表2)
                return value
            return inner
        return middle
"""

import math

#需求：可以通过装饰器使得求绝对值的函数被执行times次
def times(n):
    def middle(func):
        def inner(x):
            for i in range(n):
                x = func(x)
            return x
        return inner
    return middle

#定义装饰器函数
def get_absolute(func):
    def inner(x):
        x = abs(x) #内置函数，abs求绝对值
        return func(x)
    return inner

#定义装饰器函数3
def get_num(func):
    def inner(x):
        x = int(x)
        return func(x)
    return inner


@get_num
@get_absolute
@times(3)
#定义一个被装饰函数
def get_sqrt(x):
    return math.sqrt(x)

print(get_sqrt(256))
print(get_sqrt(-256))
print(get_sqrt("-256"))