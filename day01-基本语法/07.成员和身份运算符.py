# 成员运算符
my_str = "hello"
# 判断e在不在str中
print("e" in my_str)  # True
print("a" not in my_str)  # True

# 创建一个列表
my_list = [1, "a", 6.66, True]
# 判断1在不在列表中
print(1 in my_list)  # True
print("a" not in my_list)  # False

"""
    身份运算符
    在Python中
    == 相当于Java中的 equals
    is 相当于Java中的 ==
"""
num = 10
num2 = 10
print(num == num2)  # True
print(id(num))
print(num is num2)  # True
print(id(num2))

num3 = 1000
num4 = 1000
print(num3 == num4)  # True
print(id(num3))
print(num3 is num4)  # True
print(id(num4))

print(num3 is not num4)  # False
