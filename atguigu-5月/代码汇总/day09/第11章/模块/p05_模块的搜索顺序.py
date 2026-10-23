"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
import sys

"""
当导入一个模块时，会按照以下顺序进行查找：
（1）当前目录。
（2）PYTHONPATH环境变量中的目录。
（3）包含标准 Python 模块以及这些模块所依赖的任何 extension module 的目录。
（4）site-packages - 查找第三方包安装路径

是否可以增加别的搜索路径，或修改搜索路径的顺序？
可以
"""
print("默认的搜索路径：",sys.path)

#sys.path是一个列表
# sys.path.append("d:\\")
sys.path.insert(0,"d:\\")

print("修改后的搜索路径：",sys.path)

import p06_hello
