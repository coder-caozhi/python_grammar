"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
import abc
import math

"""
练习题3：图形面积计算（多态）
创建一个图形类体系，展示多态特性：
要求：
- 基类 Shape：
  - 定义方法 area() 和 perimeter()，方法体用pass表示
- 派生类：
  - Rectangle（矩形）：属性 width、height
  - Circle（圆形）：属性 radius
  - Triangle（三角形）：属性 a、b、c（三边长）
- 创建函数 print_shape_info(shape)，接收任何形状对象并打印其面积和周长

"""
class Shape(abc.ABC):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass

    def __str__(self):
        return f"面积：{self.area()}，周长：{self.perimeter()}"
        #这里也是多态的体现。因为self代表的不同类型的对象

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    # 重写父类方法的快捷键 Ctrl + O，重写抽象方法的快捷键Ctrl + I
    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

class Triangle(Shape):
    def __init__(self, a, b, c):
        if a<=0 or b<=0 or c<=0 or a+b<=c or b+c<=a or a+c<=b:
            return
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        p = (self.a + self.b +  self.c) /2
        return  math.sqrt(p * (p-self.a) * (p-self.b) * (p-self.c))

    def perimeter(self):
        return self.a + self.b + self.c

# def print_shape_info(shape):
#     s =  str(type(shape))
#     start = s.rindex(".")+1
#     end= s.rindex("'")
#     type_name = s[start:end]
#     print(f"{type_name}的面积：{shape.area()}，周长：{shape.perimeter()}")
#
# print_shape_info(Rectangle(10, 5))
# print_shape_info(Circle(3.0))
# print_shape_info(Triangle(3,4,5))

shapes = [Rectangle(10, 5),Circle(3.0),Triangle(3,4,5)]
for s in shapes:
    print(s)



