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

    # 定义类函数
    @classmethod
    def class_method(cls):
        """
            类函数可以获取类属性
        :return: 类的属性值
        """
        print(f"类的属性home的值是：{cls.home}")

    # 定义静态函数
    @staticmethod
    def static_method():
        """
            静态函数通常作为工具函数
        :return:
        """
        print("调用了静态函数")

    # 实例函数
    def eat(self):
        print(f"{self.name}正在吃东西")

    # 实例函数
    def drink(self):
        print(f"{self.name}正在喝饮料")

    # 在控制台按照指定格式打印实例
    def __str__(self):
        """
            相当于Java中的toString方法
        :return:
        """
        return f"Person(name={self.name}, age={self._age}, gender={self.__gender})"


# 实例化
p = Person("吴亦凡",35,"男")

# 控制台打印实例
print(p)

# 调用实例函数
p.eat()
p.drink()

# 调用类函数
Person.class_method()

# 调用静态函数
Person.static_method()
