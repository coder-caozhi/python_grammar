# 声明一个字典对象
import json

python_data = {
    "name": "Tom",
    "age": 18,
    "is_student": True,
    "tags": ["python", "oop", "json"],
    "score": {"math": 95, "english": 88}
}

print(f"Python对象转换之前的类型是：{type(python_data)}")
# 将Python对象转换为JSON字符串
python_data_to_json = json.dumps(python_data)
print(python_data_to_json)
print(f"Python对象转换之后的类型是：{type(python_data_to_json)}")
# 将JSON字符串转换为Python对象
json_to_python = json.loads(python_data_to_json)
print(json_to_python)
print(type(json_to_python))