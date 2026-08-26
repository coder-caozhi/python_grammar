# 切片的语法：list[开始:结束:步长]
# 创建一个列表
my_list = [1,2,3,4,5,6,7,8,9,10]
#取索引为1到4的位置的元素放到一个新列表中（左闭右开）
my_list2 = my_list[1:5]
print(my_list2)
# 获取所有元素
my_list3 = my_list[::]
print(my_list3)
# 反向获取元素
my_list4 = my_list[::-1]
print(my_list4)
# 隔一个取一个
my_list5 = my_list[::2]
print(my_list5)
# 反向隔一个取一个
my_list6 = my_list[::-2]
print(my_list6)