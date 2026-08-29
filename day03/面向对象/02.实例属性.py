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

# 实例化
p = Person("蔡徐坤",27,"男")
# 获取公共属性name的属性值
print(p.name)
# 获取受保护的属性_age的属性值
print(p._age) # 通过实例可以获取_age的属性值，但是不推荐，建议通过调用公共函数获取
# 获取私有的属性__gender的属性值，通过实例.属性名的方式报错，可以通过 实例._类名__属性名 方式获取（不推荐）
print(p._Person__gender)
# 修改属性值
p.name = "吴亦凡"
p._age = 35
print(p.name)
print(p._age)

