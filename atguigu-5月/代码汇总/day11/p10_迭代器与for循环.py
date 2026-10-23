"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、for循环本质上是一种语法糖，它的底层其实就是迭代器。
    语法糖（Syntactic Sugar）是编程语言中的一种特性，它指的是在不影响语言功能的前提下，
    为程序员提供更简洁、更易读的语法形式。语法糖本身并不增加语言的功能，而是让代码更容易编写和理解。语法糖的特点：
        - 简化代码：让复杂的操作用更简单的语法表达。
        - 提高可读性：使代码更接近自然语言或逻辑思维。
        - 不改变语义：语法糖只是对底层实现的封装，不会影响程序的实际行为。
        
    2、结论：凡是可以使用iterator迭代器遍历的可迭代对象（包含__iter__方法），就可以使用for循环遍历。
           反过来说，不可以使用iterator迭代器遍历的对象（不包含__iter__方法），就不可以使用for循环遍历。

"""
list_demo = [1,2,3,4,5]
# iterator_obj = list_demo.__iter__()
# while True:
#     try:
#         item = iterator_obj.__next__()
#         print(item)
#     except StopIteration:
#         print("遍历结束")
#         break

for item in list_demo:
    print(item)
