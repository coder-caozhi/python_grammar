"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import math

"""
    math模块
"""
print("向上取整：",math.ceil(2.2))
print("向上取整：",math.ceil(2.8))
print("向上取整：",math.ceil(-2.8))

print("向下取整：",math.floor(2.2))
print("向下取整：",math.floor(2.8))
print("向下取整：",math.floor(-2.8))

print("截断取整：",math.trunc(2.2)) #正数类似于向下
print("截断取整：",math.trunc(2.8)) #正数类似于向下
print("截断取整：",math.trunc(-2.8))#负数类似于向上

#round函数不是math模块，它是内置函数
print("控制精度：",round(15.896547852145, 2)) #2位是按照小数点后2位，不包含整数。但是会出现四舍五入的情况。小数点后最后的0不显示

print("幂次方：", math.pow(2.5, 3.6))
print("幂次方：", math.pow(2, 10))
print("平方根：",math.sqrt(81))
print("指数：", math.exp(3)) # 常数e 2.7182818284...
print("指数：", math.exp2(3)) #底数是2

print("对数：", math.log(1024,2))
print("对数：", math.log10(1000))

print("阶乘：", math.factorial(5))
print("阶乘：", math.factorial(50))

print("最大公约数：",math.gcd(12,18))
print("最小公倍数：",math.lcm(12,18))

def gcd(m,n):
    pass

def lcm(m,n):
    pass

a = 0.1
b = 0.2
print(f"a+b={a+b}")
print("是否是近似值：", a + b == 0.3)
print("是否是近似值：", math.isclose(a+b, 0.3))