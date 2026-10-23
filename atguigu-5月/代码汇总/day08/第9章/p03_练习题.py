"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
创建一个银行账户类 BankAccount，实现基本的封装特性：
要求：
- 私有属性：__account_number（账号）、__balance（余额）、__password（密码）
    这里私有属性是类属性还是实例属性呢？怎么判断
    类属性：它的值所有对象共享的
    实例属性：每一个对象独立的
    
    __account_number（账号）、__balance（余额）、__password（密码）：每一个账号独立

- 提供公开方法：
  - deposit(amount, password)：存款（需要验证密码）
  - withdraw(amount, password)：取款（需要验证密码）
  - check_balance(password)：查询余额（需要验证密码）
  - set_password(old_password, new_password)：修改密码，修改密码时，还得输入旧密码用于验证
- 设置合理的属性访问控制，不允许直接访问和修改私有属性

提示： 使用双下划线前缀实现私有属性

"""
class BankAccount:
    def __init__(self, account_numer,password,balance=0): #形参是普通变量，不需要加__来私有化的说明
        self.__account_number = account_numer
        self.__password = password
        self.__balance = balance

    def deposit(self, amount, password):
        if password == self.__password:
            if amount > 0:
                self.__balance += amount
                return
            print("存款金额必须是正数")
        else:
            print("密码错误，请确认密码")

    def withdraw(self, amount, password):
        if password == self.__password:
            if amount<0:
                print("取款金额必须为正数")
                return
            if amount > self.__balance:
                print("余额不足")
                return
            self.__balance -= amount
        else:
            print("密码错误，请确认密码")

    def check_balance(self, password):
        if password == self.__password:
            print("余额：",self.__balance)
        else:
            print("密码错误，请确认密码")

    def set_password(self,old_password, new_password):
        if old_password == self.__password:
            self.__password = new_password
        else:
            print("密码错误，请确认旧密码")

#测试
b = BankAccount("11111","123456", 10000)
b.check_balance("123456")
b.check_balance("123458")
b.deposit(2000,"123456")
b.check_balance("123456")