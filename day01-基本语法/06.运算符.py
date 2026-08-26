# 算术运算符

a = 10
b = 3
result1 = a / b # 得到的是一个浮点数
result2 = a // b #得到的是商，相当于Java中的 /
result3 = a % b
result4 = a ** b #a的b次方
print(result1)
print(result2)
print(result3)
print(result4)

# 赋值运算符
a /= 4
print(a)
a //= 4
print(a)
b **= 3
print(b)
# 海象运算符（:=），判断加赋值一步到位
age = 20
if my_age := age >= 18:
    print(f"是否是成年人：{my_age}") #True

text = "hello"
if (length := len(text)) > 3:
    print(f"长度是 {length}")  # 5

# 比较运算符
print(a > b)
print(a <= b)
print(a == b)

# 逻辑运算符
print(age > 18 and len(text) > 3)
print(age <= 18 or len(text) > 3)
print(not age > 18)
# 以下两种运算不会报 ZeroDivisionError: division by zero
print(age < 18 and 10/0) # False，当前面是False的时候后面不再运算
print(age >= 18 or 10/0) # True，当前面是True的时候后面不再运算
