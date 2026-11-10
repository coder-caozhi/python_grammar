"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time

"""
    2、创建进程的方式二：继承Process类
    必须重写run函数，把该进程要完成的任务，写到run方法中。
    任务完成如果需要额外的参数，可以在子类的__init__方法中定义实例属性，进行初始化。
    且在__init__方法中要调用父类的__init__来完成父类中定义的实例属性的初始化。
"""
from multiprocessing import Process

class EvenProcess(Process):
    def __init__(self,start,end):
        self.start_num = start if start % 2 == 0 else start + 1
        self.end = end
        super().__init__()

    def run(self): # 定义任务函数1
        print("偶数开始打印：")
        for i in range(self.start_num, self.end, 2):
            print("even:", i)
            time.sleep(1)

class OddProcess(Process):
    def __init__(self,start,end):
        self.start_num = start if start % 2 != 0 else start + 1
        self.end = end
        super().__init__()

    def run(self):# 定义任务函数2
        print("奇数开始打印：")
        for i in range(self.start_num, self.end, 2):
            print("odd:", i)
            time.sleep(1)

"""
注意：在Windows上执行要加上if __name__ == "__main__"。
Unix/Linux：使用fork方式，直接复制父进程内存空间，不会重新执行导入主模块的脚本。
Windows系统使用spawn方式创建新进程，会重新导入主模块的脚本。没有 if __name__ == "__main__": 保护，子进程就会重新执行创建进程的代码，导致无限递归创建进程
"""
if __name__ == "__main__":  # 主进程
    # p1和p2是子进程，print_event任务函数是在子进程中被调用执行
    p1 = EvenProcess(1, 100)
    p2 = OddProcess(1, 100)
    p1.start()
    p2.start()
