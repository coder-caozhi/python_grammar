"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
import heapq

"""
    1、几个好用的内置函数
    内置：不需要import就可以
    sorted：给各种序列排序。（序列：有序的可迭代的容器对象，例如：列表等）。返回新的序列。
    filter：过滤筛选
    map：映射转换
"""
#案例1：
# list_demo = [8, 9, 7, 5, 6, 2]
# list_demo_sorted= sorted(list_demo) #因为sorted内部不是针对list_demo直接排序的，而是创建了一个新的列表存储排好序的元素，且返回新列表
# print("排序后旧列表：", list_demo)
# print("排序后新列表：", list_demo_sorted)
#
# list_demo_sorted= sorted(list_demo, reverse=True)
# print("降序排序后新列表：", list_demo_sorted)

#案例2：
# list_demo = ["hello", "hi", "chai", "atguigu", "python", "尚硅谷"]
# # 按照字符串的长短排序，从短到长
# # list_demo_sorted= sorted(list_demo) #默认按照字符的Unicode编码值排序
# list_demo_sorted = sorted(list_demo, key=len)  # key参数接收了一个函数 ,len()，该函数用于对序列中每一个元素求长度
# print("排序后旧列表：", list_demo)
# print("排序后新列表：", list_demo_sorted)

#案例3：
# list_demo = [8, 9, 7, 5, 6, 2]
# # 筛选出所有的偶数
# # 如何查看一个函数的参数列表（1）调用函数时，把光标放到()中，按快捷键Ctrl + P
# result = filter(lambda x: x % 2 == 0, list_demo)
# # print(result) #<filter object at 0x000001A0DF055A80> 得到的是一个filter类型的对象
# print(list(result)) #把filter的对象转为list类型

#案例4：
# list_demo = ["hello", "hi", "chai", "atguigu", "python", "尚硅谷"]
# #筛选出包含a字母的单词
# result = filter(lambda x: 'a' in x ,list_demo)
# print(list(result))
#这里要基于过滤功能的上下文，这里是对列表等序列中的元素做过滤，所以匿名函数的参数用于接收每一个元素，
# 该匿名函数的返回值是True或False,当元素满足xx条件时，返回True表示需要留下该元素，不满足条件返回False,表示去掉该元素

#案例5：
#请输入3个整数值
#input("请输入3个整数：").split()得到一个列表，列表的元素是输入的多个字符串
#int这里代表函数 int()
# a,b,c = map(int ,input("请输入3个整数：").split())
# print(a,b,c)

#案例6：
# #对list_demo = ["hello", "hi", "chai", "atguigu", "python", "尚硅谷"]求每一个单词的长度
# list_demo = ["hello", "hi", "chai", "atguigu", "python", "尚硅谷"]
# result = map(len,list_demo) #将len函数应用到list_demo的每一个元素上，len函数的结果是最后列表中的每一个元素
# # print(result) #<map object at 0x000002ABE3803040>
# print(list(result))

"""
    2、几个好用的标准库中函数
    标准库中：需要import，但是不需要再单独下载安装
    functools.reduce：对可迭代对象进行累积计算
        reduce(lambda a,b: 表达式 , 可迭代对象)：
            第一次计算,a,b分别是第1个元素和第2个元素
            第二次计算，a代表上一次的计算结果，b代表第3个元素
            第三次计算，a代表上一次的计算结果，b代表第4个元素
            ...
        reduce(lambda a,b: 表达式 , 可迭代对象,初始值)
            第一次计算,a,b分别是初始值和第1个元素
            第二次计算，a代表上一次的计算结果，b代表第2个元素
            第三次计算，a代表上一次的计算结果，b代表第3个元素
            ...
        
    heapq.nlargest：找出可迭代对象中最大的 n 个元素
    heapq.nsmallest：找出可迭代对象中最小的 n 个元素
"""
import functools
# #案例7：
# list_demo = [8, 9, 7, 5, 6, 2]
# #求元素总和
# print("元素总和：",sum(list_demo))
# print("元素总和：", functools.reduce(lambda a,b: a+b, list_demo))
# #这里要对list_demo中的元素求累加和，  需要两个值相加，如a+b，所以这里的匿名函数需要2个参数
"""
    [8, 9, 7, 5, 6, 2]
    第一次计算：8,9赋值给a,b，求a+b，得到17
    第二次计算：用刚才的17和下一个元素7赋值给a,b，求a+b，得到24
    ...
    最终实现求和
"""
#案例8
# list_demo = [("张三",26000),("李四",20000),("王五",25666)]
# #求他们的薪资总和
# # print("薪资总和：", functools.reduce(lambda a,b: a[1]+b[1], list_demo))
# """
#     [("张三",26000),("李四",20000),("王五",25666)]
#     第一次计算：("张三",26000),("李四",20000)分别赋值给a,b，求a[1]和b[1]得到 26000 + 20000 = 46000
#     第二次计算：把刚才的46000和下一个元素("王五",25666)赋值给a,b，求a[1]和b[1]，此时46000是int类型，不能进行a[1]计算
# """
# print("薪资总和：", functools.reduce(lambda a,b: a+b[1], list_demo,0)) #这里的0是代表initial，初始值
# """
#     [("张三",26000),("李四",20000),("王五",25666)]
#     第一次计算：初始值,("张三",26000)分别赋值给a,b，求a和b[1]得到 0 + 26000 = 26000
#     第二次计算：把刚才的26000和下一个元素("李四",20000)赋值给a,b，求a和b[1]，得到46000
#     。。。
# """

#案例9
list_demo = [{"name":"张三","salary":26000},{"name":"李四","salary":20000},{"name":"王五","salary":25666}]
print("薪资总和：", functools.reduce(lambda a,b: a +b["salary"], list_demo,0)) #这里的0是代表initial，初始值


#案例10
# list_demo = [8, 9, 7, 5, 6, 12]
list_demo = [8, 9, 12, 12, 12, 13]
#找出最大的3个元素
biggest_three = heapq.nlargest(3,list_demo)
print(biggest_three)

#案例11
list_demo = [("张三",26000),("李四",20000),("王五",25666),("赵六",23000)]
#找出薪资最高的前2个
# result = heapq.nlargest(2,list_demo) #当元素是复杂对象时，按照索引比较大小
result = heapq.nlargest(2,list_demo,key=lambda x:x[1])  #key接收一个函数对元素做处理，取出元素的薪资来比较大小
print(result)

"""
    3、第三方库的函数：需要单独下载安装，且需要import（今天先不涉及）
"""
