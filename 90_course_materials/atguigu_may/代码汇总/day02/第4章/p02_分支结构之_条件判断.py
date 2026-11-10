"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
"""
"""
刮奖：
请输入1个5位数整数，
如果数字中包含4，就奖励100
如果数字中包含7，就奖励200
如果数字中包含9，就奖励300
奖金可以累计，统计最终奖金
"""
# num = input("请输入1个5位数的整数：")
# money = 0
# if "4" in num:
#     money += 100
#     print("数字中有4")
# if "7" in num:
#     money += 200
#     print("数字中有7")
# if "9" in num:
#     money += 300
#     print("数字中有9")
# print(f"数字：{num}，总奖金：{money}")
"""
    分支结构之条件判断：
    （1）单分支条件判断
    if 条件表达式 :
        语句块
    执行点：当条件表达式的值为True时，会执行对应的语句块，否则就不执行
"""


"""
数字判断，
如果一个数是偶数，就输出
    xx是偶数
    xx是双数
    xx是可以被2整除的数
如果是奇数，就输出
    xx是奇数
    xx是单数
    xx是不可以被2整除的数
"""
# num = int(input("请输入一个整数："))
# if num % 2 == 0:
#     print(f"{num}是偶数")
#     print(f"{num}是双数")
#     print(f"{num}是可以被2整除的数")
# else:
#     print(f"{num}是奇数")
#     print(f"{num}是单数")
#     print(f"{num}是不可以被2整除的数")

"""
    分支结构之条件判断：
    （2）双分支条件判断
    if 条件表达式 :
        语句块1
    else:
        语句块2
    执行点：当条件表达式的值为True时，会执行对应的语句块1，否则就执行语句块2
"""


"""
成绩判定，成绩范围是[0,100]
如果成绩不在[0,100]范围，提示输入有误
如果成绩是100，输出满分
如果成绩是90-99，输出优秀
如果成绩是75-89，输出良好
如果成绩是60-74，输出及格
如果成绩是0-59，输出不及格
"""
# score = int(input("请输入成绩[0,100]："))
# if score<0 or score>100:
#     print("成绩范围是[0,100]，输入有误")
# elif score == 100:
#     print("满分")
# elif score>90:
#     print("优秀")
# elif score>75:
#     print("良好")
# elif score>60:
#     print("及格")
# else:
#     print("不及格")

"""
    分支结构之条件判断：
    （3）多分支条件判断
    if 条件表达式1 :
        语句块1
    elif 条件表达式2:
        语句块2
    elif 条件表达式3:
        语句块3 
    ...
    else:
        语句块n+1
    执行点：
        当条件表达式1的值为True时，会执行对应的语句块1，后面就不执行了
        当条件表达式1不成立，看条件表达式2
        当条件表达式2的值为True时，会执行对应的语句块2，后面就不执行了
        当条件表达式2也不成立，看条件表达式3
        。。。
        当所有条件都不成立，就执行else中的语句块n+1
"""


"""
输入年月日，
年份要求正数，如果不是正数，就提示年份输入有误，且不再输入月和日，如果年份正确，继续输入月和日
月份要求[1,12]，如果月份不对，就提示月份输入有误，且不再输入日，如果月份正确，继续输入日
日期范围[1,改月最大天数]，如果日期值不对就提示日期输入有误，如果日期输入正确，就显示xx年xx月xx日
"""
year = int(input("请输入年份（要求正数）："))
if year > 0:
    month = int(input("请输入月份（要求[1,12]）："))
    if 1<=month<=12:
        #计算year年month月的总天数
        days_of_month = 31
        if month == 4 or month == 6 or month == 9 or month == 11:
            days_of_month = 30
        elif month == 2:
            days_of_month = 29 if year%4==0 and year%100!=0 or year%400==0 else 28

        day = int(input(f"请输入月份（要求[1,{days_of_month}]）："))
        if 1<=day<=days_of_month:
            print(f"{year}年{month}月{day}日")
        else:
            print(f"日期输入有误，日期范围[1,{days_of_month}]!")
    else:
        print("月份输入有误，月份范围[1,12]！")
else:
    print("年份输入有误，年份必须是正数！")
"""
    嵌套的原则：当外层条件成立，才看内层。
"""

#后续可以通过其他方式，减少的嵌套的层数
# def exerice():
#     year = int(input("请输入年份（要求正数）："))
#     if year <= 0:
#         print("年份输入有误，年份必须是正数！")
#         return
#
#     month = int(input("请输入月份（要求[1,12]）："))
#     if month<1 or month>12:
#         print("月份输入有误，月份范围[1,12]！")
#         return
#
#     # 计算year年month月的总天数
#     days_of_month = 31
#     if month == 4 or month == 6 or month == 9 or month == 11:
#         days_of_month = 30
#     elif month == 2:
#         days_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
#
#     day = int(input(f"请输入月份（要求[1,{days_of_month}]）："))
#     if 1 <= day <= days_of_month:
#         print(f"{year}年{month}月{day}日")
#     else:
#         print(f"日期输入有误，日期范围[1,{days_of_month}]!")


