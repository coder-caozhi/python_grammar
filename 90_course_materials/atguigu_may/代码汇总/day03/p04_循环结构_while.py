"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    1、while循环的语法格式：
    while ①条件表达式:  #凡是条件表达式，就表示这里需要布尔结果，True或False，当然python中，非0非0被看成True，0和空被看成False
        ②需要重复的语句块
        
    执行过程：①成立->②->①成立->②->....①不成立
    
    2、while循环的语法格式2：
    while ①条件表达式: 
        ②需要重复的语句块
    else:
        当while循环条件不成立时，执行的语句
    
    3、for循环和while循环的对比
    for循环和while循环都能实现“重复”执行某些语句的功能。
    但是对于遍历字符串、列表等可迭代对象来说，for更合适。
    对于循环次数不是很明显，只知道循环条件的情况下，while更合适。
"""
#输出5次我爱尚硅谷
# for i in range(5): #for循环是一个语法糖，它本质上底层是一个迭代器，内部会有 i = xx 赋值语句
#     print("我❤️尚硅谷")

# count = 1
# while count<=5:
#     print(f"我爱尚硅谷{count}")
#     count += 1
# else:
#     print(f"循环结束后{count=}")

#计算 1 到 100 的和
# num = 1
# total = 0
# while num<=100:
#     total += num
#     num += 1
# print(f"1 到 100 的和{total}")

#统计列表中大于 30 的数的个数
# scores = [25, 42, 19, 66, 31, 15]
# index = 0 #index称为索引/下标/编号
# count = 0
# while index<len(scores):
#     if scores[index]>30:
#         count += 1
#     index += 1
# print(f"大于30的个数：{count}")


