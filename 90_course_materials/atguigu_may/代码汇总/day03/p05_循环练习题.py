"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
练习题8：统计正负数个数
从键盘不断输入整数，统计输入的正整数、负整数的个数，输入0循环结束。

思考：
（1）循环条件是什么
（2）哪些语句需要重复，即哪些需要需要放到循环体语句中
（3）有几个变量，即有几个数据
"""
# num = 1 #任何非0的值都可以
# positive = 0
# negative = 0
# while num:
#     num = int(input("请输入1个整数："))
#     if num > 0:
#         positive += 1
#     elif num < 0:
#         negative += 1
# print(f"正数：{positive}，负数：{negative}")

"""
练习题9：猜数
    先随机产生1个[1,100]范围的整数，提示 random.randint(a,b)产生[a,b]范围的整数。
    从键盘输入数字num，猜随机产生的数是多少。例如：随机数是45
    如果猜大了，提示大了。例如输入50，提示大了，范围在[1,50]之间,
    如果猜小了，提示小了。例如输入25，提示小了，范围在[25,50]之间,
    不断缩小范围。总共只能猜7次，如果猜中了，就恭喜，7次未猜中，就公布答案。
    
思考：
（1）循环条件是什么
    猜的次数未超过7次，以及未猜中
（2）哪些语句需要重复，即哪些需要需要放到循环体语句中
    输入猜的数字，判断数字是不是大了、小了、对了
    猜的次数的累加
（3）有几个变量，即有几个数据  

"""
import random
rand_num = random.randint(1,100) #随机产生[1,100]的整数
count = 1 # 猜的次数
flag = False #False代表还没猜中

left  = 1
right = 100

while count<=7 and flag == False:
    num = int(input("请输入一个[1,100]的整数："))
    count += 1 #猜一次，猜的次数就加1
    if num == rand_num:
        print("恭喜你，猜对了")
        flag = True #True代表猜中了
    elif num > rand_num:
        right = num if num < right else right
        print(f"猜大了，范围：[{left},{right}]")
    else:
        left = num if num > left else left
        print(f"猜小了，范围：[{left},{right}]")

if count > 7:
    print(f"7次未猜中，答案是{rand_num}")