"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
定义变量保存信息，按格式打印输出：
    班级：xxx
    姓名：xxx
    身高：xxx cm
    是否住校：True 或 False
"""
# clazz = "BJ20260511AI"
# name = "柴林燕"
# height = 153
# flag = True
# # print("班级：",clazz)
# # print("姓名：",name)
# # print("身高：",height,"cm")
# # print("是否住校：",flag)
#
# print("班级：",clazz, "\n姓名：",name,"\n身高：",height,"cm\n是否住校：",flag)

"""
# 题 3：购物总价计算
# 用变量 unit_price 表示商品单价，变量 count 表示购买数量。计算购买商品的总价格，最终显示小数点后 2 位。
# """
# unit_price = 9.69
# count = 9
# total_price = unit_price * count
# print("商品单价：",unit_price,"元/个")
# print("商品数量：",count,"个")
# print("商品总价：",round(total_price,2),"元")

"""
题 4：计算长方形的面积和周长
用变量 a、b 分别表示长方形的长和宽（自己赋值）。计算长方形的面积和周长，结果显示小数点后 2 位。
"""
# from decimal import Decimal
# a = 8.69632456321456315301
# b = 5.269632456321456315301
# area = a * b
# perimeter = 2 * a + 2 * b
# print("长：", a)
# print("宽：", b)
# print("面积：", round(area,2))
# print("周长：", round(perimeter, 2))

# # 小数的时候，要么float与float计算，Decimal与Decimal计算，Decimal不要与float直接计算（*等）
# a = Decimal("8.69632456321456315301")
# b = Decimal("5.269632456321456315301")
# area = Decimal(a * b) # a*b先是float，然后再转为Decimal，如果a*b计算有误差，是无法避免的
# perimeter = Decimal(2 * a + 2 * b)
# print("面积：", round(area,2))
# print("周长：", round(perimeter, 2))

"""
用变量 r 表示圆柱底面半径，变量 h 表示圆柱的高（自己赋值）。用常量 PI=3.1415926。结果显示小数点后 2 位。
圆柱体积公式：体积 = PI * r² * h
"""
r = 3.6
h = 2.5
PI = 3.1415926
v = PI * r * r * h
print("底面半径：",r)
print("高：",h)
print("体积：",round(v,2))
