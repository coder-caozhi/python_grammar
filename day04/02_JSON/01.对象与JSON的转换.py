# =====================================================================
# 01. 对象与 JSON 的转换
# ---------------------------------------------------------------------
# 【JSON 是什么】一种"文本格式"，用来在程序之间传递数据
#                （本质是字符串，所以能写进文件、通过 HTTP 传输）
# 【两个核心函数】
#     json.dumps(Python对象)  → 转为 JSON 字符串（dumps 的 s = string）
#     json.loads(JSON字符串)  → 转回 Python 对象（loads 的 s = string）
# 【类型对照】Python 类型和 JSON 类型的对应关系见本文档末尾
# =====================================================================

import json


# ---------------------------------------------------------------------
# 一、准备一个 Python 对象（字典）
# ---------------------------------------------------------------------
print("=" * 40)
print("一、准备 Python 对象")
print("=" * 40)

python_data = {
    "name": "Tom",
    "age": 18,
    "is_student": True,
    "tags": ["python", "oop", "json"],
    "score": {"math": 95, "english": 88}
}

print(python_data)
print(f"转换之前的类型是：{type(python_data)}")     # 输出：<class 'dict'>


# ---------------------------------------------------------------------
# 二、Python 对象 → JSON 字符串（dumps）
# ---------------------------------------------------------------------
print("=" * 40)
print("二、Python 对象 → JSON 字符串")
print("=" * 40)

python_data_to_json = json.dumps(python_data)
print(python_data_to_json)
# 输出：{"name": "Tom", "age": 18, "is_student": true, "tags": [...], "score": {...}}
print(f"转换之后的类型是：{type(python_data_to_json)}")   # 输出：<class 'str'>

# 注意上面输出的两个变化：
#   True  → true   （JSON 里没有 True / False，是小写的 true / false）
#   'age' → "age"  （JSON 规定只能用双引号，单引号是非法的）


# ---------------------------------------------------------------------
# 三、JSON 字符串 → Python 对象（loads）
# ---------------------------------------------------------------------
print("=" * 40)
print("三、JSON 字符串 → Python 对象")
print("=" * 40)

json_to_python = json.loads(python_data_to_json)
print(json_to_python)
# 输出：{'name': 'Tom', 'age': 18, 'is_student': True, 'tags': [...], 'score': {...}}
print(f"转换之后的类型是：{type(json_to_python)}")        # 输出：<class 'dict'>


# ---------------------------------------------------------------------
# 四、类型对照表（记住这个，转换时就不会懵）
# ---------------------------------------------------------------------
#   Python          →   JSON
#   ---------------------------
#   dict            →   object      {}
#   list / tuple    →   array       []
#   str             →   string      ""
#   int / float     →   number      1 / 1.5
#   True / False    →   true / false
#   None            →   null
#
# 注意：JSON 只支持上面这些类型。
#       像 set、datetime、自定义对象 都不能直接转换，会报 TypeError
