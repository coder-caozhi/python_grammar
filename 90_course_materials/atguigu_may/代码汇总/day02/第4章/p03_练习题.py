"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
"""
# 从键盘输入3个整数，按照从小到大输出
# 例如：输入5,6,4   输出4,5,6
# 输入3个整数的方式一
a = int(input("请输入第1个整数："))
b = int(input("请输入第2个整数："))
c = int(input("请输入第3个整数："))

# 输入3个整数的方式二，需要使用超纲的知识点
# split()是一个函数，将一个字符串，例如:“4 5 6”，按照空格拆分为3个字符串["4","5","6"]
# map是一个函数，映射函数，把int函数映射到每一个元素上，即对"4"做int("4")， “5”做 int("5")  “6”做 int("6")
# a,b,c = map(int,input("请输入3个整数：").split())
# print(a,b,c)

# 排序输出的方式有如下几种：
# 方式一
# biggest = a if a > b else b
# biggest = biggest if biggest > c else c
# smallest = a if a < b else b
# smallest = smallest if smallest < c else c
# middle = a + b + c - biggest - smallest
# print(smallest, middle, biggest)

#方式二：冒泡排序
#比较相邻的元素，如果前面的元素比后面的元素大，就交换它们
#3个元素需要比较2轮
"""
    6,4,5
    第一轮：
        第一次：6>4成立，交换  4,6,5
        第二次：6>5成立，交换  4,5,6   只能保证最大的到末尾
    第二轮：
        第一次：4>5不成立，不交换
        
    6,5,4
    第一轮：
        第一次：6>5成立，交换  5,6,4
        第二次：6>4成立，交换  5,4,6
    第二轮：
        第一次：5>4成立，交换  4,5,6
"""
# if a>b:
#     a,b=b,a
# if b>c:
#     b,c=c,b
# if a>b:
#     a,b=b,a
# print(a,b,c)

#方式三：穷举法
# if a<b<c:
#     print(a,b,c)
# elif a<c<b:
#     print(a,c,b)
# elif b<a<c:
#     print(b,a,c)
# elif b<c<a:
#     print(b,c,a)
# elif c<a<b:
#     print(c,a,b)
# else:
#     print(c,b,a)

#方式四：两个比较法
if a<b:
    if c<a:
        print(c,a,b)
    elif b<c:
        print(a,b,c)
    else:
        print(a,c,b)
else: #b<=a
    if c<b:
        print(c,b,a)
    elif a<c:
        print(b,a,c)
    else:
        print(b,c,a)

