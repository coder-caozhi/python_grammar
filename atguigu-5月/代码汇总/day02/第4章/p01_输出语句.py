"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
    输出语句的形式有几种：
    1、普通输出
    print(参数1,参数2,参数3,...)  
    print是一个函数，调用/使用函数时，写在()中的都是参数。
    默认情况下：print会各个参数之间加空格输出。如果参数之后的分隔符不想是空格，那么可以通过sep="分隔符"
             print会在本条输出语句结束之后换行。如果输出结束后，不想换行，可以通过end="结束符"
"""
# print(1,2,3,4)
# print(10,20,30,40)

# print(1,2,3,4, sep=",", end="\t")
# print(1,2,3,4, sep="-")

"""
    2、格式化输出
    （1）print("内容"%(对应的值)) + %占位符
    内容中通过%s,%d,%f来占位
"""
# name = "柴林燕"
# age = 18
# gender = "女"
# height = 45.68651
# print("姓名：%s，年龄：%d，性别：%s，体重：%.2f"%(name,age,gender,height))

"""
    （2）print() + format
    形式一：print("内容{},内容{}".format(对应的值))
    形式二：print("内容{0},内容{1}".format(对应的值))
        有位置之后，可以显示值多次，而且顺序可以自由控制
    形式三：print("内容{别名},内容{别名}".format(别名=值1,别名=值2))
        有别名之后，可以显示值多次，而且顺序可以自由控制
    形式四：以上三种形式还可以搭配格式化控制
"""
# name = "柴林燕"
# age = 18
# gender = "女"
# weight = 45.68651
# print("姓名：{}，年龄：{}，性别：{}，体重：{}".format(name,age,gender,weight))
# print("姓名：{0}，年龄：{1}，性别：{2}，体重：{3}".format(name,age,gender,weight))
# print("体重：{}，姓名：{}，年龄：{}，性别：{}".format(name,age,gender,weight))
# print("体重：{3}，姓名：{0}，年龄：{1}，性别：{2}".format(name,age,gender,weight))
#
# x = 1
# y = 2
# print("x={0},y={1}，如果交换的话，交换后的结果会是x={1},y={0}".format(x,y))

# print("体重：{w}，姓名：{name}，年龄：{a}，性别：{g}".format(name=name,a=age,g=gender,w=weight))

# print("姓名：{}，年龄：{}，性别：{}，体重：{:.2f}".format(name,age,gender,weight))
# print("姓名：{0}，年龄：{1}，性别：{2}，体重：{3:.2f}".format(name,age,gender,weight))
# print("体重：{w:.2f}，姓名：{name}，年龄：{a}，性别：{g}".format(name=name,a=age,g=gender,w=weight))

"""
    （3）print(f"内容")  推荐用它
"""
name = "柴林燕"
age = 18
gender = "女"
weight = 45.68651
# print(f"姓名：{name}，年龄：{age}，性别：{gender}，体重：{weight}")
# print(f"姓名：{name}，年龄：{age}，性别：{gender}，体重：{weight:.2f}")
# print(f"姓名：{name:<20}，年龄：{age:<20}，性别：{gender:<20}，体重：{weight:<20.2f}")
# print(f"姓名：{name:^20}，年龄：{age:^20}，性别：{gender:^20}，体重：{weight:^20.2f}")

print(f"{'性别':^20}{'年龄':^20}{'体重':^20}")
print(f"{name:^20}{age:^20}{weight:^20}")