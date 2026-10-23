"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
"""
    进程之间默认是不直接共享数据。
    因为每一个进程有独立的内存空间，各自的列表对象在各种的内存中有独立的列表对象，互相不共享。
"""

from multiprocessing import Process
#定义任务函数：往一个列表中添加一组偶数
def put_even(nums_list):
    print("开始往列表中添加偶数")
    for i in range(2,100,2):
        nums_list.append(i)
    print(f"偶数添加完成,{nums_list=}")

# 定义任务函数：往一个列表中添加一组奇数
def put_odd(nums_list):
    print("开始往列表中添加奇数")
    for i in range(1, 100, 2):
        nums_list.append(i)

    print(f"奇数添加完成,{nums_list=}")

if __name__ == "__main__":
    list_demo = []
    p1 = Process(target=put_even,args=(list_demo,)) #args接收的参数需要用元组的形式传递
    p2 = Process(target=put_odd,args=(list_demo,))
    p1.start()
    p2.start()

    p1.join()
    p2.join()
    print(f"打印最终的列表：{list_demo=}")