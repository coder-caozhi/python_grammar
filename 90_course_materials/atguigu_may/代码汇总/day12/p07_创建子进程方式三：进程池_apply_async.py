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
    even_total = 0
    for i in range(start, end, 2):
        even_total+=i
        print("even:", i)
        time.sleep(0.1)
    return f"偶数之后:{even_total}"


# 定义任务函数2
def print_odd(start, end):
    print("奇数开始打印：")
    start = start if start % 2 != 0 else start + 1
    odd_total = 0
    for i in range(start, end, 2):
        odd_total+=i
        print("odd:", i)
        time.sleep(0.1)
    return f"奇数之后:{odd_total}"

# if __name__ == "__main__":
#     with Pool(2) as p:
#         #apply_async表示异步提交任务
#         p.apply_async(print_even,(1,100))
#         p.apply_async(print_odd,(1,100))
#         # #2个任务是异步进行的，两个任务同时进行
#         p.close() #不再提交其他任务给进程池，进程池的任务提交结束了
#         p.join() #阻塞主进程，让主进程等子进程完事之后再继续

if __name__ == "__main__":
    results = []
    with Pool(2) as p:
        apply_result1 = p.apply_async(print_even,(1,100)) #返回的是ApplyResult对象
        apply_result2 = p.apply_async(print_odd,(1,100))
        results.append(apply_result1)
        results.append(apply_result2)

        for result in results: #result是ApplyResult对象，它有get()方法获取结果
            print(result.get()) #get()函数会阻塞主进程，等子进程任务结束后，再获取返回结果，那么这样就不需要写close()和join()