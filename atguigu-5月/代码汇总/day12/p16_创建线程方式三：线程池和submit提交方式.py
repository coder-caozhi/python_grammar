"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
from concurrent.futures import ThreadPoolExecutor
import time

# 定义任务函数1
def print_even(start, end):
    print("偶数开始打印：")
    start = start if start % 2 == 0 else start + 1
    for i in range(start, end, 2):
        print("even:", i)
        time.sleep(0.1)


# 定义任务函数2
def print_odd(start, end):
    print("奇数开始打印：")
    start = start if start % 2 != 0 else start + 1
    for i in range(start, end, 2):
        print("odd:", i)
        time.sleep(0.1)

if __name__ == "__main__":
    results = []
    with ThreadPoolExecutor() as pool:
       r1 =  pool.submit(print_even,1,100)
       r2 =  pool.submit(print_odd,1,100)
       results.append(r1)
       results.append(r2)
       for r in results:
           print(r.result())