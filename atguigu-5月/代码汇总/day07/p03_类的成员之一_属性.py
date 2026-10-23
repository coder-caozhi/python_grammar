"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    一、类的成员之一：属性
    1、属性分为：
    （1）类属性：
        定义位置：类中方法(函数)外
        共享还是独立：所有对象共享的
        在类外面如何访问：建议使用 类名.类属性 访问类属性
        在类外面如何修改：只能使用 类名.类属性 = 值
        在本类实例方法（方法的第一个参数是self，都是实例方法）中如何访问：类名.类属性
    （2）实例属性
        定义位置：方法中，一般在__init__方法中
        共享还是独立：每一个对象独立的
        在类外面如何访问：只能通过 对象名.实例属性
        在类外面如何修改它：只能通过 对象名.实例属性 = 值
                只要是对象.属性 = 值，就是修改实例属性
        在本类的实例方法（方法的第一个参数是self，都是实例方法）中如何访问：self.实例属性
"""
class Person:
    home = "地球" #类属性

    # self代表当前对象。__init__方法中self代表你正在创建的哪个Person对象
    # __init__方法的执行是在创建Person对象时自动执行，不需要我们手动调用
    def __init__(self,name,age=18): #(name,age)是形参，是普通的局部变量而已，见名知意
        self.name = name #self.name是实例属性
        self.age = age   #self.age是实例属性
        self.score = 0

    # def __init__(self,n,a=18):
    #     self.name = n
    #     self.age = a

    def show(self): #这里self代表调用当前方法的对象
        #在本类的方法中，使用本类的类属性，使用“类名.类属性”，使用本类的实例属性，使用“self.实例属性”
        print(f"姓名：{self.name}，年龄：{self.age}，住址：{Person.home}，成绩：{self.score}")

p1 = Person("张三")
p2 = Person("李四", 24)

print("类属性的访问：", Person.home)
print("实例属性的访问：", p1.name)
print("实例属性的访问：", p2.name)

Person.home = "火星"
print("类属性的访问：", Person.home) #推荐用它，按照标准来说，用它
print("类属性的访问：", p1.home) #也可以，但不推荐

p1.name = "张三丰"
print("实例属性的访问：", p1.name)
print("实例属性的访问：", p2.name)

p1.home = "金星" #千万不要这么干，这里在python中是会给p1对象动态增加一个实例属性叫做home
print("类属性的访问：", p1.home)
print("类属性的访问：", p2.home)

p1.show()
p2.show()

