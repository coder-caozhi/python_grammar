"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、什么是迭代器？
    迭代器是专门用来遍历容器中的元素的一种特殊的类型，或者特殊的对象(iterator)。
    它专门用于服务可迭代对象(iterable)，通常容器是可迭代对象。
    
    2、迭代器协议
    （1）凡是包含__iter__方法的对象都是可迭代对象(iterable)，该方法的作用是返回一个迭代器对象(iterator)。
    比喻：可迭代对象(iterable)  比喻成  客机（装乘客，元素），  迭代器对象(iterator) 比喻成 空姐（为遍历元素服务）
    （2）任何迭代器对象都必须包含__next__()方法，用于遍历容器中的元素。每一次调用__next__()方法能得到一个元素。
    如果所有的元素都遍历完了，那么就会发生一个 StopIteration 异常。
    迭代器的每一个对象只能是从头到尾 或 从尾到头 走一趟就结束了，除非创建新的迭代器对象。
    
    3、常见的可迭代对象有：列表list，字符串str，集合set，字典dict，元组tuple等
                       open()函数的返回值文件对象
"""
# list_demo = [1,2,3,4,5]
# iterator_obj = list_demo.__iter__()
# while True:
#     try:
#         item = iterator_obj.__next__()
#         print(item)
#     except StopIteration:
#         print("遍历结束")
#         break
#
# str_demo = "hello"
# iterator_obj2= str_demo.__iter__()
# while True:
#     try:
#         item = iterator_obj2.__next__()
#         print(item)
#     except StopIteration:
#         print("遍历结束")
#         break

# with open("hello.txt","r",encoding="UTF-8") as fr:
#     iterator_obj3= fr.__iter__()
#     while True:
#         try:
#             line = iterator_obj3.__next__()
#             print(line,end="")
#         except StopIteration:
#             break

"""
    4、通常情况下，python中不建议我们直接手动调用 __method__魔法方法。
    那么python为__iter__()和__next__()提供了2个对应的内置函数iter()和next()
"""
list_demo = [1,2,3,4,5]
iterator_obj = iter(list_demo) #等价于list_demo.__iter__()
while True:
    try:
        item = next(iterator_obj) #等价于  item =iterator_obj.__next__()
        print(item)
    except StopIteration:
        print("遍历结束")
        break