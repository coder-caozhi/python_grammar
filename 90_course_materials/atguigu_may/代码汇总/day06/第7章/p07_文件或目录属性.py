"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    第7章的要求：
    （1）读、写文件内容（尽量掌握，尽量熟悉）
    （2）创建文件、删除文件、创建文件夹、删除文件夹.....（能看懂，能查笔记）
    
    1、访问或获取文件或目录的属性
"""
import os,time
# print("test.txt文件大小：", os.path.getsize("documents/test.txt")) #只能获取文件的大小
# print("test.txt文件创建时间：", os.path.getctime("documents/test.txt"))
# print("test.txt文件最后访问时间：", os.path.getatime("documents/test.txt"))
# print("test.txt文件最后修改时间：", os.path.getmtime("documents/test.txt"))
# mtime = time.localtime(os.path.getmtime("documents/test.txt"))
# #占位符，%Y代表4位数字的年，%m代表月....
# print("test.txt文件最后修改时间：", time.strftime("%Y-%m-%d %H:%M:%S", mtime))

# print("test.txt文件是否是文件：", os.path.isfile("documents/test.txt"))#只有文件存在，且是文件类型，才返回True，否则返回False
# print("test.txt文件是否是目录：", os.path.isdir("documents/test.txt"))#只有文件夹存在，且是文件夹类型，才返回True，否则返回False
# print("test.txt文件是否存在：", os.path.exists("documents/test.txt"))#只有文件或文件夹存在，返回True
#
# print("文件名：", os.path.basename("documents/test.txt"))
# print("文件所在目录名：", os.path.dirname("documents/test.txt"))
# print("文件绝对路径：", os.path.abspath("documents/test.txt"))
#
# tuple_result = os.path.split("documents/test.txt")
# print("文件所在目录名：", tuple_result[0])
# print("文件名：", tuple_result[1])
# print("文件名（不带扩展名）：", os.path.splitext(tuple_result[1])[0])
# print("扩展名：", os.path.splitext(tuple_result[1])[1])

print("documents文件夹大小：", os.path.getsize("documents"))#不对，无法获取文件夹的大小