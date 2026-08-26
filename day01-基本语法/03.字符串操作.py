# 使用双引号或单引号括起来的都属于字符串
from http.cookiejar import join_header_words

str = "hello python"
print(type(str))
str2 = 'hello world'
# 双引号字符串中可以嵌套单引号；单引号字符串中可以嵌套双引号
str3 = "hello 'python'"
str4 = 'hello "world"'
print(type(str4))
# 多行字符串，使用三个双引号或单引号（所见即所得）
str5 = """
    Hello World
    Hello Python
    Hello Java
    Hello C
"""
print(type(str5))
print(str5)

# 转义字符
str6 = "hello\npython"
print(str6)
str7 = "I'am Tom"
print(str7)
str8 = 'I\'m Jerry'
print(str8)

# split()函数
str9 = "蔡徐坤,吴亦凡,王飞龙,李易峰,PGone,李小璐"
my_list = str9.split(",")
print(my_list)
print(type(my_list))

# join()函数
my_list2 = ["罗志祥","陶喆","文章","林丹","吴秀波","马蓉","宋喆"]
# 使用♂符号将列表中的数据连接起来
my_str = "♂".join(my_list2)
print(my_str)

# strip()函数：去掉前后空格
my_str = "     hello pytho     "
print(my_str)
# 去除前后空格之后
print(my_str.strip())
# 去除左边的空格
print(my_str.lstrip())
# 去除右边的空格
print(my_str.rstrip())

# replace()函数
my_str2 = "范冰冰,赵薇,户晨风"
print(my_str2.replace(",","-"))
print(my_str2.replace(",",""))
my_str3 = "hahaha python"
print(my_str3.replace("ha","hei",2))
