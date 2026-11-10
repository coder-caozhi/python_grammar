"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    关键字：global
        如果想要在函数的局部位置，直接对全部的变量做修改（改元素值，改地址值），那么可以在函数内部用glolbal声明一下你用的是全局变量，
        做修改之后会影响全局的风险是我已知，是可以承受的。
    关键字： nonlocal
        如果想要在内层函数的局部位置，直接对外层函数变量做修改（改元素值，改地址值），那么可以内层函数内部用nonlocal声明一下你用的是
        外层函数的局部变量，修改之后的风险是我已知，是可以承受的。
    
    如果没有歧义，就不需要加global和nonlocal，
        如果有歧义，分不清是局部还是全局，那么就需要加global表示是全局的。
        如果有歧义，分不清是内层局部还是外层局部，那么就需要加nonlocal表示是外层函数的局部变量。
"""
# listDemo = [1,2,3] #可变类型
# a = 1 #不可变类型
# str_demo = "hello"#不可变类型
#
# def func():
#     #此时无论是可变和不可变类型，都是在func函数中新增加了局部变量，与外面的全局变量无关
#     a = 2
#     listDemo = [4,5,6]
#     str_demo = "world"
#     listDemo.append(4)#也是对局部变量listDemo做修改，与外部的全部变量无关
#     print("a = ",a)
#     print("listDemo = ",listDemo)
#     print("str_demo = ",str_demo)
#
#
# func()
# print("a = ", a)
# print("listDemo = ", listDemo)
# print("str_demo = ", str_demo)

print("=" * 50)
# listDemo = [1,2,3] #可变类型
# a = 1 #不可变类型
# str_demo = "hello"#不可变类型
#
# def func():
#     listDemo.append(4) #一定找外部。没有歧义，那么不需要加global
#     print("listDemo = ",listDemo)

print("=" * 50)
listDemo = [1,2,3] #可变类型
a = 1 #不可变类型
str_demo = "hello"#不可变类型

def func():
    global listDemo
    listDemo.append(4) #单纯从这里看，使用的是外部全局的
    listDemo = [4,5,6] #单纯从这句看，使用的是局部新定义的变量
                        #两句结合在一起，就有歧义，到底是外部的，还是局部新的
                        #如果想要是外部的，就加global
                        #如果想要明确是内部的，遵循先定义后使用
    global a,str_demo
    a = 2               #单纯从这句看，使用的是局部新定义的变量
    str_demo = "world"  #单纯从这句看，使用的是局部新定义的变量
                      #如果想要明确是外部的全局变量a,str_demo，也可以加global
    print("a = ",a)
    print("listDemo = ",listDemo)
    print("str_demo = ",str_demo)
    #此时无论是可变和不可变类型，都是在func函数中新增加了局部变量，与外面的全局变量无关
#
func()
print("a = ", a)
print("listDemo = ", listDemo)
print("str_demo = ", str_demo)

def outer():
    listDemo = [1,2,3]
    a = 1

    def inner():
        # nonlocal listDemo,a
        # listDemo.append(4) #不会指向新对象。单纯从这里看，使用的是外部函数的listDemo
        listDemo = [4,5,6] #让listDemo指向新对象。单纯从这句看，使用的是局部新定义的变量
                        # 两句结合在一起，就有歧义，到底是外部的，还是局部新的
                        # 如果想要是外部的，就加nonlocal
                        # 如果想要明确是内部的，遵循先定义后使用
        a = 2           #默认是局部新定义的，如果想要表示是外部函数的，就需要加nonlocal

    inner()#调用内部函数
    print("listDemo = ", listDemo)
    print("a = ", a)
outer() #调用外部函数