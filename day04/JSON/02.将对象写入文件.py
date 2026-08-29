# 声明一个列表
import json

user_list = [
    {"name": "Tom", "age": 18, "city": "北京"},
    {"name": "Jerry", "age": 20, "city": "上海"},
    {"name": "Alice", "age": 19, "city": "广州"}
]

# 将列表写入一个json文件
with open('python_data.json', 'w', encoding='utf-8') as f:
    # 将列表写入json文件
    # 关键参数：
    # - ensure_ascii=False：保留中文
    # - indent=4：格式化输出（缩进4个空格），便于阅读/调试（生产环境可省略，减少文件体积）
    json.dump(user_list, f, indent=4, ensure_ascii=False)

# 读取json文件获取列表
with open('python_data.json', 'r', encoding='utf-8') as f:
    # 加载文件
    user_list = json.load(f)
    print(user_list)
