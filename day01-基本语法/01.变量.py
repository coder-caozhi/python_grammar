# 变量以数字、字母、下划线命名，不能以数字开头，声明时不需要指定类型
"""
多行注释
在Python中一切皆对象
"""
print("========================")
# print
my_var = 1
print(my_var)

# 打印my_var变量执行的1对象的地址
print(id(my_var))
print("========================")
my_var2 = "hello"
print(my_var2)
my_var3 = 6.66
print(my_var3)
my_var4 = False
print(my_var4)
my_var5 = True
print(my_var5)
my_var = 10
print(my_var)
print(id(my_var))
print("========================")
# 给多个变量赋同一个值
a = b = c = 888
print(a)
print(b)
print(c)
# 给多个变量同时赋值
x,y,z = 11,22,33
print(x)
print(y)
print(z)
print("========================")
# 常量，常量使用大写字母表示
PI = 3.141592653589793
print(PI)
