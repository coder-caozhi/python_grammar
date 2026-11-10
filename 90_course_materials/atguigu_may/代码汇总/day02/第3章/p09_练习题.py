"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
# 编写代码实现程序运行时，输入2个整数，求它们的和、差、乘积、商
# a = int(input("请输入第1个整数："))
# b = int(input("请输入第2个整数："))
# print("a+b=", a + b)
# print("a-b=", a - b)
# print("a*b=", a * b)
# print("a/b=", a / b)

# a,b = input("请输入2个整数（示例：8,6）：").split(",") #按照空格等空白符进行拆分
# a = int(a)
# b = int(b)
# print("a+b=", a + b)
# print("a-b=", a - b)
# print("a*b=", a * b)
# print("a/b=", a / b)

"""
编写代码实现程序运行时，输入1个三位数的正整数，求它的百位、十位、个位
"""
# num = int(input("请输入1个三位数的正整数："))
# bai = num // 100
# # shi = num%100//10
# shi = num // 10 % 10
# ge = num % 10
# print("百位：",bai, "，十位：",shi ,"，个位：",ge)

#从键盘输入1个整数，表示完成某个任务的小时数，看该任务至少需要几天（不够1天算1天）
hours = int(input("请输入完成某个任务的小时数："))
print("完成某个任务需要：", hours//24 if hours % 24 == 0 else hours//24+1)