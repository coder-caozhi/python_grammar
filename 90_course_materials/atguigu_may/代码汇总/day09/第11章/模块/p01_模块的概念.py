"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    1、什么是模块？
    在python中一个模块是指一个xx.py文件。
    其中可以包含变量、函数和类等。
    通常情况下，我们把能够实现某一特定功能的代码放置在一个文件中作为一个模块。
"""
def say_hello():
    print("hello")
def show():
    print("这是一个模块概念的讲解")

if __name__ == '__main__':
    say_hello()
    show()
# say_hello()
# show()