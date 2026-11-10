"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
    自定义模块
"""
__all__ = ["add","multiply"]

def add(a,b):
    return a+b

def subtract(a,b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def _remainder(a,b): # 为后面演示需要，故意以_开头
    return a%b