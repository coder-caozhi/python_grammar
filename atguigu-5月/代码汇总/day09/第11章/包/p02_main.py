"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    主题：演示导入不同包的模块及其成员来使用
    1、在python中导入包的方式有多种
    （1）import 包名
        import 父包.子包
        
    主要：使用这种方式，需要在被导入包的__init__.py文件中加如下代码：
    from . import 具体的模块名称1,具体的模块名称2
"""
# import mygraphic
#
# #使用mygraphic包中的circle.py模块文件中的area等成员
# print("圆的面积：",mygraphic.circle.area(2.5))
# print("圆的周长：",mygraphic.circle.perimeter(2.5))
#
# print("矩形的面积：",mygraphic.rectangle.area(5,2))
# print("矩形的周长：",mygraphic.rectangle.perimeter(5,2))

"""
    （2）import 包名.模块 
        from 包名 import 模块（这种方式更多）
"""
# from mygraphic import circle,rectangle
# print("圆的面积：",circle.area(2.5))
# print("圆的周长：",circle.perimeter(2.5))
#
# print("矩形的面积：",rectangle.area(5,2))
# print("矩形的周长：",rectangle.perimeter(5,2))

# import mygraphic.circle,mygraphic.rectangle
# print("圆的面积：",mygraphic.circle.area(2.5))
# print("圆的周长：",mygraphic.circle.perimeter(2.5))
#
# print("矩形的面积：",mygraphic.rectangle.area(5,2))
# print("矩形的周长：",mygraphic.rectangle.perimeter(5,2))

"""
    （3）from 包.模块 import 成员
"""
# from mygraphic.circle import area as c_area,perimeter as c_perimeter
# from mygraphic.rectangle import area as r_area,perimeter as r_perimeter
# print("圆的面积：",c_area(2.5))
# print("圆的周长：",c_perimeter(2.5))
#
# print("矩形的面积：",r_area(5,2))
# print("矩形的周长：",r_perimeter(5,2))

"""
    （4）from 包名 import * + 搭配__init__.py中的__all__变量使用
    *在这里代表的是模块名
    __all__变量中定义的是哪些模块可以被使用
    
"""
# from mygraphic import *
# print("圆的面积：",circle.area(2.5))
# print("圆的周长：",circle.perimeter(2.5))
#
# print("矩形的面积：",rectangle.area(5,2))
# print("矩形的周长：",rectangle.perimeter(5,2))

"""
    （5）from 包名.模块名 import *
    *在这里代表的是模块的成员（不包含私有的成员）
"""
from mygraphic.circle import *
print("圆的面积：",area(2.5))

from mymath.basic_arithmetic import *
print("和：", add(5,6))
print("差：", subtract(5,6))
print("乘积：", multiply(5,6))
print("商：", divide(5,6))
# print("余数：", _remainder(5,6)) #错误
