"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""

"""
    1、演示突破MRO原则，打破MRO步骤
    在子类中用 super(父类名1, self).方法()：表示从父类名1之“后”的父类查找这个方法，这样可以跳过中间的一些父类。
    在子类外面 父类名2.方法(子类对象)：表示从父类名2开始查找这个方法，这样可以跳过子类自己以及前面的一些父类。
"""
class A:
    def show(self):
        print("A")
        super().show()
    def say_hello(self):
        print("hello")

class B(A):
    def show(self):
        print("B")
        super().show()

class C(B):
    def show(self):
        print("C")
        #明确找A的show()
        super(D,self).show()

    def say_hi(self):
        print("hi")

class D(A):
    def show(self):
        print("D")
        super().show()
    def say_hello(self):
        print("hello world")

class E(D):
    def show(self):
        print("E")
        super().show()

# class F: #默认继承object
class F(object): #明确继承object
    def show(self):
        print("F")
        # super().show()

class Sub(C,E,A,F):
    def show(self):
        print("Sub")
        super().show()

# s = Sub()
# s.show()
# s.say_hello()
# s.say_hi()

s = Sub()
A.show(s) #直接说调用A类show()