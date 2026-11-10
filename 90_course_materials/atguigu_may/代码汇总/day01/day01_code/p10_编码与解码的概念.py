"""
    @Author:Irene
    @Time:2026/5/12
    @Desc:
 """
"""
    1、什么是编码
    将字符串的文本转为对应的整数编码值，就是编码的过程。比喻：把情报转为密文。
    (1)最早的编码表是ASCII表，它规定了128个字符的编码值，编码值的范围[0,127]，
    大家可以适当的记如下几个字符的编码值：
        '0' 编码值是 48， '1' 编码值是49 ...
        'A' 编码值是 64，  'B' 编码值是66 ...
        'a' 编码值是 97，  'b' 编码值是98 ...
    
    (2)后来计算机被传到欧洲，欧洲各个国家用的符号，不一样（法语、德语等）。
    为了统一欧洲的一些国家的字符编码，ISO8859-1，可以表示拉丁系列的字符（256个）
    (3)后面计算机被传到了亚洲，各个国家
    例如：中国， GB2312字符集/字符编码表，台湾地区繁体字编码表 Big5
               GBK 繁体和简体都可以表示
    （3）为了统一全世界常用的文字，引出了万国码字符集 Unicode 
    Unicode对应的 编码处理方式有UTF-8,UTF-16等
    
    2、什么是解码
    将编码值重新解析为文本
    
    3、单个字符的编码和解码（掌握）
    编码：ord(单个字符)
    解码：chr(编码值)
    
    4、多个字符的编码和解码（了解）
    编码：字符串.encode(编码方式) 
    解码：bytes.decode(编码值, 编码方式)
    
"""
letter = 'a'
print("字母：",letter ,"对应的编码值：", ord(letter))
print("编码值23578对应的字符：",chr(23578)) #尚

word = "尚硅谷"
print("尚硅谷对应的编码：", word.encode("UTF-8")) #b'\xe5\xb0\x9a\xe7\xa1\x85\xe8\xb0\xb7'
# for i in word.encode("UTF-8"):
#     print(i)

code = word.encode("UTF-8")
print("code的类型：", type(code)) #<class 'bytes'> 字节数组
# print(code ,"对应的文本：", bytes.decode(code,"UTF-8"))
print(code ,"对应的文本：", bytes.decode(code,"GBK"))

