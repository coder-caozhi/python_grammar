"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
"""
    1、元组的特点：
    （1）有序
    （2）元素可重复
    （3）不可变
    （4）代表的数据结构：静态数组
    
    2、创建元组
    （1）(元素1，元素2，元素3)
    （2）tuple(容器)
    （3）特殊的空元组：(), tuple()
"""
# tuple_one = (1,2,3)
# print(tuple_one)
#
# tuple_two = tuple("hello")
# print(tuple_two)
#
# tuple_three = ()
# print(tuple_three)
#
# tuple_four = tuple()
# print(tuple_four)

"""
    3、无增、删、改
"""
tuple_demo = (1, 2, 3)
print(tuple_demo)
# tuple_demo.append(4)
# tuple_demo.insert(0,4)
# tuple_demo[0] = 100
# del tuple_demo[0]

"""
    4、容器、序列的通用的其他操作
    
    以下是之前讲过的操作，元组也是序列，也是容器，所以这些操作是相同的。
    1、根据索引/下标访问1个元素：  元组[索引]
    2、根据访问切片多个元素：      元组[start:end:step]
        step为正，从左往右
        step为负，从右往左
        start和end可以使用正下标体系，也可以使用负下标体系
    3、查询某个元素的下标/索引： 元组.index(元素)  元素必须存在，否则报错
    4、统计分析 
    查找元素的最大值：max(元组)
    查找元素的最小值：min(元组)
    查找元素的总和：sum(元组)                 序列的元素必须是数值类型
    查找某个元素重复几次：元组.count(目标元素)
    获取元素的总个数：len(元组)、len(字符串)
    5、判断某个元素在不在序列中：元素 in 序列    （序列：元组、字符串等）
    6、遍历
    (1)for 元素 in 序列:
          语句
    (2)for 下标 in range(start,end,step):
            语句
      range(start,end,step)：产生的是一个等差数列。
        step为正：递增数列
        step为负：递减数列
        start,end可以使用正下标体系，也可以使用负下标体系
    (3)for 下标,元素 in enumerate(序列):
        语句
"""

"""
    元组可以排序吗？不行
    元组可以反转吗？不行
    元组有直接的推导式吗？没有
"""
tuple_demo = (11, 2, 3,4)
print(type(tuple_demo)) #<class 'tuple'>
# tuple_demo.sort() #不行
# tuple_demo.reverse()#不行

t = (i for i in range(5))
print(t) #<generator object <genexpr> at 0x000001C965054E80>
print(type(t)) #<class 'generator'>
