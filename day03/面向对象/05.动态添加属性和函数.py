class Person:

    # 限制实例能添加的属性
    __slots__ = ("name", "age","sdy")
    pass

# 定义类函数
@classmethod
def class_method(cls):
    print("这是一个在类外面声明的要动态添加给类的一个类函数")

# 定义一个函数
def study():
    print("好好学习，天天向上")

# 给Person类动态添加属性
Person.home = "地球"
# 获取Person类的类属性值
print(Person.home)

# 给Person类动态添加类函数
Person.cls_method = class_method

# 调用Person类的类函数
Person.cls_method()

# 实例对象
p = Person()
# 给实例动态添加属性
p.age = 18
# 获取实例的属性值
print(p.age)

# 给实例动态添加函数
p.sdy = study
# 调用实例动态添加的函数
p.sdy()

p.name = "王飞龙"
print(p.name)

# 限制能给实例添加的属性之后再动态添加
p.address = "宏福苑"
print(p.address)

