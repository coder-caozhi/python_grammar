"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
import random

"""
    1、集合set的特点
    （1）无序
    （2）元素不可重复
    （3）可变
    （4）代表的数据结构：哈希表
    数据结构：（1）逻辑结构：体现元素之间关系（2）物理结构：底层实现的代码
    集合的逻辑结构：哈希表，物理结构：在python中它是数组，在Java中它是数组+单链表+红黑树
    
    2、创建集合
    （1）{元素1，元素2，元素3}
    （2）set(容器)
    （3）特殊的空集合：set()
        {}得到的不是set集合，而是dict字典
    
"""
# set_one = {11,2,3,3,2,41}
# print(set_one)
# set_two = set("hello")
# print(set_two)
# set_three = set([1,2,1,2,5])
# print(set_three)
# #思考：如何去除一个列表的重复元素
# list_demo = [1,2,1,2,5]
# print("有重复元素：",list_demo)
# list_demo = list(set(list_demo))
# print("没有重复元素：",list_demo)
#
# set_four = set()
# print(type(set_four))

"""
    3、集合增删改查遍历
    （1）增加
    集合.add(元素)
"""
# set_demo = {1,2,3}
# set_demo.add(4)
# print(set_demo)
# set_demo.add(14)
# print(set_demo)
# set_demo.add(11)
# print(set_demo)

"""
    哈希表如何存储数据（理解）？
    （1）什么是哈希？
    哈希是一个整数值。像python，Java等面向对象的编程语言中，会将每一个对象映射为一个整数，
    就像生活中，每一个人的基本信息被映射为一个身份证号码一样。至于怎么映射，不同的哈希函数原理不同，
    python中默认情况下是把内存地址作为hash值，但是很多对象是改写过__hash__()。
    （2）哈希是一个整数值的意义
    整数值就可以用来计算对象存到数组中的索引位置。
    
"""

"""
    （2）删除
    集合.remove(目标元素) ，删除的元素必须存在
    集合.pop()  默认删除哈希表结构的第一个非空元素（第一个元素会随着底层数组的长度变化而变化）
    集合.clear()：清空
"""
# set_demo = {10,20,30,40,50,60,70,80,90,100}
# print("删除之前：",set_demo)
# set_demo.remove(50)
# print("删除之后：",set_demo)
# # set_demo.remove(500) #报错
# set_demo.pop() #哈希表结构的第一个非空的元素
# print("删除之后：",set_demo)
# set_demo.clear()
# print("清空之后",set_demo)

"""
    （3）修改：没有修改单个元素的方法
    iterable：可迭代，即容器
"""
# set_demo = {10,20,30,40,50,60,70,80,90,100}
# set_demo.update([500]) #update的参数需要是一个列表、字符串、集合等可迭代对象，类似于求并集
# set_demo.update({900,800})
# print(set_demo)

"""
    （4）查询
    元素 in 集合
"""
# set_demo = {10,20,30,40,50,60,70,80,90,100}
# print("10在集合中吗？", 10 in set_demo)
# print("15在集合中吗？", 15 in set_demo)

"""
    （5）遍历
    for 元素 in 集合:
        代码
        
    （6）统计分析
    max(集合)     max和min要求元素支持可比较大小
    min(集合)
    sum(集合)  sum要求元素是数组类型
    len(集合)
    （7）排序，反转？没有
    
    （8）推导式
    集合推导式：{表达式 for 元素 in 可迭代对象} → 直接生成集合
"""
#产生10个[1,50]的整数，放到集合中
# nums = { random.randint(1,50) for i in range(10) }
# print(nums)
# print("元素个数：",len(nums))  #元素个数可能小于10

#思考：产生10个不一样的元素放到集合中？？
# nums = set()
# while len(nums) < 10:
#     nums.add(random.randint(1, 50))
# print(nums)
# print("元素个数：",len(nums))

"""
    4、两个集合的操作
    （1）并集
        a | b
        a.union(b)
        a.update(b)
    （2）交集
        a & b
        a.intersection(b)
        a.intersection_update(b)
    （3）差集
        a - b
        a.difference(b)
        a.difference_update(b)
    （4）对称差集
        a ^ b
        a.symmetric_difference(b)
        a.symmetric_difference_update(b)
"""
#并集
# one = {1,2,3,4}
# two = {3,4,5,6}
# print("并集：", one | two) #返回一个新集合
# print("并集：", one.union(two))#返回一个新集合
# print("并集：", one.update(two)) #直接修改one集合，相当于 one = one | two
# one.update(two)
# print("并集：",one)

#交集
# one = {1,2,3,4}
# two = {3,4,5,6}
# # print("交集：", one & two) #返回新集合
# # print("交集：", one & two) #返回新集合
# # print("交集：", one.intersection(two)) #返回新集合
# # print("交集：", one.intersection_update(two)) #返回None，直接修改one
# one.intersection_update(two)
# print("交集：",one)

#差集
# one = {1,2,3,4}
# two = {3,4,5,6}
# # print("差集：", one - two) # 取one中不在two中出现的元素，或者one中与two不同的元素，返回新集合
# # print("差集：", one.difference(two))#返回新集合
# # print("差集：", one.difference_update(two))#None
# one.difference_update(two)#直接更新one
# print("差集：",one)

#对称差集
# one = {1,2,3,4}
# two = {3,4,5,6}
# print("对称差集：", one ^ two)#返回新集合
# print("对称差集：", one.symmetric_difference(two))#返回新集合
# # print("对称差集：", one.symmetric_difference_update(two))#返回None
# one.symmetric_difference_update(two)
# print("对称差集：",one)