"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    在python中异常对象的抛出有如下几种情况：
    1、自动抛出：python解释器帮我们检查出来的错误或异常，然后创建合适的异常对象，并且抛出。（大部分都是这种情况）
    2、手动抛出：当程序需要在满足xx例外的情况下，使得程序中断，可以用抛出异常对象来表示
        raise 异常对象
    3、测试抛出：assert断言
"""
class BankAccount:
    def __init__(self,id):
        self.id = id
        self.balance = 0
    def withdraw(self,amount):
        if amount<0:
            # print("取款金额不能为负数")
            raise ValueError("取款金额不能为负数")
        if amount>self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
    def deposit(self,amount):
        if amount<0:
            raise ValueError("存款金额不能为负数")
        self.balance += amount

# try:
#     b = BankAccount("11111")
#     b.withdraw(100)
# except ValueError as e:
#     print(e) #自动调用e.__str__() 默认返回异常对象的描述信息("取款金额不能为负数")

b = BankAccount("11111")
while True:
    try:
        print("余额：",b.balance)
        amount = int(input("请输入存款金额："))
        b.deposit(amount)
        break
    except ValueError as e:
        print(e)

while True:
    try:
        print("余额：", b.balance)
        amount = int(input("请输入取款金额："))
        b.withdraw(amount)
        break
    except ValueError as e:
        print(e)