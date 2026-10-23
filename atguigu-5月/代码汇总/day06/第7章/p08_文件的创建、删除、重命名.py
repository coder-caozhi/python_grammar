"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
import os

"""
    创建文件：open(文件路径名,"w",encoding="utf-8"))
    创建文件：open(文件路径名,"wb"))
"""
# open("chailinyan.txt","w",encoding="utf-8").close()
# open("chailinyan.jpg","wb").close()

"""
    os.rename(源文件路径名，目标文件路径名)
    shutil.move(源文件路径名，目标文件路径名)
"""
import shutil
# os.rename("chailinyan.txt","柴林燕.txt")
# shutil.move("柴林燕.txt","chailinyan.txt")
# shutil.move("柴林燕.txt","e:\\chailinyan.txt")

"""
    删除文件 os.remove(文件的路径名)，不会去回收站
"""
os.remove("chailinyan.jpg")