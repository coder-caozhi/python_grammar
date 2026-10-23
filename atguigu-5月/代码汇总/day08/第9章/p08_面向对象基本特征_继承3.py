"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""

"""
    1、演示多继承
    这些父类不一定是混入类（父类中有多个方法，甚至有自己的属性），
    而且多个父类之间的功能可能重叠（多个父类的方法可能重名），
    甚至还会出现菱形继承问题（C继承B,E继承D，然后B和D有同时继承A，子类F同时继承C和E）。
    
    2、MRO
    如果多个父类有同名方法，子类调用时会按固定顺序查找，这个顺序就是方法解析顺序（Method Resolution Order，MRO）。
    Python3 中 MRO 遵循C3 算法，简单总结：
    （1）. 先找子类自己的方法；
    （2）. 再按父类定义的顺序从左到右查找；
    （3）. 最后找共同的祖先类。
    
    遵循先子后父

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
        super().show()

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

s = Sub()
s.show()
s.say_hello()
s.say_hi()

# b = B()
# b.show()