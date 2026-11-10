"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    关键字：break
    作用：提前结束循环，中途结束循环
"""
# 请输入一个大于1的自然数
# while True:
#     num = int(input("请输入1个大于1的自然数："))
#     if num > 1:
#         break
# print(f"{num=}")


#重新完成猜数练习题
import random
rand_num = random.randint(1,100) #随机产生[1,100]的整数
count = 1 # 猜的次数
left  = 1
right = 100

while count<=7:
    num = int(input("请输入一个[1,100]的整数："))
    count += 1 #猜一次，猜的次数就加1
    if num == rand_num:
        print("恭喜你，猜对了")
        break
    elif num > rand_num:
        right = num if num < right else right
        print(f"猜大了，范围：[{left},{right}]")
    else:
        left = num if num > left else left
        print(f"猜小了，范围：[{left},{right}]")
else: #当while count<=7不成立时执行。如果中途break出来，else不执行
    print(f"7次未猜中，答案是{rand_num}")