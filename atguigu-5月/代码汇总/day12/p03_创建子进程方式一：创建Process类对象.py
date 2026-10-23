"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time

"""
    1、创建进程的方式一：创建Process类的对象
"""
from multiprocessing import Process

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

"""
注意：在Windows上执行要加上if __name__ == "__main__"。
Unix/Linux：使用fork方式，直接复制父进程内存空间，不会重新执行导入主模块的脚本。
Windows系统使用spawn方式创建新进程，会重新导入主模块的脚本。没有 if __name__ == "__main__": 保护，子进程就会重新执行创建进程的代码，导致无限递归创建进程
"""
if __name__ == "__main__":  # 主进程
    # p1和p2是子进程，print_event任务函数是在子进程中被调用执行
    p1 = Process(target=print_even, args=(1, 100))
    p2 = Process(target=print_odd, args=(1, 100))
    p1.start()
    p2.start()
