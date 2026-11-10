"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import random
import time
from multiprocessing import Manager,Process,Pool


# #定义任务函数一：往队列中放随机数
# def put_nums(queue):
#     print("负责往队列中存放数据：...")
#     for i in range(10):
#         queue.put(random.randint(1,100))
#
# #定义任务函数二：从队列中取数据
# def get_nums(queue):
#     print("负责从队列中获取数据：...")
#     while not queue.empty():
#         print(queue.get())
#
# # if __name__ == "__main__":
# #     queue = Manager().Queue() #支持进程池的共享数据
# #     with Pool() as p:
# #         p.apply(put_nums,(queue,))
# #         p.apply(get_nums,(queue,))
#
#
# if __name__ == "__main__":
#     queue = Manager().Queue()
#     p1 = Process(target=put_nums,args=(queue,))
#     p1.start()
#     p2 = Process(target=get_nums, args=(queue,))
#     p2.start()

"""
以上非池的方式代码，报如下错误，原因是这里有主进程和2个子进程。
主进程的代码只是创建了2个子进程，并且启动它们，主进程的任务就结束了。主进程创建的Manager管理器对象就被主进程给销毁了，
当子进程要用管理器中的队列时，发现连接不上管理器。如何解决？

Process Process-2:
Process Process-3:
Traceback (most recent call last):
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 820, in _callmethod
    conn = self._tls.connection
           ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'ForkAwareLocal' object has no attribute 'connection'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\process.py", line 314, in _bootstrap
    self.run()
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "D:\atguigu\ai\BJ20260511AI\01_尚硅谷大模型之Python基础\PythonProject\day12_code\p11_进程之间共享数据的方式二：multiprocessing_Manager_Queue.py", line 15, in put_nums
    queue.put(random.randint(1,100))
  File "<string>", line 2, in put
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 824, in _callmethod
    self._connect()
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 811, in _connect
    conn = self._Client(self._token.address, authkey=self._authkey)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\connection.py", line 517, in Client
    c = PipeClient(address)
        ^^^^^^^^^^^^^^^^^^^
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\connection.py", line 719, in PipeClient
    _winapi.WaitNamedPipe(address, 1000)
FileNotFoundError: [WinError 2] 系统找不到指定的文件。
Traceback (most recent call last):
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 820, in _callmethod
    conn = self._tls.connection
           ^^^^^^^^^^^^^^^^^^^^
AttributeError: 'ForkAwareLocal' object has no attribute 'connection'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\process.py", line 314, in _bootstrap
    self.run()
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\process.py", line 108, in run
    self._target(*self._args, **self._kwargs)
  File "D:\atguigu\ai\BJ20260511AI\01_尚硅谷大模型之Python基础\PythonProject\day12_code\p11_进程之间共享数据的方式二：multiprocessing_Manager_Queue.py", line 20, in get_nums
    while not queue.empty():
              ^^^^^^^^^^^^^
  File "<string>", line 2, in empty
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 824, in _callmethod
    self._connect()
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\managers.py", line 811, in _connect
    conn = self._Client(self._token.address, authkey=self._authkey)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\connection.py", line 517, in Client
    c = PipeClient(address)
        ^^^^^^^^^^^^^^^^^^^
  File "D:\ProgramFiles\Python\Python312\Lib\multiprocessing\connection.py", line 719, in PipeClient
    _winapi.WaitNamedPipe(address, 1000)
FileNotFoundError: [WinError 2] 系统找不到指定的文件。
"""

# #定义任务函数一：往队列中放随机数
# def put_nums(queue):
#     print("负责往队列中存放数据：...")
#     for i in range(10):
#         queue.put(random.randint(1,100))
#
# #定义任务函数二：从队列中取数据
# def get_nums(queue):
#     print("负责从队列中获取数据：...")
#     while not queue.empty():
#         print(queue.get())
#
# if __name__ == "__main__":
#     # queue = Manager().Queue()
#     # p1 = Process(target=put_nums,args=(queue,))
#     # p1.start()
#     # p2 = Process(target=get_nums, args=(queue,))
#     # p2.start()
#     #
#     # #两个join可以保证主进程阻塞，等p1,p2的任务完成之后，再继续，销毁工作
#     # p1.join()
#     # p2.join()
#
#     queue = Manager().Queue()
#     p1 = Process(target=put_nums,args=(queue,))
#     p1.start()
#     p1.join()
#     #p1不结束，下面的代码不走，不启动p2
#     p2 = Process(target=get_nums, args=(queue,))
#     p2.start()
#     p2.join()

# 定义任务函数一：往队列中放随机数
def put_nums(queue,event):
    print("负责往队列中存放数据：...")
    for i in range(10):
        queue.put(random.randint(1,100))
    event.set() #发送信号，给等待的其他进程，告诉它你可以开始干活了

#定义任务函数二：从队列中取数据
def get_nums(queue,event):
    event.wait() #等待信号
    print("负责从队列中获取数据：...")
    while not queue.empty():
        print(queue.get())

if __name__ == "__main__":
    manager = Manager()
    queue = manager.Queue()
    event = manager.Event()
    p1 = Process(target=put_nums,args=(queue,event))
    p1.start()
    p2 = Process(target=get_nums, args=(queue,event))
    p2.start()

    p1.join()
    p2.join()