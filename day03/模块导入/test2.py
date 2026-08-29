# 使用import *局部导入，只能使用被导入模块中公共的成员
from fun import *

# 访问被导入模块的变量
print(num)
# print(_my_str)
# print(__my_str2)

# 调用被导入模块的函数
# fun()
# _fun1()
# __fun2()
fun3()