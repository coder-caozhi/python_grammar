"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
"""
定义一个函数check_age，该函数接受一个年龄参数。
如果年龄小于 0，抛出一个自定义异常InvalidAgeError；
如果年龄大于 120，抛出UnrealisticAgeError。
这两个自定义异常类都继承自Exception类。
调用该函数并传入一个不合法的年龄值，捕获并处理异常。

如果自定义异常没有继承BaseException及其子类，是无法使用raise手动抛出，也无法使用except进行捕获。
通常都是继承BaseException的子类Exception
"""
class InvalidAgeError(Exception):
    pass
class UnrealisticAgeError(Exception):
    pass

def check_age(age):
    if age<0:
        raise InvalidAgeError
    if age>120:
        raise UnrealisticAgeError
    return True

try:
    print(check_age(23))
except InvalidAgeError:
    print("年龄不能为负数")
except UnrealisticAgeError:
    print("年龄不能超过120")


try:
    print(check_age(223))
except InvalidAgeError:
    print("年龄不能为负数")
except UnrealisticAgeError:
    print("年龄不能超过120")

try:
    print(check_age(-23))
except InvalidAgeError:
    print("年龄不能为负数")
except UnrealisticAgeError:
    print("年龄不能超过120")