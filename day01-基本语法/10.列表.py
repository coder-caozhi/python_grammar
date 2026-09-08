"""
    列表：
        创建方式：
            1、直接使用[]
            2、使用list()
        特点：
            有序、可变、可重复、值类型不限
        访问方式：
            1.使用下标
            2.遍历
"""
# 使用[]创建一个列表
my_list = [1,"hello",True,8.88,["hello","蔡徐坤"]]
print(my_list)
# 获取my_list中的蔡徐坤
print(my_list[4][1])
# 使用list函数创建一个列表，里面的元素是1，3，5，7，9
my_list2 = list(range(1,10,2))
print(id(my_list2))
print(my_list2)

# 修改my_list2中下标为1的位置的值
my_list2[1] = 5
print(my_list2)
print(id(my_list2))

print("="*30)

# 测试常用的函数
# 在列表最后添加元素
my_list2.append(5)
print(my_list2)
# 在列表最后添加多个元素
my_list2.extend([1,2,3])
print(my_list2)
# 在执行的索引位置插入元素，索引从0开始
my_list2.insert(1,"hello")
print(my_list2)
# 吐出指定索引位置的元素，不指定索引吐出最后一个
my_list2.pop(1)
print(my_list2)
# 删除第一个出现的元素
my_list2.remove(5)
print(my_list2)
# 获取元素的索引
print(my_list2.index(7))
# 升序排序
# my_list2.sort()
# 降序排序
# my_list2.sort(reverse=True)
# 反转前打印列表
print(f"反转前的列表是：{my_list2}")
# 反转
my_list2.reverse()
print(f"反转后的列表是：{my_list2}")
