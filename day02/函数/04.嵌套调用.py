# 声明一个函数
def a():
    print("a方法入栈")
    print("执行a方法中的逻辑")
    print("a方法出栈")
def b():
    print("b方法入栈")
    # 调用a方法
    a()
    print("b方法出栈")

# 调用函数
b()