# 读取文件如果文件不存在或报错：FileNotFoundError
# 定义一个读取小文件的函数
def read_small_file(file_path,mode,encoding):
    with open(file_path, mode=mode, encoding=encoding) as f:
        # 读文件
        content = f.read()
        print(content)

# 定义一个读取大文件的函数
def read_big_file(file_path,mode,encoding):
    with open(file_path, mode=mode, encoding=encoding) as f:
        for line in f.readlines():
            # 去除每一行末尾的换行符
            line_strip = line.rstrip("\n")
            print(line_strip)


# 调用读取小文件的函数
# read_small_file("test.txt","r","utf-8")
# 调用读取大文件的函数
read_big_file("test.txt","r","utf-8")