"""
    元组
        特点：
            有序、不可变、可重复、值类型不限
        创建方式：
            1.使用小括号()，注意：如果元组中只有一个元素，元素后面得加逗号（,）
            2.使用tuple函数
        获取元素的方式：
            1.使用索引下标
            2.遍历
            3.使用enumerate函数
"""
# 使用()创建元组
my_tuple = (1,2,3)
print(type(my_tuple))
# 使用tuple函数创建元组
my_tuple2 = tuple("hello")
print(my_tuple2)
print(type(my_tuple2))
# 声明一个只有一个元素的元组，元素后面必须加逗号，否则不是一个元组
my_tuple3 = (8,)
print(my_tuple3)
print(type(my_tuple3))

# 通过索引获取元素值
print(my_tuple[0])
# 通过循环遍历每个元素
for a in my_tuple:
    print(a)
# 使用enumerate函数获取索引和元素
for i,x in enumerate(my_tuple):
    print(f"元素的索引是：{i}，元素值是：{x}")

# 获取元素的索引
print(my_tuple.index(3))
# 获取元素在元组中出现的次数
print(my_tuple2.count("h"))
# 获取元组的长度
print(len(my_tuple))
# 元组相加
print(my_tuple + my_tuple2)
# 元组的乘法
print(my_tuple * 3)
# 求和
print(sum(my_tuple))
