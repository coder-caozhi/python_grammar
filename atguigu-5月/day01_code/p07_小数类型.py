"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
import decimal

"""
    1、python中小数类型分为：
    （1）浮点型：float，精度范围大约是16-17位（科学计数法）
        误差比较大，只能得到近似值
    （2）定点型：decimal，精度范围可以任意
        更精确
    
    2、如何表示decimal的值
    Decimal("小数值")
    
    3、小数值最终显示的位数用round(值, 小数点后位数)（使用更多一些）
      Decimal类型在计算时，默认的精度由decimal.getcontext().prec，默认28位，可以手动设置（了解）
    
"""
from decimal import Decimal
#decimal模块，Decimal是类型名
a = 3.18624786248563245632563256325632896321485631453014530145301452
b = Decimal("3.18624786248563245632563256325632896321485631453014530145301452")
print("a的值：", a, "a的类型：",type(a))
print("b的值：", b, "b的类型：",type(b))

x = 0.1
y = 0.2
print(x + y) # 0.30000000000000004

m = Decimal("0.1")
n = Decimal("0.2")
print(m + n)

print(1/3) #浮点型float  0.3333333333333333

#Decimal类型在计算时，默认有一个精度范围 28位
decimal.getcontext().prec = 1000
print(Decimal("1") / Decimal("3")) # 定点型Decimal

a = 3.18624786248563245632563256325632896321485631453014530145301452
b = Decimal("3.18624786248563245632563256325632896321485631453014530145301452")
#显示时保留到小数点后2位
print("a表示到小数点后2位：", round(a, 2))
print("b表示到小数点后2位：", round(b, 2))