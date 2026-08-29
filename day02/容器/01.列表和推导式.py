my_list = [1,2,3,4,5,6]
my_list2 = [7,8,9]
# 获取长度
print(len(my_list))

# 求和
print(sum(my_list))
# 求最大值
print(max(my_list))
# 求最小值
print(min(my_list))
# 列表加法
my_list3 = my_list + my_list2
print(my_list3)
# 列表的乘法
my_list4 = my_list2 * 2
print(my_list4)

# 推导式（重要）
# 基本推导式
my_list5 = [x for x in range(1,11)]
print(my_list5)
# 带条件的推导：获取1-20中所有的偶数
my_list6 = [a for a in range(1,21) if a % 2 == 0]
print(my_list6)
# 嵌套推导
colors = ['♠', '♥', '♣', '♦']
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
my_list7 = [c + r for c in colors for r in ranks]
print(my_list7)
# 基于现有列表的推导：基于my_list获取其中所有的奇数
my_list8 = [x for x in my_list if x % 2 != 0]
print(my_list8)

