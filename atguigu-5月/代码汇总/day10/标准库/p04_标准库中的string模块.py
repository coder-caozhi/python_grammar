"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import string

# 常用字符串常量
# print(string.ascii_letters)  # 所有大小写字母
# print(string.ascii_lowercase)  # 所有小写字母
# print(string.ascii_uppercase)  # 所有大写字母
# print(string.digits)         # 数字0-9
# print(string.punctuation)    # 标点符号
# print(string.whitespace)    # 空白符号

# #需求：请输入一段文本，然后将这段文件中的所有标点符号、空白符去掉
# sentence = input("请输入一段文本：") #I'm a girl. I'm beautiful.
# # for s in string.punctuation: #去掉标点符号的方式一
# #     sentence = sentence.replace(s,"")
#
# table = str.maketrans("","",string.punctuation + string.whitespace)
# sentence = sentence.translate(table)
# print(sentence)

#需求：输出所有小写字母及其对应的编码值
for c in string.ascii_lowercase:
    print(c,"=>", ord(c))
