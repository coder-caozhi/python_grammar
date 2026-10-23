"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
    if else 用于二选一
    结果1 if 条件 else 结果2，当条件成立就选结果1，不成立就选结果2
    凡是结算结果是布尔值，都可以当条件
"""
#偶数还是奇数
num = 9
print("偶数" if num%2==0 else "奇数")

a = 5
b = 13
# c = a  if a>b else b
# print(c)
print("最大值是",a) if a>b else print("最大值是",b)

