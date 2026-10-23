"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
"""
    1、列表的特点
    （1）有序
    （2）元素可重复
    （3）可变
    （4）代表的数据结构：动态数组
    2、什么数组？
        数组是代表一块连续的存储空间，元素之间是相邻的。每一个元素有索引/下标/编号。
        正向：0,1,2,3,。。。
        负向：.......-3,-2,-1
        
    数组分为2种概念：
    （1）静态数组：长度不可变
    （2）动态数组：看起来像是长度可变，本质上是对静态数组的一个包装，抽象。
    
    数组的优点：根据索引/下标访问效率极高，时间复杂度是O(1)
        缺点：需要扩容；非末尾位置插入和删除需要移动元素；要求必须是连续的存储空间，对内存空间的连续型要求比较高。
    
    3、创建列表
    （1）[元素1，元素2，元素3]
    （2）list(容器)
    （3）特殊的空列表：[] ,list()
    4、增删改查等操作
    （1）增加
    列表.append(元素)：末尾追加元素
    列表.insert(位置,元素)：在任意位置插入元素
   
"""
# list_one = [1, 2, 3]
# print(f"{list_one=}")
# list_two = list("hello")
# print(f"{list_two=}")
# list_three = []
# print(f"{list_three=}")
# list_four = list()
# print(f"{list_four=}")

# list_demo = [10,20,30]
# print(f"追加新元素之前：{list_demo=}，id={id(list_demo)}")
# print("末尾追加元素：", list_demo.append(40)) #None
"""
上面的语句为什么是None？
因为列表是可变的，list_demo.append(40) 函数会在list_demo的内部直接追加元素，不会返回新的列表对象（所以返回None），内部数组的扩容对程序员来说是屏蔽。
"""
# list_demo.append(40)
# print(f"追加新元素之后：{list_demo=}，id={id(list_demo)}")
#
# list_demo.insert(0,50)
# print(f"插入新元素之后：{list_demo=}，id={id(list_demo)}")
#
# list_demo.insert(2,60)
# print(f"插入新元素之后：{list_demo=}，id={id(list_demo)}")
#
# list_demo.insert(-10,70)
# print(f"插入新元素之后：{list_demo=}，id={id(list_demo)}")

"""
    （3）删除
    del 列表[索引]
    del 列表[切片]
    列表.remove(目标元素)
    列表.pop() 删除末尾元素
    列表.pop(索引)
    列表.clear()清空
"""
list_demo = [10, 20, 30, 40, 50, 60, 70, 90, 80, 90, 100, 90, 90]
# print(f"删除元素之前：{list_demo=}，id={id(list_demo)}")
# #方式一
# del list_demo[1]
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# #方式二
# del list_demo[1:4]
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# 方式三
list_demo.remove(90) #删除找到的第一个90
# list_demo.remove(900) #报错（元素必须存在）
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# 删除所有90？？？
# for item in list_demo:
#     if item == 90:
#         list_demo.remove(item)
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# 漏删：list_demo=[10, 20, 30, 40, 50, 60, 70, 80, 100, 90]

# while 90 in list_demo:
#     list_demo.remove(90)
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# 可以list_demo=[10, 20, 30, 40, 50, 60, 70, 80, 100]

# count90 = list_demo.count(90)
# i = 0
# while i < count90:
#     list_demo.remove(90)
#     i+=1
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# 可以list_demo=[10, 20, 30, 40, 50, 60, 70, 80, 100]

# i = 0
# while i<len(list_demo):
#     if list_demo[i]==90:
#         del list_demo[i]
#     else:
#         i+=1
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# list_demo=[10, 20, 30, 40, 50, 60, 70, 80, 100]

# print(len(list_demo))
## range(start,end,step)它是在一开始就创建好一个range的对象，一开始的start=-1,end=-14,step=-1
# end不变，但是list_demo的元素减少， -14就会出现越界
# for i in range(-1,-len(list_demo)-1,-1):
#     if i< -len(list_demo):
#         break
#     if list_demo[i]==90:
#         del list_demo[i]
#         i=i-1
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")#这个i不受我们控制

# #方式四
# list_demo.pop() #默认删除末尾元素
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
# list_demo.pop(5) #删除[5]位置的元素
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")
#
# #方式五
# list_demo.clear()
# print(f"删除元素之后：{list_demo=}，id={id(list_demo)}")

"""
    （4）修改
    列表[索引] = 新元素
    列表[切片] = [新元素们]
"""
# list_demo = [10, 20, 30, 40, 50, 60]
# print(f"修改元素之前：{list_demo=}，id={id(list_demo)}")
# # list_demo.__setitem__(1,100) # 列表的魔法方法（关于魔法方法，在面向对象部分再说）
# # print(f"修改元素之后：{list_demo=}，id={id(list_demo)}")
#
# list_demo[1] = 100
# print(f"修改元素之后：{list_demo=}，id={id(list_demo)}")
#
# # list_demo[2:4] = [200,300] #左边是代表2个位置，右边是2个元素
# # list_demo[2:4] = [200,300,400,500] #左边是代表2个位置，右边是4个元素
# list_demo[2:4] = [200] #左边是代表2个位置，右边是1个元素
# print(f"修改元素之后：{list_demo=}，id={id(list_demo)}")

"""
    （5）查询
    根据索引/下标访问1个元素：  列表[索引]
    根据访问切片多个元素：      列表[start:end:step] 
    查询某个元素的下标/索引： 列表.index(元素)
"""
# list_demo = [10, 20, 30, 40, 50, 60]
# print("查询40的位置：", list_demo.index(40))

"""
    5、列表的其他操作
    （1）排序
    列表.sort(reverse=True) #默认reverse=False表示升序，reverse=True表示降序。不会返回新列表。
    sorted(列表)：会返回一个新列表
 
"""
# list_demo = [70, 20, 10, 30, 90, 60]
# print(f"排序之前：{list_demo=}，id={id(list_demo)}")
# list_demo.sort()
# print(f"升序排列之后：{list_demo=}，id={id(list_demo)}")
# list_demo.sort(reverse=True)
# print(f"降序排列之后：{list_demo=}，id={id(list_demo)}")

# result = sorted(list_demo)
# print(f"升序排列之后：{list_demo=}，id={id(list_demo)}")
# print(f"新的排好序的列表：{result=}，id={id(result)}")
"""
   （2）反转
"""
# list_demo = [70, 20, 10, 30, 90, 60]
# print(f"反转之前：{list_demo=}，id={id(list_demo)}")
# list_demo.reverse() #内部实现原理：首尾对应位置交换 列表[i], 列表[len(列表)-1-i]  i的循环范围[0, len(列表)/2]
# print(f"反转之后：{list_demo=}，id={id(list_demo)}")

"""
    6、列表的嵌套
    元素仍然是列表
"""
# list_demo = [1,2, [3,4]] #
# print("元素个数：", len(list_demo))
# for item in list_demo:
#     print(item)

"""
    7、列表的推导式（很好用）
    列表的推导式是一个语法糖。
    语法糖（Syntactic Sugar）是编程语言中的一种特性，它指的是在不影响语言功能的前提下，为程序员提供更简洁、更易读的语法形式。语法糖本身并不增加语言的功能，而是让代码更容易编写和理解。语法糖的特点：
        - 简化代码：让复杂的操作用更简单的语法表达。
        - 提高可读性：使代码更接近自然语言或逻辑思维。
        - 不改变语义：语法糖只是对底层实现的封装，不会影响程序的实际行为。
    for循环，是后面要学习的迭代器的简化的写法。本质上底层依赖于迭代器。
    列表推导式，是我们之前讲的循环遍历列表的操作。

    列表推导式：[变量的表达式 for 变量 in 容器(或可迭代对象) if 条件]
    列表推导式：[变量的表达式 for 变量1 in 容器(或可迭代对象) if 条件1 for 变量2 in 容器(或可迭代对象) if 条件2]
"""
#需求：产生1个列表，列表的元素由[1,10]构成
# list_one = [i for i in range(1,11)]
# print(list_one)

"""
    list_one = [i for i in range(1,11)]底层的对应代码
    list_one = []
    for i in range(1,11):
        list_one.append(i)
"""

#需求：产生1个列表，列表的元素是[1,10]的偶数的平方
# list_two = [i**2 for i in range(1,11) if i%2==0]
# list_two = [i**2 for i in range(2,11,2)]
# print(list_two)

#需求：产生1个列表，列表的元素是[['a',97], ['b',,98], ['c',99],...]
# list_three = [[chr(i),i] for i in range(97,97+26)]
# print(list_three)

"""
    8、zip函数
    zip 函数用于将1个或多个可迭代对象打包成一个迭代器，将对应位置的元素组合成元组。
    可迭代对象：可以遍历的容器对象
    迭代器：用于遍历容器中的元素的工具或对象。
    
    两个列表长度不一致，以短的为主。
"""
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c','d']
# print(zip(list1, list2)) #<zip object at 0x000002886FC52940>
# z = zip(list1, list2)
# for i in z:
#     print(i)
"""
(1, 'a')  把list1[0]位置与list2[0]位置的元素打包成一个元组
(2, 'b')
(3, 'c')
"""
# print("===========")
# for i in z:
#     print(i)
"""
下面这个for循环没有结果，为什么？因为z是一个迭代器对象。它的作用是遍历 list1和list2的打包结果，它内部会有一个游标，从头到尾走一遍，到末尾结束了。
"""

result = zip(list1, list2)
one,two,three = result #解包， 会把result中的每一个元组，依次赋值给=左边的变量。左边的变量的数量与result中元组的数量必须一致
print(one)
print(two)
print(three)

