"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
    容器类型：列表list（重要），集合set（重要），
            字符串str（可以查笔记），元组tuple（可以查笔记，把列表的关于增、删、改，排序，反转的方法去掉就是元组的操作）
            字典（重要）
            冻结集合（了解，set去掉增删改的方法，就是冻结集合的函数）
            
   1、 冻结集合的特点：
    （1）无序
    （2）不可重复
    （3）不可变
    （4）数据结构：哈希表（内部的数组长度是固定的）
    
    2、创建冻结集合
    frozenset(其他的可迭代的容器)
    
    3、增删改（不可以）
    4、查询
    （1）元素 in 集合
    （2）len(集合) 元素个数
    （3）max(集合)、min(集合)、sum(集合)
    
    5、集合与集合的操作
    （1）交集
    （2）并集
    （3）差集
    （4）对称差集
"""
# set_one = frozenset([1,2,3,1,2,3])
# print(set_one)
#
# set_two = frozenset({1,2,3,4,1,2,4})
# print(set_two)

s1 = frozenset({1,2,3,4})
s2 = frozenset({3,4,5,6})
print("交集：", s1 & s2)
print("交集：", s1.intersection(s2))
# print("交集：", s1.intersection_update(s2))#报错，因为frozenset不可变，而intersection_update需要直接修改集合

print("并集：", s1 | s2)
print("并集：", s1.union(s2))
# print("并集：", s1.update(s2))#报错，因为frozenset不可变，而update需要直接修改集合

print("差集：", s1 - s2)
print("差集：", s1.difference(s2))
# print("差集：", s1.difference_update(s2))#报错，因为frozenset不可变，而difference_update需要直接修改集合

print("对称、异或差集：", s1 ^ s2)
print("对称、异或差集：", s1.symmetric_difference(s2))
# print("对称、异或差集：", s1.symmetric_difference_update(s2))#报错，因为frozenset不可变，而symmetric_difference_update需要直接修改集合
