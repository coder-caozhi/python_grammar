# 使用import完整导入：被导入的模块中的所有的成员都可以使用
import fun
# 完整导入的时候起别名
import fun as f

# 精确导入
from fun import fun3

# 访问被导入模块的变量
print(fun.num)
print(fun._my_str)
print(fun.__my_str2)

# 通过别名访问
print(f.num)
print(f.PI)

# 调用被导入模块的函数
fun.fun()
fun._fun1()
fun.__fun2()

# 测试精确导入的函数
fun3()


