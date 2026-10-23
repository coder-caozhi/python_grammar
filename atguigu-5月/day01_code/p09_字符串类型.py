"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
"""
    1、什么是字符串？
    字符串就是文本，一串字符。
    可以是空字符串，""，''，
    注意如果单引号或双引号里面有空格，那不是空字符串
    
    2、字符串分为单行文本和多行文本
    单行文本："内容", '内容'
    多行文本： ''' 内容 ''' 
"""
'''
    多行文本 """内容"""
'''
# if "":
#     print("空字符串1")
# if " ": #不是空字符串
#     print("空字符串2")

"""
    3、特殊的转义字符（了解）
    无法用1个字母表示的符号，需要转义，例如：换行符、制表符等。常见的转义字符有这些：
    换行符：\n 
    制表符：\t
    回车结束符：\r
    退格键：\b
    斜杆本身：\\
    转义单引号：\'
    转义双引号：\"
    
    在多行文本中有一个特殊的转义，表示不换行，以\结尾
    
"""
# print("\"") #了解
# print('"')
# print('\'')#了解
# print("'")
# print("\\")

# print("hello\nworld\npython")
print("hello\tworld\tpython")
print("chai\tlin\tyan")
print("a\tb\tc")

# print("hello\rworld\rhi")
# print("hello\bworld\bhi")

# info = """
#     hello\
#     world\
#     python\
# """
# print(info)

