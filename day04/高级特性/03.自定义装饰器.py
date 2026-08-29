# 装饰器的本质就是一个函数，传入一个函数作为参数，返回一个新函数，作用是在不改变原函数的基础上对原函数的功能进行扩展
# 声明一个求和的函数
import functools

# 新的需求：在计算结果之前和计算得到结果之后在控制台打印日志
def record_logging(fun):
    @functools.wraps(fun)
    def wrapper(*args, **kwargs):
        print(f"{fun.__name__}开始了，传入的参数是：{args}或者{kwargs}")
        # 调用原函数获取计算的结果
        rest = fun(*args, **kwargs)
        print(f"{fun.__name__}返回了结果：{rest}")
        return rest
    # 返回一个新函数
    return wrapper

@record_logging
def add(a,b):
    """
        这是一个求和的函数
    :param a: 第一个参数
    :param b: 第二个参数
    :return: 两个参数的和
    """
    return a + b

@record_logging
def sub(a,b):
    return a - b

# 调用函数
result = add(10,2)
result2 = sub(10,2)