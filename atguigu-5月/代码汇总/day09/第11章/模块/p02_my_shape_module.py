"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    自定义模块
"""
__all__ = ["print_rectangle","multiply"]

def print_rectangle(width, height):
    """
    打印矩形
    :param width: 宽度
    :param height: 高度
    :return:
    """
    for i in range(height):
        for j in range(width):
            print("*", end="")
        print()

def print_diamond(lines):
    """
    打印菱形
    :param lines: 层数
    :return:
    """
    if not lines % 2 != 0:
        raise ValueError("lines 必须是奇数")
    center = int(lines // 2)
    for i in range(lines):
        for j in range(lines):
            if abs(i-center) + abs(j-center) <= center:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# 为了演示重名，故意与p01_my_math_module中的multiply()方法重名
def multiply(a, b):
    """
    重复打印b次的a接收的数据
    :param a: 要重复的数据
    :param b: 重复b次
    :return:
    """
    print(f"{a}"* b)