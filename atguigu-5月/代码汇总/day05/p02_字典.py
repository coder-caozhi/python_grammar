"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
    1、字典dict特点：
    （1）字典存储(key,value)键值对或映射关系
    之前的列表、集合、字符串、元组等，都是存储一组独立的元素（比喻：单身party），只有字典存储键值对（比喻：情侣party）。
    （2）无序：不可以通过索引操作它
        虽然3.7+之后说字典可以体现插入顺序，但是这个插入顺序是依赖于链表结构来维护的，不是在哈希表的数组中按顺序存储。
    （3）可重复：
        key：不可重复
        value：可以重复
    （4）可变
        增加新的键值对，可以删除键值对，可以修改value（但不可以修改key）
    （5）对应的数据结构：哈希表
    
    2、如何创建字典
    （1）{key:value , key:value}
    一般来说，key都是选择不可变类型，而且是可哈希的类型。因为字典需要根据key的哈希值来决定(key,value)存在哈希表中什么位置。
    通常选择字符串作为key。
    （2）dict(key=value, key=value)
    （3）dict([(key, value), (key, value)])
    （4）空字典：{}， dict()
    
"""
# dict_one = {"name":"chailinyan", "age":18, "gender":"女"}
# print(dict_one)
#
# dict_two = dict(name="chailinyan", age=18, gender="女")#当我们学完函数之后，这里有一个知识点，叫做关键字传参。参数名类似于变量名，不能加引号
# print(dict_two)
#
# dict_three = dict([("name","chailinyan"), ("age",18),("gender","女")])
# print(dict_three)
#
# dict_four = {} #空字典
# print(dict_four)
# print(type(dict_four))
# dict_five = dict() #空字典
# print(dict_five)

"""
    3、增删改查遍历
    （1）添加
    字典名["key"] = value
"""
# dict_demo = {}
# print(f"原字典：{dict_demo}")
# dict_demo["name"] = "chailinyan"
# print(f"添加了一对键值对之后字典：{dict_demo}")
# dict_demo["age"] = 18
# print(f"添加了一对键值对之后字典：{dict_demo}")

"""
    （2）删除
    del 字典名["key"]
    字典名.pop("key")
    字典名.popitem()：删除末尾的键值对
    字典名.clear()：清空
"""
# dict_demo = {"name": "chailinyan", "age": 18, "gender": "女", "tel": "10086", "address": "北京"}
# print(f"原字典：{dict_demo}")
#
# del dict_demo["gender"]
# print(f"删除gender对应键值对：{dict_demo}")
#
# dict_demo.pop("age")
# print(f"删除age对应的键值对：{dict_demo}")
#
# dict_demo.popitem() #删除末尾的键值对（按照遍历/添加顺序来说，最后一对）
# print(f"删除一对键值对：{dict_demo}")
#
# dict_demo.clear()
# print(f"清空：{dict_demo}")

"""
    （3）修改
    字典名["key"] = value  #如果这个键值对不存在，那么会新增一对键值对，如果key已存在，新value会覆盖原来的value
    字典名.update({"key":value,"key2":value2}) ：同时更新多对键值对的value。如果有新的键值对，也会新增到字典中。
    字典名.setdefault(key, 默认value)：如果key存在，不新增不修改。如果key不存在，没有指定value,value默认值是None，指定了value就指定的来。
"""
# dict_demo = {"name": "chailinyan", "age": 18, "gender": "女", "tel": "10086"}
# print(f"原字典：{dict_demo}")
#
# dict_demo["age"] = 20
# print(f"修改年龄之后：{dict_demo}")
#
# dict_demo.update({"gender": "美女","tel":"110", "address": "北京"})
# print(f"修改性别等之后：{dict_demo}")
#
# dict_demo.setdefault("name")
# print(f"修改name之后：{dict_demo}") #没变
#
# dict_demo.setdefault("name","Irene")
# print(f"修改name之后：{dict_demo}") #没变
#
# # dict_demo.setdefault("salary")
# # print(f"修改salary之后：{dict_demo}") #新增了"salary":None
#
# dict_demo.setdefault("salary",26000)
# print(f"修改salary之后：{dict_demo}") #新增了"salary":26000

"""
    （4）查询
    根据key查询value：  字典名["key"]  key不存在报错
                       字典名.get("key") key不存在，返回None
    查询所有的key ： 字典名.keys() 返回所有key组成的列表           
    查询所有的value ： 字典名.values() 返回所有value组成的列表
    查询所有的(key,value)：字典名.items() 返回所有(key,value)组成的列表 
    查询key是否存在字典中： key in 字典名
    查询键值对的数量：len(字典名)
    
"""
# dict_demo = {"name": "chailinyan", "age": 18, "gender": "女", "tel": "10086"}
# print(f"原字典：{dict_demo}")
#
# print(f"查询name对应的value：{dict_demo['name']}")
# # print(f"查询address对应的value：{dict_demo['address']}") #报错
# print(f"查询name对应的value：{dict_demo.get("name")}")
# print(f"查询address对应的value：{dict_demo.get('address')}")#key不存在，返回None
#
# print(f"查询所有的key：{dict_demo.keys()}")
# print(f"查询所有的value：{dict_demo.values()}")
# print(f"查询所有的(key,value)键值对：{dict_demo.items()}")
# print(f"查询name在不在字典中：", "name" in dict_demo)
# print(f"查询chailinyan在不在字典中：", "chailinyan" in dict_demo) #False，无法直接判断value是不是在字典中
# print(f"查询chailinyan在不在字典中：", "chailinyan" in dict_demo.values()) #True
# print(f"键值对的数量：{len(dict_demo)}")

"""
    （5）遍历
    形式一：
        for key in 字典名: #key是一个变量名，自己取
            代码
    形式二：
        for value in 字典名.values(): 
            代码
    形式三：
        for key,value in 字典名.items():   #遍历items()得到的每一对键值对是(key,value)，这里相当于解包
            代码
"""
# dict_demo = {"name": "chailinyan", "age": 18, "gender": "女", "tel": "10086"}
# print("遍历所有key：")
# for key in dict_demo:
#     print(key)
#
# print("遍历所有value：")
# for value in dict_demo.values():
#     print(value)
#
# print("遍历所有键值对：")
# for key,value in dict_demo.items():
#     print(key,value)

"""
    4、推导式
    （1）列表推导式：[表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件]
    （2）集合推导式：{表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件}
    （3）字典推导式：{key的表达式:value的表达式 for 变量 in 可迭代对象 if 条件 for 变量 in 可迭代对象 if 条件}
    （4）生成器推导式：后面再讲
"""
# code = [97, 98, 99, 100]
# letter = ['a', 'b', 'c', 'd']
# dict_demo = {key: value for key in code for value in letter}
# print(dict_demo)
#{97: 'd', 98: 'd', 99: 'd', 100: 'd'}
"""
    dict_demo = {key: value for key in code for value in letter} 
    等级代码：
    dict_demo = {}
    for key in code:
        for value in letter:
            dict_demo[key] = value
    循环嵌套：外循环循环1次，内循环循环一轮。
        即当key=97，value依次是'a','b','c','d' 最后只留下'd' key不能重复，导致覆盖
        即当key=98，value依次是'a','b','c','d' 最后只留下'd' key不能重复，导致覆盖
"""
code = [97, 98, 99, 100]
dict_demo = {key: chr(key) for key in code}
print(dict_demo)