"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import math

"""
    装饰器的第二种定义方式：定义装饰器类
    class 装饰器类名:
        def __init__(self, 装饰器的参数列表):
            pass
        def __call__(self, func): #func用于接收被装饰函数
            def inner(参数列表): #被装饰函数的参数列表
                增加功能
                value = func(参数列表)
                增加功能
                return value
            return inner
    
- __call__方法，call方法的参数是被装饰函数。在call中定义内部函数，核心逻辑写在内部函数里，然后call返回内部函数。
- __init__方法：如果装饰器带参数，就在__init__方法的形参列表定义该参数。如果装饰器不带参数，__init__可以不写。

"""
class AbsoluteDecoratorClass:
    def __call__(self, func):
        def inner(x):
            x = abs(x)
            return func(x)
        return inner
#
# #定义一个被装饰函数
# @AbsoluteDecoratorClass() #()不能省略，因为
# def get_sqrt(x):
#     return math.sqrt(x)
#
# if __name__ == "__main__":
#     print(get_sqrt(9))

class TimesDecoratorClass:
    def __init__(self,times):
        self.times = times

    def __call__(self, func):
        def inner(x):
            for i in range(self.times):
                x = func(x)
            return x
        return inner

#定义一个被装饰函数
@AbsoluteDecoratorClass() #()不能省略，因为这里需要创建对象
@TimesDecoratorClass(3)
def get_sqrt(x):
    return math.sqrt(x)

if __name__ == "__main__":
    print(get_sqrt(-256))