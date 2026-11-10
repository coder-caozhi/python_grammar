"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
import os.path
import time

"""
    time模块的函数等看笔记
"""
# import time
# #求1+2+3+...+n的和
# def total_num(n):
#     total = 0
#     for i in range(1,n+1):
#         total += i
#     return total
#
# def total_num2(n):
#     return n * (n + 1) // 2
#
# n = 100000000
# start = time.time() #获取一个时间戳
# print(total_num(n))
# middle = time.time()
# print("total_num函数的执行时间：", middle - start)
#
# print(total_num2(n))
# end = time.time()
# print("total_num2函数的执行时间：", end - middle)

# t = os.path.getctime("hello.txt")
# print(t)
# t_struct = time.localtime(t)
# print(t_struct)
# t_str = time.strftime("%Y-%m-%d %H:%M:%S", t_struct)
# print(t_str)

for i in range(10,0,-1):
    print(i)
    time.sleep(1) #休眠1秒
