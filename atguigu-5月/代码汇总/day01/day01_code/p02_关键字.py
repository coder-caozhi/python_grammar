"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
from keyword import kwlist # 告诉python解释器去哪个 xx.py文件中找kwlist这个变量
                          # from表示从哪个py文件中，import导入xx变量、函数、类等，导入到当前的py文件中使用

"""
    1、什么是关键字？（理解）
    关键字是一些非常重要的单词，它们是python语法的一部分，有着特殊的意义，平时不能乱用。
    2、如何查看有哪些是关键字？
    在keyword模块中有一个变量kwlist，记录了python中所有的关键字
    ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
    'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for',
     'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or',
      'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
    3、大约35个
"""
print(kwlist)
