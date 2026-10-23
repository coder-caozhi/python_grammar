"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    2、读取文件
    步骤：
    （1）打开一个通道，用于读数据
        open()函数
    （2）读数据
    （3）关闭通道，释放资源（强烈建议）
    
    3、不同的读函数
    （1）read()：一次读取整个文件的内容
        如果是纯文本文件，返回一个字符串
        如果是非纯文本文件，返回一个字节串
    （2）read(size)：一次读取size个字符/字节
        对于读取大文件来说，read(size)更合适一点
    （3）readline()：一次读取一行（仅限于纯文本文件）
    （4）readline(size)：一次读取一行（仅限于纯文本文件）中的size个字符
        size<=一行的的字符，那么只读取size个字符
        size>一行的字符，那么只读取一行
    （5）readlines()：读取多行，且返回的是一个列表，并且每一行的换行符也会保留
    （6）readlines(size)：一次读取size个字符所占的行
        size<=一行的的字符，那么只读取一行
        size>一行的的字符，size个字符出现在几行中，就读取几行
    
"""
# fr = open("1.txt","r", encoding="utf-8")#这里"r"可以省略
# data = fr.read()
# fr.close()
#
# print("读取的文件内容：", data)

# fr = open("1.txt","r", encoding="utf-8")
# data = fr.read(10)
# fr.close()
# print("读取的文件内容：", data)

# fr = open("1.txt","r", encoding="utf-8")
# data = fr.readline()
# fr.close()
# print("读取的文件内容：", data)

# fr = open("1.txt","r", encoding="utf-8")
# data = fr.readline(50)
# fr.close()
# print("读取的文件内容：", data)

# fr = open("1.txt","r", encoding="utf-8")
# data = fr.readlines()
# fr.close()
# print("读取的文件内容：", data)

# fr = open("1.txt","r", encoding="utf-8")
# data = fr.readlines(20)
# fr.close()
# print("读取的文件内容：", data)

# fr = open("柴林燕.txt","r", encoding="utf-8") #读文件时，如果文件不存在，会报错，不会自动创建。
# print(fr.read())
# fr.close()

fr = open("documents/test", "r", encoding="utf-8") #读文件时，必须指定文件，不能指定文件夹
lines = fr.readlines()
fr.close()