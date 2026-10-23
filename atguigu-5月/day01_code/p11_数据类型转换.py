"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
"""
    1、自动类型转换
    bool(布尔类型) -> int(整数类型) -> float(浮点类型) -> complex(复数)
    
    2、强制类型转换
    
    数值类型 + ：求和
    字符串类型 + ：拼接
    
    在python中，字符串只能与字符串拼接，不能直接与其他类型拼接。
    
    转为字符串用：str(值)
    转为整数，小数，布尔： int(值)、float(值)、Decimal(值)、bool(值)
    
"""
from decimal import Decimal
print(type(1/2))
print(True + True)

a = 1
b = 2
print(a + b) # 求和 得到3
print(str(a) + str(b)) #拼接 12
# print("hello" + 5) #错误，无法拼接，无法求和
print("hello"  + str(5))

x = "123"
y = "456"
print(x + y) #拼接
print(int(x) + int(y)) #求和

m = "3.14"
n = "2.14"
print(m + n)  #拼接
print(float(m) + float(n))  #求和
print(Decimal(m) + Decimal(n))  #求和