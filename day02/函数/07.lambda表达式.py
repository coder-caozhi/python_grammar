# 定义一个列表
my_list = [1,2,-3,4,-5]

# 在map函数中使用Lambda表达式
my_list2 = list(map(lambda a: a**2,my_list))
print(my_list2)

# 在filter函数中使用Lambda表达式
my_list3 = list(filter(lambda x: x % 2 == 0, my_list))
print(my_list3)

# sort函数：对列表直接排序，没有返回值
my_list.sort()
# sorted函数：对列表排序之后返回一个新的列表
my_list4 = sorted(my_list,reverse=True)
print(my_list4)

# 在sorted函数中使用Lambda表达式
my_list5 = sorted(my_list,key=lambda x:abs(x),reverse=True)
print(my_list5)