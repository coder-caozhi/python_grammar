# 赋值
import copy

a = b = 10
print(id(a))
print(id(b))

# 浅拷贝
my_list = [1,[2,3]]
# 调用copy函数复制一个对象
my_list2 = my_list.copy()
# 分别打印
print(my_list)
print(my_list2)
print(id(my_list))
print(id(my_list2))
# 修改my_list索引为0的值
# my_list[0] = 10 # my_list会变，my_list2不变
# 修改my_list索引为1的列表中索引为0的位置的值
my_list[1][0] = 200
print(my_list)
print(my_list2)

print("="*30)
# 深拷贝
my_list3 = copy.deepcopy(my_list)
print(my_list)
print(my_list3)
# 修改my_list索引为1的列表中索引为0的位置的值
my_list[1][0] = 300
print(my_list)
print(my_list3)