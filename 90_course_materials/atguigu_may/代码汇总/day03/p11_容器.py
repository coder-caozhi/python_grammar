"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    1、python中的容器类型非常丰富：
    （1）内置的容器类型（使用它们不需要import）：字符串str,列表list,集合set，元组tuple，字典dict等
    （2）标准库中的容器类型（使用它们需要import）：collections模块中的defaultdict、deque等
    （3）第三方或自定义
    
    学过Java同学，Java有集合框架集，ArrayList，LinkedList，HashMap等
    
    2、python中的容器类型
    （1）可变：列表list，集合set，字典dict，字节数组bytearray
    （2）不可变：字符串str，元组tuple，范围range，字节串bytes，冻结集合frozenset
    
    3、python中的容器类型
    （1）有序：有序是指可以通过索引来访问，即每一个元素有顺序、编号，索引从0开始
        列表list，字节数组bytearray，字符串str，元组tuple，字节串bytes
         字符串str
         "hello"        [0]元素是h，[1]元素是e，[2]元素是l，[3]元素是l，[4]元素是o
         列表list
         [10,20,30,40]  [0]元素是10，[1]元素是20，[2]元素是30，[3]元素是40
    （2）无序：无序是指不可以通过索引来访问
        集合set，字典dict，冻结集合frozenset
    
    4、python中的容器类型
    （1）元素可重复：列表list，字节数组bytearray，字符串str，元组tuple，字节串bytes
    （2）元素不可重复：集合set，字典dict，冻结集合frozenset
"""
# 字符串容器
word = "hello"
print(f"{word=}")
# 修改hello，把e替换为a
# word.replace("e","a")
word = word.replace("e", "a")  # 字符串容器对象不可变，凡是修改，都会产生1个新的字符串对象
print(f"{word=}")

# 元组容器
tuple_demo = (1, 2, 3)
print(f"{tuple_demo=}")
# tuple_demo.append(4)#无法追加
# tuple_demo[0] = 100 #无法修改元素
print(f"{tuple_demo=}")

# 集合
set_demo = {1, 2, 3, 3, 2, 1}  # 元素不可重复
print(f"{set_demo=}")

# 有序和无序
list_demo = [1, 25, 36, 89, 12, 4]
print(f"{list_demo=}")
print("第1个元素是",list_demo[0])
#list_demo=[1, 25, 36, 89, 12, 4]

set_demo = {1, 25, 36, 89, 12, 4}
print(f"{set_demo=}")
# print("第1个元素：",set_demo[0]) #无法通过索引来访问
#set_demo={1, 36, 4, 89, 12, 25}
