"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
import numbers

"""
练习题1：随机数列表
1. 定义一个包含 10 个随机整数（范围 1-100）的列表（可手动输入或用 random 模块）
2. 打印列表的长度、最大值、最小值、总和
3. 打印列表中索引为 5 的元素，以及最后 3 个元素（切片）
4. 统计列表中数字50出现的次数
5. 遍历列表，打印每个元素的索引和值（用 enumerate）
"""
# import random
# nums = [random.randint(1,100) for _ in range(10)]
# print("列表：", nums)
# print("列表的长度：", len(nums))
# print("列表的最大值：", max(nums))
# print("列表的最小值：", min(nums))
# print("列表的元素总和：", sum(nums))
# print("列表索引为5的元素：", nums[5])
# print("列表最后的3元素：", nums[-3:])
# print("50出现的次数：", nums.count(50))
# for i,num in enumerate(nums):
#     print(f"元素的索引：{i},元素值：{num}")

"""
练习题2：成绩分析
给定学生成绩列表 scores = [78, 92, 85, 69, 100, 88, 75, 92, 100, 85]，完成以下操作：
1. 计算班级的平均分（总和 / 人数），保留 1 位小数
2. 找出最高分和最低分，并打印 “最高分：XX，最低分：XX”
3. 检查是否有学生考了满分（100 分），有则打印 “有满分，满分有x个”，无则打印 “无满分”
4. 通过切片获取成绩列表中前 5 个分数，计算其平均分
5. 遍历成绩列表，打印 “第 X 个学生的成绩是：XX”（X 从 1 开始）
"""
# scores = [78, 92, 85, 69, 100, 88, 75, 92, 100, 85]
# print("成绩列表：",scores)
# print("成绩的平均分：", round(sum(scores) / len(scores),1))
# print(f"成绩最高分:{max(scores)}，最低分：{min(scores)}")
# count100 = scores.count(100)
# if count100 > 0:
#     print(f"有满分，满分有{count100}个")
# else:
#     print(f"无满分")
# before5 = scores[:5]
# print(f"前5个的学生分数：{before5}，平均分：{round(sum(before5)/5,1)}")
# for i,score in enumerate(scores):
#     print(f"第{i+1}个学生的成绩是：{score}")

"""
练习题3：列表
1）给定一个列表 numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]，编写一个程序，将列表中所有的偶数元素删除
"""
# 方式一：
# numbers = [1, 2, 4, 4, 6, 6, 7, 8, 9, 10]
# i = 0
# while i<len(numbers):
#     if numbers[i]%2==0:
#         del numbers[i]
#     else:
#         i+=1
# print(numbers)

# 方式二：
# numbers = [1, 2, 4, 4, 6, 6, 7, 8, 9, 10]
# # odds = [i for i in numbers if i%2]#i%2非0表示条件成立
# odds = [i for i in numbers if i%2!=0]
# print(odds)

"""
练习题4：列表
2）创建一个空列表 fruits，然后添加 "apple", "banana", "cherry", "date" 四个元素。
接着在列表的开始添加 "elderberry"，在 "cherry" 之前添加 "fig"，并将列表的最后一个元素替换为 "grape"。
"""
# fruits = []
# fruits.append("apple")
# fruits.append("banana")
# fruits.append("cherry")
# fruits.append("date")
# print("fruits:", fruits)
#
# fruits.insert(0,"elderberry")
# fruits.insert(fruits.index("cherry"), "fig")
# fruits[-1] = "grape"
# print("fruits:", fruits)


"""
练习题5：列表
3）给定一个列表 prices = [10.5, 20.0, 15.75, 8.2, 12.0]，
编写一个程序，将列表中的元素都乘以 1.1（表示增加 10%），并将结果存储在一个新列表 new_prices 中。
"""
# prices = [10.5, 20.0, 15.75, 8.2, 12.0]
# print("原价格：", prices)
# new_prices = [round(p * 1.1, 2) for p in prices]
# print("新价格：", new_prices)

"""
练习题6：列表
4）有两个列表 list1 = [1, 2, 3, 4, 5] 和 list2 = [6, 7, 8, 9, 10]，将它们合并为一个新列表 combined_list，并对 combined_list 进行降序排序
"""
# list1 = [1, 2, 3, 4, 5]
# list2 = [6, 7, 8, 9, 10]
# combined_list = list1 + list2
# combined_list.sort(reverse=True)
# print(combined_list)

"""
练习题7：列表
从控制台输入一句话，包含中英文等多种字符，然后将里面的英文字母筛选出来构成一个新列表（使用列表推导式）
"""
# sentence = input("请输入一句话：")
# print(sentence)
# #
# # letters = [s for s in sentence if 'a'<=s<='z' or 'A'<=s<='Z']
# # # letters = [s for s in sentence if s.isalpha()] # isalpha()包含字母、中文等
# letters = [s for s in sentence if s.isalpha() and s.isascii()]
# print(letters)

"""
练习题8：列表
从控制台输入一组单词放到列表中，直到输入exit（不放到列表）结束，统计最长的字符串
"""
# words = []
# while True:
#     word = input("请输入单词：")
#     if word == "exit":
#         break
#     words.append(word)
# print("所有单词：",words)
# print("最长的单词：", max(words,key=len)) #len是一个函数，用于求字符串的长度

# max_length_word = ""
# for word in words:
#     if len(word) > len(max_length_word):
#         max_length_word = word
# print("最长的单词：", max_length_word)

