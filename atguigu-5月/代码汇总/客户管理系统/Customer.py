"""
    客户类
"""
import re


class Customer:
    """客户类"""

    def __init__(self, id, name, age, phone, email):
        """
        初始化客户信息
        :param id: 客户编号
        :param name: 客户姓名
        :param age: 客户年龄
        :param phone: 客户手机号
        :param email: 客户邮箱
        """
        self.id = id
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email

    @staticmethod
    def check_id(c_id):
        """
        检查编号是否为正整数
        :param id: 客户编号
        :return: True/False
        """
        return c_id.isdigit() and int(c_id) > 0

    @staticmethod
    def check_name(c_name):
        """
        检查姓名是否为字符
        :param name: 客户姓名
        :return: True/False
        """
        return c_name.isalpha()

    @staticmethod
    def check_age(c_age):
        """
        检查年龄是否为合法年龄值
        :param age: 客户年龄
        :return: True/False
        """
        return c_age.isdigit() and 0 < int(c_age) < 120

    @staticmethod
    def check_phone(c_phone):
        """
        检查手机号是否合法
        :param phone: 客户手机号
        :return: True/False
        """
        return re.match(r"^(13[0-9]|14[01456879]|15[0-35-9]|16[2567]|17[0-8]|18[0-9]|19[0-35-9])\d{8}$", c_phone) is not None

    @staticmethod
    def check_email(c_email):
        """
        检查邮箱是否合法
        :param email: 客户邮箱
        :return: True/False
        """
        return re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", c_email) is not None

    def __str__(self):
        """打印客户信息"""
        return (f"Id: {self.id:<5}, Name: {self.name:<10}, Age: {self.age:<5}, Phone: {self.phone:<15}"
                f", Email: {self.email:<25}")
