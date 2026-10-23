"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
设计一个图书馆借阅系统，综合运用三大特性：
要求：
- 基类 LibraryItem（封装）：
  - 私有属性：__item_id、__title、__is_borrowed
  - 方法：
    - borrow()：修改__is_borrowed为True
    - return_item()：修改__is_borrowed为False
    - `get_info()：编号：xx，名称：xx，是否可借阅：是/否
- 派生类（继承与多态）：
  - Book：额外属性 author、pages，重写 get_info()
  - DVD：额外属性 director、duration，重写 get_info()
  - Magazine：额外属性 issue_number，重写 get_info()
- 类 Library（组合）：
  - 属性：物品列表
  - 方法：add_item()、remove_item()、search_by_title()、display_available_items()
- 实现多态：单独定义display_item_info(item) 函数能正确显示任何类型物品的信息
"""
class LibraryItem:
    def __init__(self,id,title):
        self.__id = id
        self.__title = title
        self.__is_borrowed = False

    def borrow(self):
        self.__is_borrowed = True

    def return_item(self):
        self.__is_borrowed = False

    def get_info(self):
        return f"编号：{self.__id}，名称：{self.__title}，是否可借阅：{"否" if self.__is_borrowed else "是"}"

    @property
    def id(self):
        return self.__id

    @property
    def title(self):
        return self.__title

    @property
    def is_borrowed(self):
        return self.__is_borrowed

class Book(LibraryItem):
    def __init__(self,id,title,author,pages):
        super().__init__(id,title)
        self.__author = author
        self.__pages = pages

    def get_info(self):
        return super().get_info() + f"，作者：{self.__author}，页数：{self.__pages}"

class DVD(LibraryItem):
    def __init__(self, id, title, director, duration):
        super().__init__(id, title)
        self.__director = director
        self.__duration = duration

    def get_info(self):
        return super().get_info() + f"，导演：{self.__director}，时长：{self.__duration}"

class Magazine(LibraryItem):
    def __init__(self, id, title, issue_number):
        super().__init__(id, title)
        self.__issue_number = issue_number

    def get_info(self):
        return super().get_info() + f"，期刊号：{self.__issue_number}"

class Library:
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def remove_item(self, id):
        index = 0
        while index < len(self.__items): #为了对比上一个练习题，这里用while实现一版
            if self.__items[index].id == id:
                self.__items.pop(index)
            else:
                index += 1
    def search_by_title(self, title):
        results = []
        for item in self.__items:
            if item.title == title:
                results.append(item)
        return results

    def display_available_items(self):
        return self.__items #返回所有图书产品
        # return [item for item in self.__items if not item.is_borrowed] #返回所有可借阅的图书产品

    def borrow(self,id):
        for item in self.__items:
            if item.id == id:
                item.borrow()

    def return_item(self,id):
        for item in self.__items:
            if item.id == id:
                item.return_item()

def display_item_info(item):
    print(item.get_info())

library = Library()
library.add_item(Book(1001,"《python从入门到精通》","尚硅谷", 590))
library.add_item(Book(1002,"《Java从入门到精通》","尚硅谷", 800))
library.add_item(DVD(1003,"《python从入门到精通》","尚硅谷", 600)) #600分钟
library.add_item(Magazine(1004,"《读者》","BJ89628632145"))
print("图书馆的图书：")
for item in library.display_available_items():
    print(item.get_info())

print("查询《python从入门到精通》：",library.search_by_title("《python从入门到精通》"))
print("删除图书：")
library.remove_item(1002)

print("图书馆的图书：")
for item in library.display_available_items():
    print(item.get_info())

print("借书《读者》：")
library.borrow(1004)
print("图书馆的图书：")
for item in library.display_available_items():
    print(item.get_info())

print("还书《读者》")
library.return_item(1004)
print("图书馆的图书：")
for item in library.display_available_items():
    print(item.get_info())
