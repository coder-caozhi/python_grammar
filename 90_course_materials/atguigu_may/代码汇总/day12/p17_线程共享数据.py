"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time
from threading import Thread,current_thread
#经典案例：卖票问题
#有一个演唱会门票，分为多个渠道同时卖票
def sale_ticket():
    ct = current_thread() #获取执行这个任务的当前线程对象
    global total_ticket
    while total_ticket>0:
        # time.sleep(0.001)
        total_ticket -= 1
        print(f"{ct.name}卖出一张票，剩余：{total_ticket}张")

if __name__ == "__main__":
    total_ticket = 10
    t1 = Thread(target=sale_ticket)
    t2 = Thread(target=sale_ticket)
    t1.start()
    t2.start()

"""
    从上面代码的运行结果中能看出：同一个进程的多个线程之间可以通过使用全局变量直接实现共享数据的效果，
    不需要额外的借助Queue，Pipe等方式
    
    刚才运行时出现负数票，重复票等问题，就是线程安全问题。
"""