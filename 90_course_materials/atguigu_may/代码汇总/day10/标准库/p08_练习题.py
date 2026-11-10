"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import string

"""
题目要求：编写一个程序，实现以下功能：
1. 接收用户输入的一个起始日期（格式：YYYY-MM-DD）和一个天数 n；
2. 计算并输出起始日期加上 n 天后的日期；
3. 计算并输出起始日期是星期几（中文显示：星期一 / 星期二...）；
4. 计算并输出起始日期所在月份的总天数。
"""
# from datetime import datetime
# from datetime import timedelta
# import calendar
# date_str = input("请输入一个起始日期（格式：YYYY-MM-DD）")
# # n = int(input("请输入一个天数："))
# #
# date_obj = datetime.strptime(date_str,"%Y-%m-%d")
# # after_date = (date_obj + timedelta(days=n)).date()
# # print(f"{date_str}加上{n}天之后的日期是{after_date}")
#
# # week = date_obj.weekday()
# # week_name = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
# # print(f"{date_obj.date().strftime('%Y-%m-%d')}对应的星期是{week_name[week]}")
#
# year = date_obj.year
# month = date_obj.month
# print(f"{date_obj.date().strftime('%Y-%m-%d')}所在月份的总天数：{calendar.monthrange(year, month)[1]}")

"""
题目要求：编写一个函数，生成指定长度的随机验证码，要求：
1. 验证码包含大写字母、小写字母和数字；
2. 长度由用户输入指定（范围：4-8 位）；
3. 确保每个验证码中至少包含 1 个大写字母、1 个小写字母和 1 个数字；
4. 输出生成的验证码。
"""
# import random
# n = int(input("请输入验证码的位数（范围：4-8 位）："))
# one_upper_letter = random.choice(string.ascii_uppercase)
# one_lower_letter = random.choice(string.ascii_lowercase)
# one_digit_letter = random.choice(string.digits)
# last_letters = random.choices(string.digits+string.ascii_letters, k=n-3)
# code = [one_upper_letter] + [one_lower_letter] + [one_digit_letter] + last_letters
# random.shuffle(code)
# code = "".join(code)
# print("验证码：",code)


"""
题目要求：编写一个程序，实现以下功能：
1. 让用户选择计算类型：圆的面积、球体的体积、直角三角形的斜边长度；
       	print("=== 几何计算工具 ===")
        print("1. 计算圆的面积")
        print("2. 计算球体的体积")
        print("3. 计算直角三角形的斜边长度")
2. 根据选择的类型，接收对应的输入参数（如圆的半径、三角形的两条直角边）；
   例如：选择1.计算圆的面积后，让用户输入圆的半径
3. 使用 math 库的函数完成计算，结果保留 2 位小数；
4. 输出计算结果。
"""
# import math
# print("=== 几何计算工具 ===")
# print("1. 计算圆的面积")
# print("2. 计算球体的体积")
# print("3. 计算直角三角形的斜边长度")
# select = int(input("请选择："))
# match select:
#     case 1:
#         radius = float(input("请输入圆的半径值："))
#         area = math.pi * radius * radius
#         print(f"圆的半径：{radius}，面积：{area}")
#     case 2:
#         radius = float(input("请输入球的半径值："))
#         volume = 4/3*math.pi * radius ** 3
#         print(f"球的半径：{radius}，体积：{volume}")
#     case 3:
#         a = float(input("请输入直角边1的值："))
#         b = float(input("请输入直角边2的值："))
#         c = math.sqrt(a**2 + b**2)
#         print(f"直角边是{a},{b}的斜边是{c}")
#     case _:
#         print("不支持该计算")

"""
题目要求：编写一个抽奖程序，结合random、datetime、string库，实现：
1. 读取用户输入的抽奖名单（多个名字用逗号分隔）；
2. 生成每个参与者的唯一抽奖码（格式：8 位，前 4 位为随机大写字母，后 4 位为随机数字）；
3. 记录抽奖时间（精确到秒）；
4. 随机抽取 1 名一等奖、2 名二等奖、3 名三等奖；
5. 按格式输出抽奖结果（包含抽奖时间、各奖项获奖者及抽奖码）。
"""
import random
from datetime import datetime
names = input("请输入抽奖者名单（多个名字用逗号分隔）").split(",") #张三,李四,王五,赵六,熊大,熊二,光头强,张三

join_dict = {} #key是抽奖码，value是抽奖者的名字
for name in names:
    while True:
        upper_letters = random.sample(string.ascii_uppercase,4)
        digit_nums = random.sample(string.digits,4)
        code = upper_letters + digit_nums
        code = "".join(code)
        if code not in join_dict:
            join_dict[code] = name
            break
print("抽奖码与抽奖者：", join_dict)

codes = list(join_dict.keys())#获取字典的所有key
random.shuffle(codes)

print("参与抽三等奖的有：", codes)
print("抽取三等奖：")
three = random.sample(codes,3)
three_time = datetime.now()
print("中奖者：")
for code  in three:
    print(f"中奖码：{code}，名字：{join_dict[code]}，中奖时间：{three_time}")
    codes.remove(code)


print("参与抽二等奖的有：", codes)
print("抽取二等奖：")
two = random.sample(codes,2)
two_time = datetime.now()
print("中奖者：")
for code  in two:
    print(f"中奖码：{code}，名字：{join_dict[code]}，中奖时间：{two_time}")
    codes.remove(code)

print("参与抽一等奖的有：", codes)
print("抽取一等奖：")
one = random.sample(codes,1)
one_time = datetime.now()
print("中奖者：")
for code  in one:
    print(f"中奖码：{code}，名字：{join_dict[code]}，中奖时间：{one_time}")
    codes.remove(code)