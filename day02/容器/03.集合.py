"""
    集合
        特点：
            无序、可变、不可重复、值类型不限
        创建方式：
            1.使用大括号{}，注意：空集合不能使用{}，使用{}创建的是空字典，需要使用set()创建空集合
            2.使用set函数
        获取元素的方式：
            遍历
"""
# 使用{}创建集合
my_set = {1,1,2,3,4}
print(my_set)
print(type(my_set))
# 不能使用{}创建空集合，创建的是空字典，需要是set()函数才能创建空集合
# my_empty_set = {}
my_empty_set = set()
print(my_empty_set)
print(type(my_empty_set))
# 使用set()函数创建集合
my_set2 = set([5,5,6,6,7,8,9])
print(my_set2)
print(type(my_set2))

# 常用的函数
# 向集合中添加元素
my_set.add(5)
print(my_set)
# 向集合中添加多个元素
my_set.update([6,6,7,7])
print(my_set)
# 随机吐出一个元素
print(my_set.pop())
print(my_set)
# 删除一个存在的元素
# my_set.remove(4)
# 删除一个不存在的元素，报错：KeyError: 8
# my_set.remove(8)
# 使用discard函数删除一个不存在的元素不会报错
my_set.discard(8)
print(my_set)
# 清空集合
my_set.clear()
print(my_set)

print("*"*30)

my_set3 = {1,2,3,4,5}
my_set4= {2,3,4,5,6}
# 取交集
print(my_set3 & my_set4)
# 取并集
print(my_set3 | my_set4)
# 取差集
print(my_set3 - my_set4)
print(my_set4 - my_set3)
# 取对称差集
print(my_set3 ^ my_set4)
print(my_set4 ^ my_set3)

