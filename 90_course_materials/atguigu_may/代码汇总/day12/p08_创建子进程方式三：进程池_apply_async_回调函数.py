"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time
from multiprocessing import Pool

# 定义任务函数1
def print_even(start, end):
    print("偶数开始打印：")
    start = start if start % 2 == 0 else start + 1
    even_total = 0
    for i in range(start, end, 2):
        even_total+=i
        print("even:", i)
        time.sleep(0.1)
    return f"偶数之后:{even_total}"


# 定义任务函数2
def print_odd(start, end):
    print("奇数开始打印：")
    start = start if start % 2 != 0 else start + 1
    odd_total = 0
    for i in range(start, end, 2):
        odd_total+=i
        print("odd:", i)
        time.sleep(0.1)
        if i==13:
            raise Exception("遇到13死亡")
    return f"奇数之后:{odd_total}"

# 回调函数：处理结果
def call_back_func(result):
    print("结果是：",result)

def handle_error(error):
    print("异常是：",error)


if __name__ == "__main__":
    results = []
    with Pool(2) as p:
        p.apply_async(print_even,(1,100),callback=call_back_func,error_callback = handle_error)
        p.apply_async(print_odd,(1,100),callback=call_back_func,error_callback = handle_error)
        p.close()  # 不再提交其他任务给进程池，进程池的任务提交结束了
        p.join() #阻塞主进程，让主进程等子进程完事之后再继续
