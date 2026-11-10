"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    1、写操作：演示写到本地文件中
    步骤：
    （1）打开一个通道，用于写数据
        open()函数
    （2）写数据
    （3）关闭通道，释放资源（强烈建议）
"""
#写一句话到 1.txt
# fw = open("1.txt", "w", encoding="utf-8") #相对路径。相对当前文件的目录，在第7章文件夹中
#                                         #1.txt不存在，会自动创建
# fw.write("我爱尚硅谷")
# fw.close()

# fw = open("1.txt", "w", encoding="utf-8") #1.txt已存在，会覆盖原来的内容
# fw.write("我爱python")
# fw.close()

# fw = open("1.txt", "a", encoding="utf-8") #1.txt已存在，会追加新内容
# fw.write("我爱柴老师")
# fw.close()

# fw = open("test/2.txt", "a", encoding="utf-8")
# fw.write("hello")
# fw.close()

# fw = open("测试/2.txt", "a", encoding="utf-8") #“测试”的文件夹不存在。会报错，不会自动创建文件夹
# fw.write("hello")
# fw.close()

fw = open("documents/test", "w", encoding="utf-8") #无法往文件夹中写入内容，必须指定具体的文件
fw.write("hello world")
fw.close()