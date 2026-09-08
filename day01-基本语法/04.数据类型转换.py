# 隐式转换
num = 3
num2 = 3.3
# 整型和浮点型相加转换为浮点型
num3 = num + num2
print(num3)
print(type(num3))

# 两个整型相除也会转换为浮点型
num4 = 10
num5 = 3
num6 = 10 / 3
print(num6)
print(type(num6))

# 注意：在Python中整型和字符串不能相加，不会拼接字符串会报错
num7 = 88
str = "My Balance is"
# str2 = str + num7
# print(str2)

# 无法自动转换，必须显式转换
# str7 = '7'
# print(num7 + str7)

# 显示转换
# 字符串转int，字符串必须是数值类型
my_str = "123"
my_str_to_int = int(my_str)
print(my_str_to_int)
print(type(my_str_to_int))

# 浮点型转int，直接截取
my_float = 3.99
my_float_to_int = int(my_float)
print(my_float_to_int)
print(type(my_float_to_int))

# 布尔转int
my_f = False
my_f_to_int = int(my_f)
print(my_f_to_int)
print(type(my_f_to_int))

# 转布尔类型：0/空值/空容器为False，其他为True
my_num = 0
my_s = ""
my_l = []
my_num2 = 111
my_s2 = "hello"
my_l2 = [1,2,3]
my_num_to_bool = bool(my_num)
print(my_num_to_bool) # False
print(type(my_num_to_bool))
my_s_to_bool = bool(my_s)
print(my_s_to_bool) # False
print(type(my_s_to_bool))
my_l_to_bool = bool(my_l)
print(my_l_to_bool) # False
print(type(my_l_to_bool))
my_num2_to_bool = bool(my_num2)
print(my_num2_to_bool) #True
my_s2_to_bool = bool(my_s2)
print(my_s2_to_bool) # True
my_l2_to_bool = bool(my_l2)
print(my_l2_to_bool) # True

# 编码
my_en = "快下课了"
my_by = my_en.encode("UTF-8")
print(my_by)
print(type(my_by))

# 解码
my_en2 = my_by.decode("UTF-8")
print(my_en2)
print(type(my_en2))