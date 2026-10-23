"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    3、测试抛出：assert断言
        当断言的条件不成立是，会抛出AssertionError异常
"""
def add(a,b):
    # return a+b
    return a-b #故意写错

assert add(1,2)==3 , "add有问题"
"""
    上面这句代码等价于：
    if add(1,2)==3:
        raise AssertionError("add有问题")
"""

