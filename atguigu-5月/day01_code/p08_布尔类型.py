"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
"""
    1、布尔类型只有2个值：True，False
    2、布尔类型bool，在python中属于int的子类型，可以与整数、小数进行算术计算
    
    type(变量)查看变量中数据值的类型
    isinstance(变量，类型)查看该变量的值是属于这个类型的吗
    
    True底层对应的是1，False对应的是0
    
    3、非0，非空都是True
       0，空都是False
       空：""（空字符串）, None（特殊值空值）, []（空列表）等
"""
a = True
print("a变量的值：",a, "a的类型：", type(a))
print(isinstance(a, bool))
print(isinstance(a, int))

print(a + 1)

num = 100
if num: #非0等价于True， if True才是条件成立，执行对应的语句
    print("条件成立1")

num = 0
if num: #0等价于False， if False表示条件不成立，不执行对应的语句
    print("条件成立2")