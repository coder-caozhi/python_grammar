"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    导入其他模块的方式有如下几种：
    1、import 模块名  或  import 模块名 as 别名
       模块名只需要写 xx.py文件的文件名，不需要写扩展名.py
       一旦取了别名，就要用别名
       
    如何使用模块中的函数、变量、类等成员，那么需要用 模块名.成员
"""
# #演示导入p02_my_math_module.py
# import p02_my_math_module
# #演示导入p02_my_shape_module.py
# import p02_my_shape_module as shape
#
# print("和：", p02_my_math_module.add(5,6))
# print("差：", p02_my_math_module.subtract(5,6))
# print("乘积：", p02_my_math_module.multiply(5,6))
# print("商：", p02_my_math_module.divide(5,6))
# print("余数：", p02_my_math_module._remainder(5,6)) #这种约定式的私有，跨模块也可以使用。但是不推荐。
#
# print("画矩形：")
# shape.print_rectangle(8,10)
# print("画菱形：")
# shape.print_diamond(9)
# print("*重复50")
# shape.multiply("*",50)

"""
    2、from 模块名 import 成员 或 from 模块名 import 成员 as 成员的别名
       from 模块名 import 成员1,成员2,成员3 或 from 模块名 import 成员1 as 别名1,成员2 as 别名2,成员3 
       
       如何使用这些成员，直接使用成员名，不需要再加 模块名. 了
       
       总结：import后面是什么，就直接使用什么名
"""
# #演示导入p02_my_math_module.py的add，subtract
# from p02_my_math_module import add,subtract,multiply as num_mul,divide,_remainder
# # #演示导入p02_my_shape_module.py
# from p02_my_shape_module import print_rectangle,print_diamond,multiply as shape_mul
#
# print("和：", add(5,6))
# print("差：", subtract(5,6))
# print("乘积：", num_mul(5,6))
# print("商：", divide(5,6))
# print("余数：", _remainder(5,6))
#
# print("画矩形：")
# print_rectangle(8,10)
# print("画菱形：")
# print_diamond(9)
# print("*重复50")
# shape_mul("*",50)

"""
    （3） from模块 import *
    这里的*代表的是这个模块中的所有“成员”（不包含私有的成员，例如：_成员）
"""
# #演示导入p02_my_math_module.py的add，subtract等
# from p02_my_math_module import *
# # #演示导入p02_my_shape_module.py
# from p02_my_shape_module import *
#
# from p02_my_math_module import multiply as num_mul
# from p02_my_shape_module import multiply as shape_mul
#
# print("和：", add(5,6))
# print("差：", subtract(5,6))
# print("乘积：", num_mul(5,6))
# print("商：", divide(5,6))
# # print("余数：", _remainder(5,6)) #错误
#
# print("画矩形：")
# print_rectangle(8,10)
# print("画菱形：")
# print_diamond(9)
# print("*重复50")
# shape_mul("*",50)

"""
    （4）from 模块 import * + 被导入模块中加__all__变量进行限制
"""

#演示导入p02_my_math_module.py的add，subtract等
from p02_my_math_module import *
# #演示导入p02_my_shape_module.py
from p02_my_shape_module import *

from p02_my_math_module import multiply as num_mul
from p02_my_shape_module import multiply as shape_mul

print("和：", add(5,6))
# print("差：", subtract(5,6))#错误，因为在p02_my_math_module.py文件的__all__变量中没有列出它可以被其他模块使用
print("乘积：", num_mul(5,6))
# print("商：", divide(5,6))#错误，因为在p02_my_math_module.py文件的__all__变量中没有列出它可以被其他模块使用
# print("余数：", _remainder(5,6)) #错误，因为在p02_my_math_module.py文件的__all__变量中没有列出它可以被其他模块使用

print("画矩形：")
print_rectangle(8,10)
# print("画菱形：")
# print_diamond(9)
print("*重复50")
shape_mul("*",50)