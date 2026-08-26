"""
    Python中的数据类型：
        数值
            整数
            浮点数
            布尔
            复数
        字符串
        容器
           列表[]
           元组()
           集合{}
           字典
        None
    通过type函数查看变量的类型
"""
num = 1
print(type(num))
num1 = 8.88
print(type(num1))
num2 = True
print(type(num2))
# 分隔符
num3 = 1_000_000_000_000
print(type(num3))
print(num3)
# 布尔类型属于int的子类型
num4 = False
print(isinstance(num4,int))

# 数值、字符串、元组属于不可变类型，列表、集合、字典属于可变类型
str = 'hello'
print(str)
print(id(str))
str = "python"
print(str)
print(id(str))

# 声明一个列表
my_list = [1,2,3,4]
print(my_list)
print(id(my_list))
# 修改列表第一个位置的值
my_list[0] = 100
print(my_list)
print(id(my_list))

# 声明一个函数
def hello_world():
    print("hello python")

result = hello_world()
print(result)