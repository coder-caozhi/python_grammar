class Person:
    """
        这是一个Person类
    """

    # 定义类的属性，所有实例共享
    home = "earth"

    # 定义初始化的函数
    def __init__(self):
        # 给实例设置一个默认的属性age
        self.age = 18

# 获取类的成员
# 获取类的属性
print(Person.home)
# 获取类的说明文档
print(Person.__doc__)
# 获取类的初始化函数
print(Person.__init__)

# 修改类的属性：只能通过类.属性名的方式
Person.home = "地球"
# 重新获取类的属性
print(Person.home)

# 实例化
p = Person()
# 获取对象的age属性值
print(p.age)
# 通过实例获取类的属性值（不推荐）
print(p.home)

# 通过实例修改类的属性是无法修改的，相当于给当前实例添加了一个新的属性
p.home = "火星"
print(p.home)
# 再创建一个实例
p2 = Person()
# 获取类的属性值
print(p2.home)