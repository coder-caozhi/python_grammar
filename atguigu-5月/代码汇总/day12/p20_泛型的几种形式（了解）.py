"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
from typing import Literal,TypeVar,Generic

#Literal字面量值
# def set_color(color: Literal["red", "blue", "green"]) -> None:
#     print(f"设置颜色为：{color}")
#
# set_color("red")    # 正常
# set_color("yellow")

# # 1. 泛型列表：明确列表元素是int类型
# def sum_numbers(numbers: list[int]) -> int:
#     return sum(numbers)
#
# # 2. 泛型字典：键是str，值是float
# def get_scores() -> dict[str, float]:
#     return {"math": 95.5, "english": 88.0}
#
# # 3. 泛型元组：固定长度和类型
# def get_point() -> tuple[int, int]:
#     return (10, 20)
#
# # 测试
# print(sum_numbers([1, 2, 3]))  # 输出：6
# print(sum_numbers(["hello","world","python"]))
# print(sum_numbers([1.0, 2.0, 3.3, 4.5]))
# print(get_scores())            # 输出：{'math': 95.5, 'english': 88.0}
# print(get_point())             # 输出：(10, 20)

# # 定义可接受任意类型的类型变量
# T = TypeVar('T') #建议使用大写字母
# # 泛型函数：返回列表中第一个元素
# def first_element(lst: list[T]) -> T: #表示返回值的类型与list的元素类型是同一种类型，所以用用一个字母表示
#     if not lst:
#         raise ValueError("列表不能为空")
#     return lst[0]
#
# # 测试不同类型列表
# print(first_element([1, 2, 3]))    # 输出：1（int类型）
# print(first_element(["a", "b"]))   # 输出：a（str类型）
# print(first_element([3.14, 2.71])) # 输出：3.14（float类型）


# class Animal:
#     def speak(self) -> str:
#         return "..."
#
# class Dog(Animal):
#     def speak(self) -> str:
#         return "Woof!"
#
# class Cat(Animal):
#     def speak(self) -> str:
#         return "Meow!"
#
# # 绑定到 Animal 或其子类
# A = TypeVar('A', bound=Animal) #限定上限，A对应的类型是Animal或它的父类是Animal
#
# def make_sounds(animals: list[A]) -> list[str]:
#     return [animal.speak() for animal in animals]
#
# dogs = [Dog(), Dog()]
# cats = [Cat(), Cat()]
# bears = ["熊大","熊二"]
#
# dog_sounds = make_sounds(dogs)  # ["Woof!", "Woof!"]
# cat_sounds = make_sounds(cats)  # ["Meow!", "Meow!"]
# bear_sounds = make_sounds(bears)


T = TypeVar('T')

class Stack(Generic[T]): #Generic代表通用类型，泛型
    """泛型栈类"""
    def __init__(self) -> None:
        self.items: list[T] = []

    def push(self, item: T) -> None:
        self.items.append(item)

    def pop(self) -> T:
        return self.items.pop()

    def is_empty(self) -> bool:
        return len(self.items) == 0


# 使用示例
int_stack = Stack[int]()  # 指定类型参数
int_stack.push(42)
int_stack.push("hello")
value = int_stack.pop()  # value: int

str_stack = Stack[str]()
str_stack.push("hello")
text = str_stack.pop()  # text: str