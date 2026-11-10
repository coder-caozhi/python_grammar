"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time

"""
定义一个迭代器类 RangeIterator，接收两个参数 start、end，实现功能：
可以遍历 [start, end) 之间所有 3 的倍数，必须手动实现 __iter__ 和 __next__ 方法，禁止用生成器。
"""
# class RangeIterator:
#     def __init__(self, start, end):
#         self.start = start
#         self.end = end
#         remainder = start % 3
#         self.current = start if remainder == 0 else 3 - remainder + start #找到第一个3的倍数
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         value = self.current
#         self.current += 3 #步长就是3
#         return value
#
# if __name__ == "__main__":
#     r = RangeIterator(1,10)
#     for i in r:
#         print(i)

"""
编写一个生成器函数 fib_generator(n)，生成前 n 项斐波那契数列。规则：
- 第 1、2 项为 1
- 从第 3 项开始，每一项 = 前两项之和
- 使用 yield 实现，不能一次性返回列表
"""
# def fib_generator(n):
#     a = b = 1
#     for i in range(1,n+1):
#         yield a
#         a,b = b,a+b
#
# if __name__ == "__main__":
#     g = fib_generator(10)
#     for i in range(10):
#         print(next(g))

"""
编写一个装饰器 timer，可以装饰任意函数，自动打印该函数的运行时间（秒）。要求：
- 装饰器不带参数
- 能装饰有参 / 无参函数
- 输出格式：函数名 运行时间：x.xx 秒，提示：函数对象.__name__可以获取函数名
"""
#定义装饰器函数
def timer(func):
    def inner(*args): #inner()的参数列表对应被装饰函数的参数。那么因为被装饰函数的参数列表不一致，所以只能选择使用可变参数
        start = time.time()
        value = func(*args)
        end = time.time()
        print(f"{func.__name__}运行时间：{end-start}")
        return value
    return inner

#被装饰函数
@timer
def test_func():
    print("hello")

@timer
def add(start, end):
    sum = 0
    for i in range(start, end + 1):
        sum += i
    return sum

if __name__ == "__main__":
    test_func()
    print(add(1,100000))