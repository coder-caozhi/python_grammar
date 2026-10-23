"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
    1、python中所有函数都有返回值，默认返回None
    2、在函数体中用 “return 值” 语句来返回函数的具体结果。
      如果函数体中没有 “return 值” 的语句 或 只有 "return"的语句，那么函数的返回值就为None
"""
def say_hello():
    print("hello")
    #这里没有return语句，说明say_hello函数没有具体的返回值，默认返回None，也有人说该函数没有返回值

print(say_hello()) #(1)say_hello()调用say_hello函数，会执行say_hello函数的功能
                   #(2)print(say_hello()) 这里表示打印say_hello函数的返回值，不是打印say_hello函数对象本身

def say_hi():
    print("hi")
    return #return后面没有值，也是代表say_hi函数没有具体的返回值，默认返回None，也有人说该函数没有返回值
print(say_hi())

def add(a,b): #有参函数
    return a+b
print(add(1,2)) #打印add(1,2)函数的调用结果