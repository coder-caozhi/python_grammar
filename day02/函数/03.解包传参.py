# 声明函数
def get_info(name, age):
    print(f"您的姓名是：{name}，您今年{age}岁了")

# 定义列表
my_list = ["关羽",32]
# 定义元组
my_tuple = ("张飞",31)
# 定义字典
my_dict = {"name":"诸葛亮","age":28}

# 调用函数解包传参
get_info(*my_list)
get_info(*my_tuple)
get_info(**my_dict)

