"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
import copy

"""
    参数传递：
    1、谁给谁传值？实参给形参传值
    2、实参给形参传什么值？数据值 or 地址值
    答案：地址值，因为python一切皆对象。无论是变量赋值、参数传递、返回值等都是在传递地址值。
    
    
    3、关于函数调用的2个动作：
    （1）入栈：当函数被调用时，python解释器会在栈内存空间给这个函数开辟一整块独立的内存空间，用于存储这个函数的局部变量、操作数栈等信息。
    （2）出栈：当函数调用结束时，python解释器会自动释放该函数占用的栈内存空间。
    
    4、这种设计有什么影响？或者 形参对对象的修改与实参有什么关系？ 
    （1）当形参代表的是不可变的类型时，那么形参的修改与实参无关
    参数是字符串类型、整数类型、浮点型等
"""
# def change(a):
#     print(f"{a=}")
#     a += 1
#     print(f"{a=}")
#
# num = 1
# print("调用change函数之前：",num)
# change(num)
# print("调用change函数之后：",num)

# def change2(a):
#     print(f"{a=}")
#     a += 1
#     print(f"{a=}")
#     return a
#
# num = 1
# print("调用change函数之前：",num)
# num = change2(num)
# print("调用change函数之后：",num)

# s1 = "hello" #字符串对象不可变
# s1=s1.replace("e","a")
"""
    （2）当形参代表的是可变的类型时，那么形参对元素的修改与实参有关，因为此时形参与实参指向同一个对象
"""

# def change(lst):
#     print(f"{lst=}")
#     lst[0] = 100
#     print(f"{lst=}")
#
# nums = [1,2,3]
# print("调用change函数之前：",nums)
# change(nums)
# print("调用change函数之后：",nums)

"""
    （3）当形参代表的是可变的类型时，那么形参如果指向了新的对象，与实参就无关了。
"""

# def change(lst):
#     print(f"{lst=}")
#     lst = [100,2]
#     print(f"{lst=}")
#
# nums = [1,2,3]
# print("调用change函数之前：",nums)
# change(nums)
# print("调用change函数之后：",nums)

# s1 = {1,2,3,4}
# s2 = {3,4,5,6}
# print("交集：", set.intersection(s1,s2)) #产生了新的集合地址，所以需要返回新地址
# print("交集：",set.intersection_update(s1,s2))#基于s1直接修改，不产生新地址


# def change(lst):
#     print(f"{lst=}")
#     # lst += [100,2] # 这个没有产生新的列表对象，直接在lst列表中拼接新元素
#     lst = lst + [100,2] #产生新的列表对象
#     print(f"{lst=}")
#
# nums = [1,2,3]
# print("调用change函数之前：",nums)
# change(nums)
# print("调用change函数之后：",nums)

"""
    5、当形参代表可变类型时，如果函数体中对形参的元素做修改时，可能影响实参。
      那么能不能无论函数体做什么操作，都不要影响实参？如果想要实现这个要求，需要使用copy.deepcopy(可变对象) 深拷贝
"""
def change(lst):
    print(f"{lst=}")
    lst.append(1)
    lst[0] = 88
    lst += [100,2] # 这个没有产生新的列表对象，直接在lst列表中拼接新元素
    lst = lst + [100,2] #产生新的列表对象
    print(f"{lst=}")

nums = [1,2,3,[4,5]]
print("调用change函数之前：",nums)
change(copy.deepcopy(nums))
print("调用change函数之后：",nums)
