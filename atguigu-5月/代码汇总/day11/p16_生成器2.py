"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import random

"""
     2、如何使用
    （1）使用函数定义生成器（这个函数不是普通的函数）
    要点：任何包含yield语句的函数都可以产生生成器，调用该函数的结果得到一个生成器对象
         包含yield语句的函数的函数体，需要我们遍历生成器才能执行，即调用它的__next__方法。
    （2）使用推导式定义/创建生成器
    
    复习：
        列表推导式：[表达式 for 变量 in 可迭代对象 if 条件]
        集合推导式：{表达式 for 变量 in 可迭代对象 if 条件}
        字典推导式：{key表达式:value表达式 for 变量 in 可迭代对象 if 条件}
        生成器推导式：(表达式 for 变量 in 可迭代对象 if 条件)
        
    推导式也是语法糖
"""
# #列表推导式
# #随机产生10个[1,100]的偶数
# even_nums = [random.randint(1,50)*2   for i in range(10)]
# print(even_nums)
#
# #随机产生10个[1,100]的整数，要求不重复，结果可能少于10
# # nums_set = {random.randint(1,100)  for i in range(10)}
# # print(nums_set)
# nums_set = set()
# while len(nums_set)<10:
#     nums_set.add(random.randint(1,100))
# print(nums_set)
#
# #字典推导式
# #key是[1,5]的整数，value是它的平方
# nums_dict = {key:key**2  for key in range(1,6)}
# print(nums_dict)

# 生成器推导式
# 随机产生10个[1,100]的偶数
# even_nums = (random.randint(1,50)*2   for i in range(10))
# print(type(even_nums))
# print(even_nums)#地址值
# for num in even_nums:
#     print(num)

# while True:
#     try:
#         print(next(even_nums)) #等价于 print(even_nums.__next__())
#     except StopIteration:
#         break

"""
even_nums = (random.randint(1,50)*2   for i in range(10))
等价的代码
"""
def func(): #func()不是普通函数
    for i in range(10):
        yield random.randint(1,50)*2
even_nums = func() #返回生成器对象
while True:
    try:
        print(next(even_nums)) #等价于 print(even_nums.__next__())
    except StopIteration:
        break