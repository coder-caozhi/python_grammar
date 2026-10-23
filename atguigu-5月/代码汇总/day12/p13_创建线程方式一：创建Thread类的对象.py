"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time
from threading import Thread

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
    t1 = Thread(target=print_even,args=(1,100))
    t2 = Thread(target=print_odd,args=(1,100))
    t1.start()
    t2.start()
