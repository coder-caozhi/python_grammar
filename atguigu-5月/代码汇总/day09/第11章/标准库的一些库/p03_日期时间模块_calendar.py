"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    calendar看笔记
"""
from calendar import calendar, prcal, month, prmonth,weekday,weekheader,monthrange,isleap,leapdays

# print("2026年的日历：")
# # print(calendar(2026))
# # prcal(2026)
#
# print("本月的日历：")
# # print(month(2026,5))
# prmonth(2026,5)

# print(weekday(2026,5,23)) #5
# #weekheader代表星期单词的开头几个字母，指定宽度
# print(weekheader(3)) #Mon Tue Wed Thu Fri Sat Sun   3代表宽度
# print(weekheader(5)) # Mon  Tue  Wed  Thu  Fri  Sat  Sun  5代表宽度

# print(monthrange(2026,5))
#(calendar.FRIDAY, 31) 元组，第一个元素
#元素1：这个月第1天是星期几
#元素2：这个月的总天数

# year = 2026
year = 2000
print("2026年是闰年吗？", year%4==0 and year%100!=0 or year%400==0)
print("2026年是闰年吗？", isleap(year))

after = 3000
print("2000-3000年之间有几个闰年：",leapdays(year,after))
