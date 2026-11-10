"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、什么是生成器？
    生成器是一种特殊的迭代器，默认自带__next__方法。
    普通的迭代器返回值的时候用return语句（直接结束当前方法的执行），
    而生成器返回值的时候用yield语句（暂停当前方法的执行，之后可以继续刚才的位置往下执行直到遇到下一个yield语句或StopIteration异常）。
    
    生成器也可以与其他迭代工具（如for循环）无缝配合使用，提供简洁和高效的迭代方式。
    
    2、如何使用
    （1）使用函数定义生成器
    要点：任何包含yield语句的函数都可以产生生成器
         包含yield语句的函数的函数体，需要我们遍历生成器才能执行，即调用它的__next__方法。
"""
def func():
    print("hello")
    yield 1
    print("world")
    yield 2
    print("python")
    yield 3

if __name__ == "__main__":
    g = func() #得到的是一个生成器对象，一个特殊的迭代器对象
    # print(type(g)) #<class 'generator'>
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    # print(g.__next__())
    while True:
        try:
            print(g.__next__())
        except StopIteration:
            break