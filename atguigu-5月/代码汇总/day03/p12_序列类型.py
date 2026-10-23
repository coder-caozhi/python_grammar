"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    1、什么是序列？
    凡是有序的容器对象都可以称为序列。
    字符串序列、列表序列、元组序列、字节串序列等
    
    2、所有序列的共同特征
    （1）有序：能通过索引操作它们
    （2）可重复
    
    3、以列表为例，列表的符号是[]
    4、所有序列的共同操作
    （1）根据索引访问1个元素
        索引的表示有2套：
            正索引：0,1,2,...,元素总个数-1
            负索引：-元素总个数,.... -3,-2,-1
            

"""
# list_demo = [10, 20, 30, 40, 50]
# print(f"第3个元素：", list_demo[2])
# print(f"第3个元素：", list_demo[-3])

"""
    （2）根据切片访问多个元素
        切片[start:end:step]
            step默认值是1
        当step为正数时，从左往右取元素，start和end可以是正索引值，也可以是负索引值。
            start默认值是0,end默认值len(列表)
        当step为负数时，从右往左取元素，start和end可以是正索引值，也可以是负索引值
            start默认值是-1,end默认值-len(列表)-1
        end索引对应的元素不包含
        
    列表的长度：len(列表)
"""
# list_demo = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("访问一组元素：", list_demo[3:7])
# print("访问一组元素：", list_demo[3:-3])
# print("访问一组元素：", list_demo[3:-3:2])

# print("访问一组元素：" ,list_demo[7:3:-1])
# print("访问一组元素：" ,list_demo[-3:3:-1])
# print("访问一组元素：" ,list_demo[-3:3:-2])

# print("访问一组元素：" ,list_demo[:3]) #等价于[0:3:1]
# print("访问一组元素：" ,list_demo[:]) #等价于[0:len(列表):1]
# print("访问一组元素：" ,list_demo[3:]) #等价于[3:len(列表):1]

# print("访问一组元素：", list_demo[::-1]) #等价于[-1:-len(列表)-1:-1]
# print("访问一组元素：", list_demo[:5:-1]) #等价于[-1:5:-1]

"""
    （3）查询元素的索引
     序列.index(元素) 返回的是索引值，而且是正索引：0,1,2,...,元素总个数-1
"""
# list_demo = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# print("元素50的索引值是多少？", list_demo.index(50))
# print("元素150的索引值是多少？", list_demo.index(150)) #报错

"""
    （4）序列的相加
"""
# one = [1,2,3]
# two = [4,5,6]
# three = one + two
# print(f"{three=}")
# print(f"{one=}")
# print(f"{two=}")

# one = [1,2,3]
# two = [4,5,6]
# one += two
# print(f"{one=}")
# print(f"{two=}")

"""
    （5）序列乘法
    序列 * n
"""
# one = [1,2,3]
# two = one * 3
# print(two) #重复one 3遍

# print("=" * 20)

"""
    （6）对序列的元素进行统计分析
    sum(序列)
    max(序列)
    min(序列)
    序列.count(目标)，看目标重复几遍
    len(序列)
"""
# list_demo = [1, 5, 3, 4, 5, 3, 5, 4]
# print("元素累加和：", sum(list_demo))
# print("元素最大值：", max(list_demo))
# print("元素最小值：", min(list_demo))
# print("4重复的次数：", list_demo.count(4))
# print("元素总个数：", len(list_demo))

"""
    （7）遍历序列
    语法形式一：
        for 元素 in 序列:
            语句
            
    语法形式二：
        for 索引变量 in range(索引范围):
            语句
            
    语法形式三：
        for 索引变量,元素 in enumerate(序列):
            语句
    
"""
list_demo = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#遍历所有元素
# for i in list_demo: #此时i是代表列表中的元素
#     print(i)

# for i in range(len(list_demo)): #i的取值范围[0, len(list_demo)-1]，这里的i是索引值
#     print(f"第{i + 1}个元素是{list_demo[i]}")

# for index, element in enumerate(list_demo):
#     print(f"索引:{index}，元素是{element}")

#遍历部分元素
# for i in range(2,7):
#     print(list_demo[i])

#倒序遍历
for i in range(-1,-len(list_demo)-1,-1):
    print(list_demo[i])
