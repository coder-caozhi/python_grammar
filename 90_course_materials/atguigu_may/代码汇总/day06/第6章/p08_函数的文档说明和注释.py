"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    当我们要定义一个函数时，想要让团队中的其他人，或将来的自己，能更好的理解函数的作用，调用方式，参数的意义等，
    最好能写上函数的文档说明，函数的注释等。
    还有函数名、参数名的命名也很重要，最好能见名知意。
    
    函数的文档说明的作用：当我们在pycharm等集成开发工具中，使用某个函数时，把鼠标放到函数名上，可以查看函数的文档说明，用于了解这个函数。
                    或者使用help(函数名) 打印函数的文档说明
                    
    函数的注释：通常是对参数的类型，函数的返回值类型等做说明，但是不能真正的起到限制的作用。
"""
def print_rectangle(a:int, b:int, s:str)->None:
    """
    这个函数的作用是打印a行b列s对应的符号组成的矩形
    :param a: 代表行数，大于1的正整数
    :param b: 代表列数，大于1的正整数
    :param s: 代表字符，可以是1个或多个字符
    :return: None
    """
    for i in range(a):
        for j in range(b):
            print(s, end='')
        print()
    # print(a,b,s)

# print_rectangle(5,10,"#")
# help(print_rectangle)
# print_rectangle(5.6, 9.6, 9.6) #先是有警告，运行有错误，因为浮点数无法遍历
