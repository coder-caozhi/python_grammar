# 声明一个全局变量（如果是不可变类型，在函数内部无法修改变量的值）
a = 10
# 声明一个全局变量（如果是可变类型，在函数内部可以修改变量的值）
b = [1,2,3]

# 定义一个函数修改全局变量的值，全局变量是一个不可变类型的值
def modify_a():
    # 在函数内部使用global关键字将全局变量修饰之后即可修改全局变量的值
    global a
    a = 100
    print(a)

# 定义一个函数修改全局变量的值，全局变量是一个可变类型的值
def modify_b():
    b[0] = 100
    print(b)
# 调用函数modify_a
modify_a() # 100
# 在函数外部再打印a的值
print(a) # 100

# 调用函数modify_b
modify_b() # [100,2,3]
# 在函数外部再打印a的值
print(b) # [100,2,3]

print("="*60)

# 修改嵌套作用域变量的值
def modify_c():
    # 嵌套作用域变量
    c = 200
    def modify_d():
        # 在函数内部使用nonlocal关键字将嵌套作用域变量修饰之后即可修嵌套作用域变量的值
        nonlocal c
        c = 2000
        print(c)
    # 调用子函数
    modify_d()
    print(c)

# 调用modify_c函数
modify_c()