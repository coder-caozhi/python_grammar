"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
父类：又称为基类、超类
子类：又称为派生类

要求：
- 基类 Employee（封装）：
  - 私有属性：__name、__id、__base_salary
  - 公开方法：get_details()、calculate_salary()（基本工资）
- 派生类：
  - Manager：额外属性 bonus（奖金），重写 calculate_salary()
  - Developer：额外属性 project_count，重写 calculate_salary()（按项目数量计算）
  - Intern：额外属性 mentor（指导人），重写 calculate_salary()（固定津贴）
- 公司类 Company（组合）：
  - 属性：员工列表
  - 方法：add_employee()、remove_employee()、get_total_salary()、list_all_employees()
"""
class Employee:
    def __init__(self, name, id, base_salary):
        self.__name = name
        self.__id = id
        self.__base_salary = base_salary

    def get_details(self):
        return f"姓名：{self.__name}，编号：{self.__id}，基本工资：{self.__base_salary}"

    def calculate_salary(self):
        return self.__base_salary

    @property
    def base_salary(self):
        return self.__base_salary

    @property
    def id(self):
        return self.__id

class Manager(Employee):
    def __init__(self, name, id, base_salary,bonus):
        super().__init__(name, id, base_salary)
        self.__bonus = bonus

    def calculate_salary(self):
        return self.base_salary + self.__bonus #错误，因为父类的self.__base_salary不能在子类中直接使用

    def get_details(self):
        return super().get_details() + f"，奖金：{self.__bonus}"

class Developer(Employee):
    def __init__(self, name, id, base_salary,project_count):
        super().__init__(name, id, base_salary)
        self.__project_count = project_count

    def calculate_salary(self):
        return self.base_salary + self.__project_count * 5000

    def get_details(self):
        return super().get_details() + f"，项目数量：{self.__project_count}"

class Intern(Employee): #实习生
    def __init__(self, name, id, base_salary,mentor):
        super().__init__(name, id, base_salary)
        self.__mentor = mentor

    def calculate_salary(self):
        return self.base_salary + 1000
    def get_details(self):
        return super().get_details() + f"，指导人：{self.__mentor}"

#快速折叠代码：Ctrl+Shift+ -
#快速展开折叠代码：Ctrl+Shift+ +
class Company:
    def __init__(self):
        self.__employees = []

    def add_employee(self, employee):
        self.__employees.append(employee)

    def remove_employee(self ,id):
        for employee in self.__employees: #员工编号具有唯一性，找到一个删除后就结束
            if employee.id == id:
                self.__employees.remove(employee)
                break
    def get_total_salary(self):
        return sum(e.calculate_salary() for e in self.__employees)

    def list_all_employees(self):
        return self.__employees

#测试
company = Company()
company.add_employee(Manager("小范",1001, 20000, 50000))
company.add_employee(Developer("小张",1002,15000,5))
company.add_employee(Intern("小郝",1003,10000,"小范"))
# print(company.list_all_employees())
for employee in company.list_all_employees():
    print(employee.get_details())

print("删除1002员工：")
company.remove_employee(1002)
for employee in company.list_all_employees():
    print(employee.get_details())

print("薪资总和：", company.get_total_salary())