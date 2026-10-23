"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
1. 创建一个Student类，包含以下内容：
   - 类属性：school_name（学校名称，初始值为"第一中学"）、student_count（学生总数，初始值为0）
   - 实例属性：name（姓名）、age（年龄）、class_name（班级）
2. 在__init__方法中：
   - 初始化实例属性
   - 每次创建学生对象时，让student_count自动增加1
3. 定义实例方法：
   - introduce(self)：打印学生的所有个人信息
   - have_birthday(self)：让学生年龄增加1岁，并打印生日祝福
4. 定义类方法：
   - change_school(cls, new_name)：修改学校名称
   - get_student_count(cls)：返回当前学生总数
5. 定义静态方法：
   - is_valid_age(age)：判断年龄是否在6-18岁之间（包含边界）
6. 创建至少3个学生对象，并依次：
   - 调用introduce()方法
   - 为其中一个学生调用have_birthday()方法
   - 使用类方法修改学校名称
   - 使用类方法查看学生总数
   - 使用静态方法验证几个不同年龄
"""

class Student:
    school_name = "第一中学"
    student_count = 0

    def __init__(self, name, age, class_name):  # 第一个参数是self，都是实例方法
        self.name = name
        self.age = age
        self.class_name = class_name
        Student.student_count += 1  # 在实例方法中，需要访问本类的类属性，需要  类名.类属性

    def introduce(self):
        print(f"姓名：{self.name}，年龄：{self.age}，班级：{self.class_name}，"
              f"学校名称：{Student.school_name}，学生的总人数：{Student.student_count}")

    def have_birthday(self):
        self.age += 1
        print(f"祝{self.name}生日快乐！")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name

    @classmethod
    def get_student_count(cls):
        return cls.student_count

    @staticmethod
    def is_valid_age(age):
        return 6 <= age <= 18

#测试代码
# 6. 创建至少3个学生对象，并依次：
s1 = Student("张三",23,"1班")
s2 = Student("李四",24,"1班")
s3 = Student("王五",25,"2班")
#    - 调用introduce()方法
s1.introduce()
s2.introduce()
s3.introduce()

#    - 为其中一个学生调用have_birthday()方法
s1.have_birthday()
s1.introduce()

#    - 使用类方法修改学校名称
Student.change_school("第一高级中学")
print(Student.school_name)

#    - 使用类方法查看学生总数
print("学生总人数：",Student.get_student_count())

#    - 使用静态方法验证几个不同年龄
print("检验年龄：",Student.is_valid_age(25))
print("检验年龄：",Student.is_valid_age(7))