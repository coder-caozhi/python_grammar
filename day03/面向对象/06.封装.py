class Person:
    """
        这是一个Person类
    """

    # 定义类的属性，所有实例共享
    home = "earth"

    # 定义初始化的函数
    def __init__(self,name,age,gender):
        # 实例的公共属性，相当于Java中public修饰的属性
        self.name = name
        # 实例的受保护的属性，相当于Java中protected
        self._age = age
        # 实例的私有属性，相当于Java的private
        self.__gender = gender

    # 定义函数用来获取_age的属性值
    def get_age(self):
        return self._age

    # 定义一个设置_age属性值的函数
    def set_age(self,age):
        self._age = age

    # __gender的get方法
    @property
    def gender(self):
        print("获取__gender属性的get函数被调用了")
        return self.__gender

    # __gender的set方法
    @gender.setter
    def gender(self,gender):
        print("设置__gender属性的set函数被调用了")
        self.__gender = gender

    # email是一个只读属性
    @property
    def email(self):
        return f"{self.name}@atguigu.cn"

    # 定义toString函数
    def __str__(self):
        return f"Person(name={self.name},age={self._age},gender={self.gender})"

# 创建实例
p = Person("王飞龙",18,"女")
# 调用自定义的函数获取_age属性值
print(p.get_age())
# 调用自定义的函数设置_age属性值
p.set_age(24)
# 打印对象
print(p)
# 获取性别
print(p.gender)
# 设置性别
p.gender = "男"
print(p)
# 获取邮箱
print(p.email)
# 设置邮箱
p.email = "wangfeilong@atguigu.cn"
print(p.email)