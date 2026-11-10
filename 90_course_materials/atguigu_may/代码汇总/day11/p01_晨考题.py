"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import re
import string
from collections import Counter,defaultdict

"""
编写一个函数，接收一个由数字组成的字符串（例如 "12345"），完成以下功能：
1. 将字符串中的每个字符转为整数，存入列表
2. 计算列表中所有数字的平均值（保留 2 位小数）
3. 计算列表中所有数字的几何平均数
4. 返回：平均值、几何平均数
"""
# def exam1(num_str):
#     nums = [int(s) for s in num_str]
#     avg = round(sum(nums)/len(nums),2)
#     result = 1
#     for num in nums:
#         result *= num
#     gm = result ** (1/len(nums))
#     return avg,gm
#
# avg,gm = exam1("12345")
# print(f"平均值：{avg},几何平均数：{gm}")

"""
给定一段英文文本（包含大小写、标点），完成：
1. 去掉所有标点符号
2. 全部转为小写
3. 按单词统计出现次数（使用 Counter）
4. 使用 defaultdict 统计首字母相同的单词列表
    "Hello world! Hello Python. Python is fun, fun fun. Wow!"
    单词频次： {'fun': 3, 'hello': 2, 'python': 2, 'world': 1, 'is': 1, 'wow': 1}
    首字母分组： {'w': ['wow', 'world'], 'i': ['is'], 'h': ['hello'], 'f': ['fun'], 'p': ['python']}
"""
# str_demo = "Hello world! Hello Python. Python is fun, fun fun. Wow!"
# #方式一：使用replace
# # for c in string.punctuation:
# #     str_demo = str_demo.replace(c, "")
# # print(str_demo)
#
# #方式二：使用sub
# # pattern = "[" + string.punctuation +"]"
# # str_demo=re.sub(pattern,"",str_demo)
# # print(str_demo)
#
# #方式三：使用maketrans
# table = str.maketrans("","",string.punctuation)
# str_demo = str_demo.translate(table)
# print("去掉标点符号：",str_demo)
#
# str_demo = str_demo.lower()
# print("转为小写",str_demo)
#
# words_list = str_demo.split()
# word_count = Counter(words_list)
# print("统计单词的次数：", word_count)
#
# first_letter_same_words_dict = defaultdict(list)
# words_list = set(words_list)
# for word in words_list:
#     first_letter_same_words_dict[word[0]].append(word)
# print("按照单词的首字母分类：", first_letter_same_words_dict)