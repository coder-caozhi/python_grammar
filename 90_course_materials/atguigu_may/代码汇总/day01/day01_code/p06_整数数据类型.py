"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
import decimal

"""
    1、python中的数据类型有很多
    （1）内置和标准库中的类型
    A:python中有一些类型是嵌入到python解释器中，没有单独的py文件，甚至是用C、C++来实现的。这种看不到源码。这些类型是内置类型，
    例如：整数类型int，小数类型float，布尔类型bool，字符串str等，使用它们不需要import
    B:python中也有一些类型是官方提供的库，即很多的py文件，例如：decimal库中Decimal类型，使用它们需要import
    （2）自定义类型：后期学习面向对象时再说
    
    2、整数类型 int
    在python中只有1种整数类型int，不像其他语言分为：byte,short,int,long。
    在python中int可以表示任意范围的整数。
    
    3、python中有小整数池的概念，官方的CPython解释器中的小整数池的范围是[-5, 256]。
    小整数池中的整数对象是可以被共享的。
    
    4、python中是一切皆对象。
    Java中有面向对象的概念，但是Java中的8种基本数据类型：byte,short,int,long,float,double,boolean,char不是面向对象的。
    但是python中所有类型，包括int,float,bool都是对象。
    
    5、整数对象不可变
    为了节省内存，python考虑共享一些对象，例如：小整数池的范围是[-5, 256]
    通过id(变量)查看对应的内存地址。
    这些整数对象可以被共享有一个前提条件，就是整数对象是不可变。
    
    6、如果整数值比较大，可以采用_分割写法
"""
a = 1
b = 15_632_145_632_145
print("a的类型：",type(a))
print("b的类型：",type(b))
print(b)

x = 100
y = 100
print("x的的数据值：", x, " x的地址值：", id(x))
print("y的的数据值：", y, " y的地址值：", id(y))
#上面的地址相同
#下面的地址不同
x = 1000
y = 1000
print("x的的数据值：", x, " x的地址值：", id(x))
print("y的的数据值：", y, " y的地址值：", id(y))
