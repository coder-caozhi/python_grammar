"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
"""
    （1）字符串的连接
    "分隔符".join(字符串)
"""
# list_demo = [1,2,3,4,5]
# s = str(list_demo)
# print(s) # "[1, 2, 3, 4, 5]"
# print(len(s))
# print("-".join(s))

# s = "hello"
# print("-".join(s)) #h-e-l-l-o

"""
    （2）拆分
    字符串.split()：按照空格等空白符拆分
    字符串.split(分隔符):按照指定的分隔符拆分
"""
# s = "hello world\tpython\nmysql"
# print(s.split())
# s = "hello,world,python"
# print(s.split(","))

#一次输入值
# words = input("请输入多个单词（空格分割）：").split()
# print(words)

#请输入多个整数
# nums = input("请输入多个整数（空格分割）：").split() #每一个元素都是字符串
# nums = [int(n) for n in input("请输入多个整数（空格分割）：").split()] #每一个元素都是int
# print(nums)
# print(sum(nums))

"""
    （3）去掉首或尾的部分
    字符串.strip() 或  字符串.strip("字符")
    字符串.lstrip() 或  字符串.lstrip("字符")
    字符串.rstrip() 或  字符串.rstrip("字符")
    字符串.removesuffix(后缀)
    字符串.removeprefix(前缀)
"""
# s = "****hello****world****"
# print("去掉开头和结尾的*：", s.strip("*"))
# print("去掉开头的*：", s.lstrip("*"))
# print("去掉结尾的*：", s.rstrip("*"))
#
# s = "     hello   world    "
# print("去掉开头和结尾的空格：",s.strip())
# print("去掉开头的空格：",s.lstrip())
# print("去掉结尾的空格：",s.rstrip())
#
# s = "test.txt"
# print("去掉后缀：", s.removesuffix(".txt"))
# print("去掉前缀：", s.removeprefix("test"))

"""
    (4)转大小写
    字符串.lower()
    字符串.upper()
    字符串.capitalize()：整个字符串的首字母转为大写
    字符串.title()：每一个单词的首字母转为大写
"""
# s = "Hello World"
# print("转为全小写：", s.lower())
# print("转为全大写：", s.upper())
s = "hello world"
print("首字母转为大写：", s.capitalize())
print("首字母转为大写：", s.title())

