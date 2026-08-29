# 使用input函数让用户在控制台输入内容，返回的是字符串
# name = input("请输入您的姓名：")
# print(type(name))
# age = input("请输入您的年龄：")
# print(type(age))

# 使用print函数输出内容会自动换行
name = "吴签"
age = 28
salary = 3000.567
print(name)
print(age)
print(salary)
# 输出多个特殊符号
# 输出30个*号
print("*"*30)
# 输出60个等号
print("="*60)

"""
格式化输出：
    1.使用占位符：%
    2.使用format函数
    3.使用f-string（推荐）
"""
print("我叫%s，我今年%d岁，我的工资是每月%.2f元"%(name,age,salary))
print("我叫{}，我今年{}岁，我的工资是每月{}元".format(name,age,salary))
print(f"我叫{name},我今年{age}岁，我的工资是每月{salary}元")
print(f"我叫{name},",end='')
print(f"我的年龄是{age}岁")