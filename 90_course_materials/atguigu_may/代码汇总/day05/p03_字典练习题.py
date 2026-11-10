"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
给定字符串 "Atguigu is a Good place"统计出现次数最多的字母，Aa不区分
最终用一个字典来表示每一个字母的次数，key为字母，value为次数。
"""
# s = "Atguigu is a Good place uu"
# letter_count = {}
# s = s.lower() #全部转为小写
# s = s.replace(' ', '')  #替换所有空格为空字符串，相当于去掉空格
# print(s)
# for letter in s:
#     #分两种情况：（1）这个字母之前出现过了（2）这个字母首次出现
#     if letter in letter_count:
#         letter_count[letter] += 1
#     else:
#         letter_count[letter] = 1
# print(letter_count)
#
# # print("出现次数最多的字母：", max(letter_count, key=letter_count.get)) #get是一个函数，字典的函数，根据key获取value
# #这个只能找到1个，不能找出所有次数最多的字母
#
# max_count = 0
# max_count_letter = []
# for letter, count in letter_count.items():
#     if count > max_count: #当某个字母的次数比现在max_count还多
#         max_count = count #最多次数max_count更新为当前字母的次数
#         max_count_letter = [letter] #出现次数最多的字母的列表中 记录当前字母
#     elif count == max_count:#出现第二个字母次数与当前最多次数max_count一样
#         max_count_letter.append(letter)  #次数最多的字母的列表有追加当前字母
# print("出现次数最多的字母：",max_count_letter)

"""
给定一个字典 student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}，编写一个程序，
（1）增加一个新学生的成绩：Lily成绩60
（2）查看Alice成绩
（3）删除Bob的成绩信息
（4）将每个学生的分数增加 5 分，并将结果存储在一个新的字典 updated_scores 中。

"""
student_scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 88}
print(f"原成绩字典：{student_scores}")
student_scores["Lily"] = 60
print(f"新增Lily之后：{student_scores}")
print(f"查看Alice的成绩：{student_scores['Alice']}")
print(f"查看Lucy的成绩：{student_scores['Lucy'] if student_scores.get('Lucy') else "Lucy不在这个班"}")
student_scores.pop("Bob")
print(f"删除Bob之后：{student_scores}")
updated_scores  = {key:value+5 for key, value in student_scores.items()}
print(f"每个同学+5分后：{updated_scores}")