"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
"""
"""
    1、分支结构：
    （1）if-else的条件判断系列
    （2）match-case的选择结构系列
    
    2、match-case的语法格式
    match 表达式:
        case 常量值1:
            语句块1
        case 常量值2:
            语句块2
        case 常量值3:
            语句块3
        case 常量值4:
            语句块5
        case _:
            语句块n+1
    3、if-else与match-case对比
    （1）if-else的适用性更广，凡是可以用match-case，都可以使用if-else解决
    （2）对于常量值的比较判断，match-case的可读性和执行效率更好
"""
#从控制台接收[1,7]的整数值，输出对应的星期的英文单词
# week = int(input("请输入[1,7]的整数值："))
# match week:
#     case 1:
#         print("Monday")
#     case 2:
#         print("Tuesday")
#     case 3:
#         print("Wednesday")
#     case 4:
#         print("Thursday")
#     case 5:
#         print("Friday")
#     case 6:
#         print("Saturday")
#     case 7:
#         print("Sunday")
#     case _:
#         print("Error")

#从控制台接收[1,12]的整数值，输出对应的季节
#3,4,5 春季
#6,7,8 夏季
#9,10,11 秋季
#12,1,2 冬季
# month = int(input("请输入[1,12]的整数值："))
# match month:
#     case  3 | 4 | 5:
#         print("Spring")
#     case 6 | 7 | 8:
#         print("Summer")
#     case 9 | 10 | 11:
#         print("Fall")
#     case 12 | 1 | 2:
#         print("Winter")
#     case _:
#         print("Error")

# match month:
#     case  3 , 4 , 5: #错误
#         print("Spring")
#     case 6 , 7 , 8:
#         print("Summer")
#     case 9 , 10 , 11:
#         print("Fall")
#     case 12 , 1 , 2:
#         print("Winter")
#     case _:
#         print("Error")

"""
答疑：
"""
year = int(input("请输入年份（要求正数）："))
month = int(input("请输入[1,12]的整数值："))
#计算year年month月的总天数
# days_of_month = 31
# if month == 4 or month == 6 or month == 9 or month == 11:
#     days_of_month = 30
# elif month == 2:
#     days_of_month = 29 if year%4==0 and year%100!=0 or year%400==0 else 28
# if month == 4 or  6 or  9 or 11: #表达式1 month==4，表达式2是6，表达式3是9，表达式4是11，  True/False or 6 or 9 or 11，后面3个非0等价于True， False or True or True or True
#     days_of_month = 30
# elif month == 2:
#     days_of_month = 29 if year%4==0 and year%100!=0 or year%400==0 else 28

# if month in [4,6,9,11]:
#     days_of_month = 30
# elif month == 2:
#     days_of_month = 29 if year%4==0 and year%100!=0 or year%400==0 else 28

match month:
    case 4 | 6 | 9 | 11:
        days_of_month = 30
    case 2:
        days_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    case _:
        days_of_month = 31

print(f"{year}年{month}月的总天数{days_of_month}")