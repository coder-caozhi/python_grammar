# 写文件如果文件不存在会自动创建
# 覆盖写
def write_file(file_path,encoding):
    with open(file_path, mode="w", encoding=encoding) as f:
        # 直接写到一行
        f.write("今天天气好晴朗")
        f.write("处处好风光")
        f.write("\n")
        # 换行写
        f.write("蝴蝶儿忙，蜜蜂也忙\n")
        f.write("小鸟儿忙着，白云也忙\n")

# 追加写
def append_file(file_path,encoding):
    with open(file_path,mode="a",encoding=encoding) as f:
        f.write("\n")
        f.write("爱到心破碎，也别去怪谁\n")
        f.write("只因为相遇太美\n")


# 调用追加写
append_file("test2.txt","utf-8")
