"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
1. 列表操作
    1. 创建一个列表 nums = [1,2,3,4,5]，在列表末尾添加数字 6，在开头插入数字 0。
    2. 列表 lst = [10,20,30,20,40,20]，删除列表中第一个 20。
    3. 计算列表 scores = [88,92,76,90,85] 的总和和平均值。
    4. 反转列表 lst = [1,2,3,4]（直接修改原列表）。
    5. 列表 fruits = ["apple","banana","orange"]，判断 "apple" 是否在列表中。
"""
# nums = [1, 2, 3, 4, 5]
# print(f"原列表：{nums}")
# nums.append(6)
# print(f"末尾追加6之后：{nums}")
# nums.insert(0,0)
# print(f"在开头插入0之后：{nums}")

# lst = [10,20,30,20,40,20]
# print(f"原列表：{lst}")
# lst.remove(20)
# print(f"删除第1个20之后：{lst}")

# scores = [88,92,76,90,85]
# print(f"成绩：{scores}")
# total = sum(scores)
# avg = total / len(scores)
# print(f"总分：{total}，平均分：{avg}")

# lst = [1,2,3,4]
# print(f"原列表：{lst}")
# lst.reverse()
# print(f"反转之后：{lst}")

# fruits = ["apple","banana","orange"]
# print("apple是否在列表中：", "存在" if "apple" in fruits else "不存在")


"""
2. 集合操作
    1. 创建集合 s1 = {1,2,3,4} 和 s2 = {3,4,5,6}，求两个集合的交集。
    2. 向集合 s = {1,2} 中添加元素 3，删除元素 1。
    3. 判断集合 a = {1,2} 是否是集合 b = {1,2,3} 的子集。
    4. 有两个列表 lst1 = [1,2,3,4]、lst2 = [3,4,5,6]，找出两个列表中都存在的元素。
    5. 去除列表 lst = [5,2,5,1,2,1,3] 中的重复元素，并从小到大排序。
"""
# s1 = {1, 2, 3, 4}
# s2 = {3, 4, 5, 6}
# print(f"集合1:{s1}")
# print(f"集合2:{s2}")
# print(f"交集：{s1 & s2}")
# print(f"交集：{s1.intersection(s2)}")
# s1.intersection_update(s2)
# print(f"交集：{s1}")

# s = {1, 2}
# print(f"原集合：{s}")
# s.add(3)
# print(f"添加3之后：{s}")
# s.remove(1)
# print(f"删除1之后：{s}")

# a = {1, 2}
# b = {1, 2, 3}
# print(f"集合1:{a}")
# print(f"集合2:{b}")
# print(f"集合1是集合2的子集吗？{a.issubset(b)}")
# print(f"集合1是集合2的子集吗？{ a <= b}")
# print(f"集合1是集合2的子集吗？{a==a&b}")

# lst1 = [1, 2, 3, 4]
# lst2 = [3, 4, 5, 6]
# print(f"集合1:{lst1}")
# print(f"集合2:{lst2}")
# # lst3 = list(set(lst1)  & set(lst2))
# lst3 = []
# for item in lst1:
#     if item in lst2:
#         lst3.append(item)
# print("两个列表中相同的元素：", lst3)

# lst = [5,2,5,1,2,1,3,11,15,34,22]
# lst = list(set(lst))
# lst.sort()
# print(f"去重重复元素和排序后：{lst}")

"""
3. 字符串操作
    1. 定义字符串 s = "Hello Python 123"，统计字符串中字母的个数。
    2. 给定字符串 name = "  python learner  "，去除首尾空格，并将所有字母转为大写。
    3. 截取字符串 s = "abcdefg"，输出第 3 个到第 6 个字符（包含两端）。
    4. 判断字符串 tel = "13800138000" 是否全部由数字组成。
    5. 将字符串 words = "python-java-c++" 按照 - 分割，得到列表。
"""
# s = "Hello Python 123"
#方式一：后面学习了正则之后，可以将非字母的快速去掉，然后统计剩余的字符个数
#方式二：循环判断
# letter_count = 0
# for item in s.lower():
#     # if 'a' <= item <= 'z':
#     if item.isalpha() and item.isascii():
#         letter_count += 1
# print(f"字母的个数：{letter_count}")

# name = "  python learner  "
# name = name.strip().upper()
# print(f"去除首尾空格并且转为大写：{name}")

# s = "abcdefg"
# print(f"原字符串：{s}")
# print(f"截取第3个到第6个字符：{s[2:6]}")

# tel = "13800138000"
# print("tel:", tel)
# print(f"是否全部由数字组成：{tel.isdigit()}")
# flag = True
# for s in tel:
#     if not '0' <= s <= '9':
#         flag = False
#         print("不是全部由数字组成")
#         break
# else: #如果中途break出循环，不执行else
#     print("全部由数字组成")

words = "python-java-c++"
print(f"原字符串:{words}")
words_list = words.split("-")
print(f"按照-拆分后的列表：{words_list}")
