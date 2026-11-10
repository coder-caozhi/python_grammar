"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
"""
    simple_text = "hello"
    
    通过翻译把小写转大写
"""
#第一步：制作翻译表
table = str.maketrans({'h':'H', 'e':'E', 'i':'I', 'o':'O', 'u':'U'}) #{'h':'H', 'e':'E', 'i':'I', 'o':'O', 'u':'U'}是字典
#第二步：翻译
simple_text = "hello"
result = simple_text.translate(table)
print("翻译后的结果：", result)

"""
    nums = "1234"
    
    通过翻译把阿拉伯数字转为中文大写数字
"""
# table = str.maketrans({"1":"壹", "2":"贰", "3":"叁"})
# nums = "1234"
# result = nums.translate(table)
# print("翻译后的结果：",result)

"""
    nums = "abc"
    
    处理为：ABC
"""
#如果传两个参数，需要str1和str2为等长的字符串，str1中的每个字符都将映射到str2中相同位置的字符。
table = str.maketrans("abc","ABC")
nums = "abcd"
result = nums.translate(table)
print("翻译后的结果：",result)

"""
    nums = "abc,def,hik"
    
    处理为:ABCDEFHIK
"""
#如果有第三个参数，第3个参数中指定的字符会被删除
# table = str.maketrans("abcdefhijk","ABCDEFHIJK",",")
# nums = "abc,def,hik"
# result = nums.translate(table)
# print("翻译后的结果：",result)

import string
nums = "abc.def,hik-?hil"
table = str.maketrans("","", string.punctuation) #string.punctuation代表所有英文标点符号
result = nums.translate(table)
print("翻译后的结果：",result)