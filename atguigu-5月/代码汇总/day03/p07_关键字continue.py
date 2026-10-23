"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    关键字：continue
    作用：跳过本次循环体剩下的语句，继续下一次循环
"""
#从控制台接收正整数，判断它是奇数还是偶数，不判断负整数，0就代表输入结束
while True:
    num = int(input("请输入一个正整数："))
    if num < 0:
        continue
    if num == 0:
        break
    print(f"正整数{num}是{'偶数' if num%2==0 else '奇数'}")