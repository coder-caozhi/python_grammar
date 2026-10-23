"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
from datetime import date,datetime
# datetime对应 datetime.py文件
# date,datetime 对应的是class
"""
    datetime模块中的函数、类等请看笔记中的表格。
"""
# print("今天的日期：", date.today())
# print("现在的时间：",datetime.now())
#
# kai = date(2026,5,11) #创建了一个date类的对象
# print("开班日期：",kai)
#
# end_class = datetime(2026,5,23,17,30,0)
# print("下课时间：",end_class)

# today = date.today() #today是一个对象
# print("今年：", today.year)
# print("当前月：", today.month)
# print("当前日期：", today.day)
# # print("小时：",today.hour) #错误
# print("星期值：", today.weekday()) #周一到周日分别是0-6
# print("星期值：", today.isoweekday())#周一到周日分别是1-7
#
# now = datetime.now()
# print("now = ", now)
# print("今年：", now.year)
# print("当前月：", now.month)
# print("当前日期：", now.day)
# print("时：",now.hour)
# print("分：",now.minute)
# print("秒：",now.second)
# print("微秒：",now.microsecond)

# date_str = input("请输入你的生日（xxxx年xx月xx日）：")#2000年05月09日
# #p：parse解析，将字符串解析为日期时间对象
# # datetime类
# #datetime.strptime(date_str,"%Y年%m月%d日")函数调用结果是一个datetime类的对象
# #datetime.strptime(date_str,"%Y年%m月%d日").date() 函数调用结果是一个date类型的对象
# birthday = datetime.strptime(date_str,"%Y年%m月%d日").date()
# # print(type(birthday))
# print("得到出生的年份值：", date_str[0:4]) #不同类型的对象所支持的操作是不同的
# print("得到出生的年份值：", birthday.year)

# #返过来，把日期时间对象转为字符串
# today = date.today() #date类型的对象
# #f：format格式化，将日期时间对象转为字符串
# date_str = today.strftime("%Y-%m-%d")
# print(date_str)
# print(type(date_str))

#时间差

# kai = date(2026,5,11)
# today = date.today()
# t = today - kai
# # print(type(t)) #<class 'datetime.timedelta'>
# print(t) #12 days, 0:00:00

kai = datetime(2026,5,11,9,0,0)
now = datetime.now()
t = now - kai
print(t) #12 days, 7:44:47.732955
print("开班的天数：",t.days) #12
print("开班的秒数：",t.seconds) #27944













