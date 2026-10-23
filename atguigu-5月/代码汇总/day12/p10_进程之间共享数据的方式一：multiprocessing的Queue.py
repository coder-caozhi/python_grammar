"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
from multiprocessing import Process,Queue,Pool
#定义任务函数：往一个列表中添加一组偶数
def put_even(nums_queue):
    print("开始往列表中添加偶数")
    for i in range(2,10,2):
        nums_queue.put(i) #put添加元素到队列中，不是用append
    print(f"偶数添加完成")

# 定义任务函数：往一个列表中添加一组奇数
def put_odd(nums_queue):
    print("开始往列表中添加奇数")
    for i in range(1, 10, 2):
        nums_queue.put(i)
    print(f"奇数添加完成")


if __name__ == "__main__":
    data_queue = Queue() #用于在多个进程之间装共享数据的一个队列，一个数据结构
    p1 = Process(target=put_even,args=(data_queue,)) #args接收的参数需要用元组的形式传递
    p2 = Process(target=put_odd,args=(data_queue,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"打印最终的列表（获取2个子进程放的所有数字）：")
    while not data_queue.empty(): #data_queue.empty()如果队列为空，返回True，前面加not表示队列非空
        print(data_queue.get()) #从队列中取数据

# if __name__ == "__main__":
#     #Queue objects should only be shared between processes through inheritance
#     data_queue = Queue() #错误，multiprocessing.Queue不支持进程池的情况。只支持直接创建Process类对象或继承Process类的对象。
#     with Pool() as p:
#         p.apply(put_even,(data_queue,))
#         p.apply(put_odd,(data_queue,))
#
#     print(f"打印最终的列表：")
#     while not data_queue.empty():
#         print(data_queue.get())