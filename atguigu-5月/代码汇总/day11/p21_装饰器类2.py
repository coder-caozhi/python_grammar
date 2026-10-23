"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import math

"""
    如果装饰器类不带参数，那么可以简化
    class 装饰器类名:
        def __init__(self, func):
            self.func = func
        def __call__(self, 参数列表):#被装饰函数的参数列表
            value = self.func(参数列表)
            return value
"""
class AbsoluteDecoratorClass:
    def __init__(self,func):
        self.func = func

    def __call__(self, x):
        x = abs(x)
        return self.func(x)

#定义一个被装饰函数
@AbsoluteDecoratorClass
def get_sqrt(x):
    return math.sqrt(x)

if __name__ == "__main__":
    print(get_sqrt(9))
