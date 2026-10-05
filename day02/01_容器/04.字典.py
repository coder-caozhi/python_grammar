# =====================================================================
# 04. 字典
# ---------------------------------------------------------------------
# 【特点】    有序（3.7+）、可变、key 不可重复、值类型不限
# 【创建方式】1. 使用大括号 {key: value}   2. 使用 dict() 函数
# 【获取元素】1. 通过 [key]   2. 通过 get(key)   3. 遍历
# 【场景】    用 key 快速查找对应的 value
# =====================================================================


# ---------------------------------------------------------------------
# 一、使用 {} 创建字典
# ---------------------------------------------------------------------
print("=" * 40)
print("一、使用 {} 创建字典")
print("=" * 40)

my_dict = {"name": "蔡徐坤", "age": 38}
print(my_dict)                    # 输出：{'name': '蔡徐坤', 'age': 38}
print(type(my_dict))              # 输出：<class 'dict'>

my_dict = dict()
#my_dict = {}
print(my_dict)


# ---------------------------------------------------------------------
# 二、使用 dict() 函数创建字典
# ---------------------------------------------------------------------
print("=" * 40)
print("二、使用 dict() 函数创建字典")
print("=" * 40)

my_dict2 = dict(name="吴亦凡", age=35)   # 用 key=value 的形式
print(my_dict2)
print(type(my_dict2))             # 输出：<class 'dict'>


# ---------------------------------------------------------------------
# 三、遍历字典：key / value / 键值对
# ---------------------------------------------------------------------
print("=" * 40)
print("三、遍历字典")
print("=" * 40)

for k in my_dict:                 # 直接遍历 → 拿到的是 key
    print(f"所有的key是：{k}")

for v in my_dict.values():        # 遍历 .values() → 拿到的是 value
    print(f"所有的值是：{v}")

for k, v in my_dict.items():      # 遍历 .items() → 同时拿到 key 和 value
    print(f"{k}:{v}")


# ---------------------------------------------------------------------
# 四、获取与修改元素
# ---------------------------------------------------------------------
print("=" * 40)
print("四、获取与修改元素")
print("=" * 40)

my_dict = {"name": "蔡徐坤", "age": 38}
print(my_dict["name"])            # 通过 [key] 获取，key 不存在会报 KeyError
print(my_dict.get("age"))         # 通过 get(key) 获取，key 不存在返回 None
print(my_dict.get("height", "未填写"))   # get 可以设置"默认值"

my_dict["hobby"] = ["唱歌", "打篮球", "Rap"]   # key 不存在 → 新增
my_dict["age"] = 27               # key 已存在 → 修改
print(my_dict)


# ---------------------------------------------------------------------
# 五、常用函数
# ---------------------------------------------------------------------
print("=" * 40)
print("五、常用函数")
print("=" * 40)

print(my_dict.keys())             # 获取所有的 key
print(my_dict.values())           # 获取所有的 value
print(my_dict.items())            # 获取所有的键值对

del my_dict["hobby"]              # 删除指定的键值对
print(my_dict)

print("name" in my_dict)          # 判断 key 是否在字典中 → True

# setdefault(key, 默认值)：key 不存在才设置，已存在则保持原值不动
my_dict.setdefault("address", "宏福苑")
print(my_dict)

# fromkeys(可迭代对象, 值)：批量创建 key，并统一赋初值
print(my_dict.fromkeys("hello", 88))


# ---------------------------------------------------------------------
# 六、字典推导式：用两个列表快速构建字典
# ---------------------------------------------------------------------
print("=" * 40)
print("六、字典推导式")
print("=" * 40)

my_keys = ["name", "age", "address"]
my_values = ["王飞龙", 24, "洛阳龙门"]
my_dict3 = {k: v for k, v in zip(my_keys, my_values)}   # zip 把两个列表逐一配对
print(zip(my_keys, my_values))    # 输出：<zip object ...>（迭代器）
print(my_dict3)                   # 输出：{'name': '王飞龙', 'age': 24, 'address': '洛阳龙门'}


# ---------------------------------------------------------------------
# 七、setdefault 的应用：把数据按键分组
# ---------------------------------------------------------------------
print("=" * 40)
print("七、setdefault 的应用")
print("=" * 40)

# 数据：[("分类", "具体值"), ...]，目标是把相同分类的值归到一个列表里
data = [("fruit", "apple"), ("fruit", "banana"), ("veg", "carrot")]
group = {}

# for c, v in data：循环变量本身就是"多重赋值目标"，每轮执行 c, v = 当前元组
# 注意：这里的"解包"不需要星号，因为左边 2 个变量正好等于右边元组的 2 个元素
#       （* 只在"元素个数对不上、要收集剩余元素"时才需要，如 c, *rest = (...))
for c, v in data:
    # setdefault(c, []) 的行为分两种情况，但"返回值"都是该 key 对应的列表：
    #   1. c 不存在 → 插入 c: []，并返回这个"新建的空列表"
    #   2. c 已存在 → 忽略默认值 []，原样返回"已有的列表"（不会覆盖）
    # 因为返回的是列表本身，所以可以接着链式调用 .append(v)
    group.setdefault(c, []).append(v)

    # 逐轮跟踪：
    #   第 1 轮 c="fruit", v="apple"  → 新建 {"fruit": []}          → append 后 {"fruit": ["apple"]}
    #   第 2 轮 c="fruit", v="banana" → "fruit" 已存在，返回原列表    → append 后 {"fruit": ["apple", "banana"]}
    #   第 3 轮 c="veg",   v="carrot" → 新建 {"veg": []}            → append 后 {"veg": ["carrot"]}

print(group)                      # 输出：{'fruit': ['apple', 'banana'], 'veg': ['carrot']}

# 错误示范 1：直接 group[c].append(v)
#   → 首次遇到 "fruit" 时 key 还不存在，会报 KeyError
# 错误示范 2：group.get(c, []).append(v)
#   → 不报错但结果是空字典 {}！因为 get 返回的是"临时新建的空列表"，
#     append 完就被丢弃了，没有存回字典里，所以永远存不进去

