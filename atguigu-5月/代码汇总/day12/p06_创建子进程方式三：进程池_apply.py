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
    for i in range(start, end, 2):
        print("even:", i)
        time.sleep(1)


# 定义任务函数2
def print_odd(start, end):
    print("奇数开始打印：")
    start = start if start % 2 != 0 else start + 1
    for i in range(start, end, 2):
        print("odd:", i)
        time.sleep(1)

if __name__ == "__main__":
    with Pool(2) as p:
        p.apply(print_even,(1,100))
        p.apply(print_odd,(1,100))
        #2个任务是同步进行的，即一个任务完成，另一个任务才开始