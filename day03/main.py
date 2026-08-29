# 导入atguigu包，__init__.py中的成员都可以使用
import random

import atguigu
# 导入atguigu包下的fun模块（导入所有）
import atguigu.fun as fun
# 精确导入
from atguigu.fun2 import fun3


print(atguigu.__author__)
print(atguigu.__version__)

# 调用fun模块中的成员
print(fun.num)
print(fun.__my_str2)
fun.fun()
fun.__fun2()

fun3()

print(random.randint(1,10))

# 打印__name__属性
print(__name__)