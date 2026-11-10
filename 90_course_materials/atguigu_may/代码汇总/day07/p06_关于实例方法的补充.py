"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    回顾：在类外面如何访问时：
    实例方法：对象.实例方法()  更推荐，更标准
    类方法：类名.类方法()
    静态方法：类名.静态方法()
    
    有人就提出，能不能统一一下它们的调用方式，都用类名.方法()？（了解）
    python接收了这个提议，支持 “类名.方法()”形式调用所有方法，
    实例方法：类名.实例方法(对象,其余参数)
    类方法：类名.类方法()
    静态方法：类名.静态方法()
"""
class Person:
    home = "地球"

    def __init__(self, name):
        self.name = name

    """
        当我们用 对象.实例方法() 的方式调用时，第一个参数不需要传，python解释器会自动将调用方法的对象赋值给self。
        当我们用 类名.实例方法(）的方式调用时，第一个参数必须手动传，对象给self。
        即要让self获取到当前对象的引用，即地址，才能获取到当前对象的属性信息等。
    """
    def eat(self): #实例方法
        print(f"{self.name}在吃饭，我现在{Person.home}")

    @classmethod
    def show(cls): #类方法
        print(f"我是一个人，我住在{cls.home}") #cls等价于Person

    @staticmethod
    def func(): #静态方法
        print(f"我就是一个普通的方法，{Person.home}")#可以访问类属性，但是一般不会这么干

#方式一：调用eat()，也是推荐的方式
p =  Person("张三")
p.eat()

#方式二：调用eat()，可以了解
Person.eat(p)