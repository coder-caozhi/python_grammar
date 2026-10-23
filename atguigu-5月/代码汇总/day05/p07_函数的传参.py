"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
    如果函数定义了形参，调用时就要传入对应的实参，传参的形式分为多种：
    1、按位置传参：实参按照位置一一给形参赋值，位置、个数、顺序必须一一对应。
"""
# def func1(name,age,gender):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender}")

# 按照位置传参
# func1("柴林燕",18,"女")
# print(func1("柴林燕", 18, "女")) #不加print，否则也是打印一个None
# func1("chai") #func1() missing 2 required positional arguments: 'age' and 'gender'
# func1("柴林燕",18,"女","北京") #func1() takes 3 positional arguments but 4 were given
# func1("柴林燕","女", 18)

"""
    2、形参设置默认值，称为默认值参数
    def 函数名(形参名1, 形参名2 = 默认值, 形参名3 = 默认值)
        函数体
    一旦某个形参设置了默认值，那么它后面的形参必须都设置默认值
"""
# def func2(name, age=18, gender=None):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender}")
#
# #调用带默认值参数的函数
# # func2()#错误，因为name没有默认值
# func2("柴") #有默认值的形参，就可以不传实参了
# func2("张三",23,"男")
# func2("张三",23)
# # func2("张三","男")#如果按照位置传参，无法越过age参数
# func2("张三",gender="男") #gender="男"就是关键字传参

"""
    3、关键字传参
    def 函数名(形参名1, 形参名2, 形参名3):
        函数体语句
    def 函数名(形参名1, 形参名2 = 默认值, 形参名3 = 默认值)
        函数体
        
    调用函数时，可以写 形参名 = 值，进行关键字传参，此时形参名必须正确。此时顺序无所谓了
"""
# def func3(name, age=18, gender=None):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender}")
#
# func3(name="柴林燕")
# func3(name="柴林燕",age=20)
# func3(name="柴林燕",gender="male")
# func3(name="柴林燕",gender="male",age = 28)
# func3(gender="male",age = 28,name="柴林燕")
# # func3(gender="male",age = 28,xingming="柴林燕") #错误，没有形参名是xingming
# func3("柴林燕",gender="male",age = 28)

"""
    4、强制位置传参和强制关键字传参
    形参列表中加入/，在/之前的必须是按照位置传参
    形参类别中加入*，在*后面的必须是关键字传参
    /和*不要求同时出现在参数列表中
    在/和*之间的参数，可以选择位置传参，也可以选择关键字传参，但是一旦出现关键字传参，后面都得关键字传参
"""
# def func3(name, age=18, /, gender=None, salary=15000, *, tel=None, address=None):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender},薪资：{salary}, 电话：{tel}，地址：{address}")
#
# # func3(name="柴林燕") #错误，/之前的必须是位置传参
# # func3("柴林燕",age=23) #错误，/之前的必须是位置传参
# # func3("柴林燕",23,"女",20000, "10086") #错误，*后面必须是关键字传参
# func3("柴林燕",23,"女",20000, tel="10086",address="北京") #错误，*后面必须是关键字传参
# func3("柴林燕",23,gender="女",salary =20000, tel="10086",address="北京") #错误，*后面必须是关键字传参
# func3("柴林燕",23,"女",salary=20000, tel="10086",address="北京") #错误，*后面必须是关键字传参


"""
    5、解包传参
    函数名(*列表/元组)  将列表或元组的元素一一作为参数值一一传给函数，且是按照位置传参的方式
    函数名(**字典)  将字典的value一一作为参数值一一传给函数，且是关键字传参的方式传入，要求key与形参名一致
"""
# def func5(name, age, gender):
#     print(f"姓名：{name}，年龄：{age}，性别：{gender}")
#
# lst = ["柴林燕", 23, "女"]
# func5(*lst)  # 对lst列表进行解包，将列表的每一个元素作为参数值一一传给func5函数
# data = {"name": "柴林燕", "age": 23, "gender": "美女"}
#
# func5(**data)  # 对data字典进行解包，将字典中的键值对的value作为参数值一一传给func5函数，要求字典的key与形参名一致
# # data = {"name": "柴林燕", "age": 23, "xingbie": "美女"}
# # func5(**data)
#
# # data = {"name": "柴林燕", "age": 23, "gender": "美女", "address":"北京"} #键值对的数量与函数的参数要对应
# # func5(**data)
"""
    6、可变参数
    (1)*参数名：对应的是一个元组
        A：只能按照位置传参
        B：不能设置默认值
        C：后面可以跟其他参数
    (2)**参数名：对应的是一个字典
        A：只能按照关键字传参
        B：不能设置默认值
        C：它后面不能再出现任何参数了
"""
# def func6(name,age, *hobby): #*hobby可以接收0~n个参数值
#     print(f"姓名：{name}，年龄：{age}，爱好：{hobby}")
#
# func6("柴林燕", 23)
# func6("柴林燕", 23, "刷剧")
# func6("柴林燕", 23, "刷剧","跑步","看电影")

#补充：元组如果只有1个元素，也得写,
# t1 = ("张三",)
# print(t1)
# print(type(t1))

# def func6(name,age, **info): #**info表示可以接收0~n个键值对
#     print(f"姓名：{name}，年龄：{age}，其他信息：{info}")
# func6("柴林燕", 23)
# # func6("柴林燕", 23, 20000) #错误，**info只能接受键值对
# func6("柴林燕", 23, salary=20000)
# func6("柴林燕", 23, salary=20000,tel="10086",address="北京")

# def func6(name,age, *hobby, **info):
#     print(f"姓名：{name}，年龄：{age}，爱好：{hobby}，其他信息：{info}")

# func6("柴林燕",23, hobby=("看电影","跑步"), salary=20000,tel="10086")#不对，*hobby只能接受位置传参
# func6("柴林燕",23, "看电影","跑步", salary=20000,tel="10086")
# func6("柴林燕",age=23, "看电影","跑步", salary=20000,tel="10086") #报错，一旦age使用了关键字传参，后面都得关键字传参，但是*hobby只能接受位置传参

# def func6(name,age=18, *hobby, **info):
#     print(f"姓名：{name}，年龄：{age}，爱好：{hobby}，其他信息：{info}")
# func6("柴林燕","看电影","跑步", salary=20000,tel="10086")#错误“看电影"被赋值给了age

# def func6(name, *hobby,age=18, **info):
#     print(f"姓名：{name}，年龄：{age}，爱好：{hobby}，其他信息：{info}")
# func6("柴林燕","看电影","跑步", salary=20000,tel="10086")
# func6("柴林燕","看电影","跑步", age = 23,salary=20000,tel="10086")
# func6("柴林燕","看电影","跑步", salary=20000,tel="10086",age=30)
