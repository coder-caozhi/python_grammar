"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
    逻辑运算符是用于判断多个布尔值或多个条件的关系。计算结果也是布尔值。
    （1）与   and  表示同时成立的关系
    （2）或   or   表示有1个成立即可的关系
    （3）非   not  表示条件取反的关系
"""
#表达年龄值同时满足大于18，且小于35
age = 23
print(age>18 and age<35)
print(18 < age < 35)

#表达年龄同时满足大于18，性别为女
gender = '男'
print(age > 18 and gender=='女')

#闰年
#（1）年份值能被4整除，同时不能被100整除
#（2）或年份值可以被400整除
year = 2000
print(year%4==0 and year%100!=0 or year%400==0)

#偶数
#能被2整除的数
num = 6
print(num%2==0) #是偶数吗
print(not num%2!=0) #不是奇数吧