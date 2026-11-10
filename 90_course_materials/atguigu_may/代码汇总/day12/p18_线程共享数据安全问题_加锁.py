"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time
from threading import Thread,current_thread,Lock
#经典案例：卖票问题
#有一个演唱会门票，分为多个渠道同时卖票
# def sale_ticket():
#     ct = current_thread() #获取执行这个任务的当前线程对象
#     global total_ticket
#     lock.acquire()
#     while total_ticket>0:
#         time.sleep(1)
#         total_ticket -= 1
#         print(f"{ct.name}卖出一张票，剩余：{total_ticket}张")
#     lock.release()
#
# if __name__ == "__main__":
#     total_ticket = 10
#     lock = Lock()
#     t1 = Thread(target=sale_ticket)
#     t2 = Thread(target=sale_ticket)
#     t1.start()
#     t2.start()

"""
    上面的代码加锁了，解决的安全问题，但是锁的代码范围太大了。导致其他线程没有机会。
    锁的代码范围怎么样是合适的呢？
    通常是单次任务的代码，具有原子性不可拆分的代码。
    例如：买一次票
            （1）查看是否有余票
            （2）减少票数
            （3）打印票数
"""

def sale_ticket():
    ct = current_thread() #获取执行这个任务的当前线程对象
    global total_ticket

    while total_ticket>0:
        time.sleep(0.001)
        try:
            lock.acquire()
            if total_ticket>0:
                time.sleep(0.1)
                total_ticket -= 1
                print(f"{ct.name}卖出一张票，剩余：{total_ticket}张")
            else:
                print("票已卖完")
                break
        finally:
            lock.release()

if __name__ == "__main__":
    total_ticket = 10
    lock = Lock()
    t1 = Thread(target=sale_ticket)
    t2 = Thread(target=sale_ticket)
    t1.start()
    t2.start()

"""
    在测试中暂时没有发现安全问题，如何判断自己的代码是否有必要加锁，预防安全问题？
    （1）是否有多个线程
    （2）多个线程是否使用共享数据
    （3）对共享数据是否有修改/写操作
    共享资源可以是一个变量、一个文件、一个数据表中的记录、一台打印机资源等。
    只要3个条件同时满足，就一定隐藏着线程安全问题，出现问题是早晚的事情。
"""