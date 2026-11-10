"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    列表list：[]
    集合set：{}
    
    1、对容器的元素统计分析：
    sum(容器)
    max(容器)
    min(容器)
    len(容器)
    2、遍历容器的通用操作
    for 元素 in 容器:
            语句
    3、元素 in 容器
"""
one = {1,2,3}
print("元素累加和：", sum(one))
print("元素最大值：", max(one))
print("元素最小值：", min(one))
print("元素总个数：", len(one))
for i in one:
    print(i)
print("4在容器中吗？", 4 in one)
print("1在容器中吗？", 1 in one)