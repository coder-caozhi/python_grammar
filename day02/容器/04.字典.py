"""
    字典
        特点：
            有序、可变、key不可重复、值类型不限
        创建方式：
            1.使用大括号{key:value}
            2.使用dict函数
        获取元素的方式：
            1.通过[key]
            2.通过get(key)
            3.遍历
"""
# 使用{}创建字典
my_dict = {"name":"蔡徐坤","age":38}
print(type(my_dict))
# 使用dict函数创建字典
my_dict2 = dict(name="吴亦凡",age=35)
print(type(my_dict2))

# 获取所有的key
for k in my_dict:
    print(f"所有的key是：{k}")
# 获取所有的值
for v in my_dict.values():
    print(f"所有的值是：{v}")
print(my_dict.items())
# 获取key和value
for k,v in my_dict.items():
    print(f"{k}:{v}")
# 使用[key]获取值
print(my_dict["name"])
# 使用get(key)获取值
print(my_dict.get("age"))
# 添加值
my_dict["hobby"] = ["唱歌","打篮球","Rap"]
# 修改值
my_dict["age"] = 27
print(my_dict)

print("="*30)

# 常用函数
# 获取所有的key
print(my_dict.keys())
# 获取所有的值
print(my_dict.values())
# 获取所有键值对
print(my_dict.items())
# 删除值
del my_dict["hobby"]
print(my_dict)
# 判断是否是该容器的成员
print("name" in my_dict)
# 获取值，如果没有设置默认值
my_dict.setdefault("address","宏福苑")
print(my_dict)
# 快速创建字典，统一初始化值
print(my_dict.fromkeys("hello",88))

# 推导式
# 使用两个列表快速构建字典
my_keys = ["name","age","address"]
my_values = ["王飞龙",24,"洛阳龙门"]
my_dict3 = {k: v for k, v in zip(my_keys, my_values)}
print(zip(my_keys,my_values))
print(my_dict3)

# setdefault函数的应用
data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
group = {}
for c , v in data:
    # 根据遍历到的c从group字典中获取值，没有就设置默认值为空列表，然后王列表中添加遍历到的v
    group.setdefault(c,[]).append(v)
# 在控制台打印group
print(group)