"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
    1、什么是面向对象？
    面向对象是一种编程思想，称为OOP（Object Oriented Program），以对象为中心，代码的最基本结构是类。对象的行为和数据是绑定在一起的。每一个对象是独立的。
    面向过程是另一种编程思想，称为POP（Procedural  Oriented Program ），以函数为中心，代码的最基本的结构是函数。数据与行为是分开。
    例如：把大象装进冰箱的任务
    面向过程：
        def open():
            ...
        def save():
            ...
        def close():
            ...
        
        open()
        save()
        close()
    面向对象：
        class 人:
            def __init__(self,name):
                self.name = name
            def pull(东西):
                print(self.name,"拉东西")
                if 东西是冰箱门:
                    冰箱.open()
                elif 东西是大象:
                    大象.walk()
            def push(东西):
                if 东西是冰箱门:
                    冰箱.close()
                elif 东西是大象:
                    大象.walk()
        class 大象:
            def walk():
                大象走...
        class 冰箱:
            def open():
                ...
            def close():
                ...
            def save():
                ...
        
        r = 人("张三")
        r2 = 人("李四")
        e = 大象("Alice", 5)
        b = 冰箱("格力", 5, 6, 10)
        r.pull(b)
        r.pull(e)
        r.push(e)
        r.push(b)
    
    2、类与对象的概念
    类：一类具有相同特征的事物的抽象描述。=>抽象
    对象：这类事物的一个具体的实例、个体。=>具体
    例如：
        学生类：代表学生这个群体，他们有：姓名、年龄、电话、成绩...，  学习()，吃饭(),....
        教师类：代表教师这个群体，他们有：姓名、年龄、电话、薪资...，  讲授()，吃饭(),....
        
        学生类和教师类都是人。
        人类：他们有：姓名、年龄、电话...， 吃饭(),....
        学生类和教师类分别继承人类，再又新增自己独特的属性和方法
            学生类 继承 人类：成绩...， 学习()，...
            教师类 继承 人类：薪资...， 讲授()，...
            
    3、如何定义类，如何创建对象
    定义类语法格式：
        class 类名:
            类体
    创建对象的语法格式：
        对象名 = 类名()
        对象名 = 类名(参数)
        
    4、类与的对象的关系
    类是创建对象的模板，设计图，对象是类的实例，个体。
    
    
"""
class Person:
    pass
p1 = Person()
p2 = Person()
print(p1) #p1存储了第一个Person对象的首地址
print(p2) #p2存储了第二个Person对象的首地址