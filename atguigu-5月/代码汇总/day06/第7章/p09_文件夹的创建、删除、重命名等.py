"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
import os
import shutil

"""
    创建文件夹：
    （1）os.mkdir(文件夹的路径名)
    （2）os.makedirs(多级的文件夹的路径名)
    
"""
# os.mkdir("尚硅谷")
# os.mkdir("第六天\\代码\\python")#相当于想要创建python文件夹，如果第六天\\代码不存在就报错
# os.makedirs("第六天\\代码\\python")

"""
    获取当前工作目录：os.getcwd() ：current work directory
    切换文件夹：os.chdir(新目录)：change directory
"""
# print(os.getcwd())
# #切换到第六天\\代码\\python
# os.chdir("第六天\\代码\\python")
# print(os.getcwd())
# open("aaa.txt","w").close() #相对当前的工作目录创建了aaa.txt

"""
    删除目录
    - os.rmdir：删除一级空目录
    - os.removedirs：删除多级空目录
    - shutil.rmtree：递归删除非空目录（谨慎使用）

"""
# os.rmdir("第六天\\代码\\python")
# os.rmdir("尚硅谷")
# os.rmdir("第六天\\代码\\python")
# os.removedirs("第六天\\代码\\python")
# shutil.rmtree("documents")

"""
    遍历目录
    - os.listdir：不递归遍历子目录，返回一个列表，而且只遍历一层
    - os.walk：递归遍历子目录
"""
# print(os.listdir("documents"))
# print(os.walk("documents")) #<generator object walk at 0x00000235840B9010>这是一个生成器对象，也是一个可迭代的对象
# for f in os.walk("documents"): #f是一个元组对象
#     print(f)
#f的元组(当前目录， [当前目录下的所有子目录], [当前目录下的所有文件])

"""
    获取目录总大小：
"""
# def get_dir_size(pathname):
#     if os.path.isfile(pathname):
#         return os.path.getsize(pathname)
#     if os.path.isdir(pathname):
#         total = 0
#         list_demo = os.listdir(pathname)
#         for f in list_demo:#f这里可能是一个文件，也可能是一个文件夹
#             total += get_dir_size(os.path.join(pathname, f)) #拼接当前pathname路径 + f的路径
#         return total
#     return 0
# print("目录总大小：",get_dir_size("documents"))

# print("目录总大小：",  sum(os.path.getsize(os.path.join(root,f)) for root,dirs,files in os.walk("documents") for f in files))
"""
    (1)for root,dirs,files in os.walk("documents")，递归遍历documents的子目录或文件
    documents ['test'] ['2.txt']
    documents\test ['0511班', '尚硅谷'] ['1.txt']
    documents\test\0511班 [] ['day06_01晨考题.mp4']
    documents\test\尚硅谷 [] ['hello.txt']
    
    (2)for f in files，遍历每一层目录中的文件
         ['2.txt']
         ['1.txt']
         ['day06_01晨考题.mp4']
         ['hello.txt']
         这些列表中每一个文件
    (3)os.path.join(root,f)
        documents\2.txt
        documents\test\1.txt
        documents\test\0511班\day06_01晨考题.mp4
        documents\test\尚硅谷\hello.txt
    (4)os.path.getsize(os.path.join(root,f))
         documents\2.txt的文件大小
        documents\test\1.txt的文件大小
        documents\test\0511班\day06_01晨考题.mp4的文件大小
        documents\test\尚硅谷\hello.txt的文件大小
    (5)sum求这些文件大小的总和
       
"""
# for root,dirs,files in os.walk("documents"):
#     print(root,dirs,files)

"""
    复制文件夹：shutil.copytree(原文件夹，新文件夹)
"""
shutil.copytree("documents","documents_copy")