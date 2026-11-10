"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    自定义异常，需要定义一个类，继承Exception或它的子类，一般不会直接继承BaseException。
"""
class Money_Can_Not_Negative_Exception(Exception):
    pass
class Money_Not_Enough_Exception(Exception):
    pass

class BankAccount:
    def __init__(self,id):
        self.id = id
        self.balance = 0
    def withdraw(self,amount):
        if amount<0:
            # print("取款金额不能为负数")
            raise Money_Can_Not_Negative_Exception("取款金额不能为负数")
        if amount>self.balance:
            raise Money_Not_Enough_Exception("余额不足")
        self.balance -= amount
    def deposit(self,amount):
        if amount<0:
            raise Money_Can_Not_Negative_Exception("存款金额不能为负数")
        self.balance += amount

b = BankAccount("11111")
while True:
    try:
        print("余额：",b.balance)
        amount = int(input("请输入存款金额："))
        b.deposit(amount)
        break
    except Money_Can_Not_Negative_Exception as e:
        print(e)

while True:
    try:
        print("余额：", b.balance)
        amount = int(input("请输入取款金额："))
        b.withdraw(amount)
        break
    except Money_Can_Not_Negative_Exception as e:
        print(e)
        print("你想越取越多，休想")
    except Money_Not_Enough_Exception as e:
        print(e)
        print("钱不够，赶紧去挣钱")