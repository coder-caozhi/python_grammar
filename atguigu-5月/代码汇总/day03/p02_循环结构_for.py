"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    1、python中的循环结构有2种：
    （1）for
    （2）while
    循环结构的最根本的特点：重复执行某些语句
    
    2、for循环
    这里的for循环类似于其他语言中的foreach循环。
    这里的for循环作用是遍历/迭代某个容器（可迭代对象）的元素
    
    遍历：挨个查看容器中的元素
    迭代：重复，重复的次数由元素的个数决定
    
    python中的容器：字符串str,列表list等
    
    3、for循环的语法格式
    for 元素变量名 in 容器/可迭代对象:
        对元素做xx操作的语句
"""
# for s in "hello": #s是自己取的一个变量名，它会在每一次循环时，依次代表容器中的元素
#     print(s)

# for i in [10,20,30]: #[]代表列表
#     print(i)

"""
    range函数可以生成一组数
    range(start, stop, step)：
        start代表起始值，如果没有指定，默认从0开始
        stop代表结束值（不包含），必须指定
        step代表步长，如果没有指定，默认步长是1
"""
# for i in range(5): #range(5)产生[0,1,2,3,4]
#     print(i)

# for i in range(5, 10): #range(5,10)产生[5,6,7,8,9]
#     print(i)

# for i in range(1, 10, 2): #range(1,10,2)产生[1,3,5,7,9]
#     print(i)

# for i in range(15, 10): # 没有数据， 如果step是正数，start<stop
#     print(i)

for i in range(15, 10, -2): #从大到小，如果step是负数，start>stop
    print(i)