"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import re
import string

"""
    1、什么是正则？
    正则：一段文本的规则
    例如：密码规则，要求有大写字母、小写字母、特殊符号组成
         手机号码的规则：11位数字，而且13x,14x等
    2、什么是正则表达式？
    定义正则的表达式，定义文本规则的表达式。
    表达式组成的元素，符号等如下：
    看笔记
    
    3、如下python的函数与正则有关
    Python的re模块提供了正则表达式匹配操作。re模块中提供了一些方法用于查找或处理字符串。
    - re.search(pattern, string, flags)：扫描整个 string 查找正则表达式 pattern 产生匹配的第一个位置，并返回相应的 Match。
                        如果字符串中没有与模式匹配的位置则返回 None。
    - re.match(pattern, string, flags)：如果 string 开头的零个或多个字符与正则表达式 pattern 匹配，则返回相应的 Match。
                    如果字符串开头与模式不匹配则返回 None。
    - re.findall(pattern, string, flags)：返回 pattern 在 string 中的所有非重叠匹配，以字符串列表或字符串元组列表的形式。
            对 string 的扫描从左至右，匹配结果按照找到的顺序返回。空匹配也包括在结果中。
    - re.sub(pattern, repl, string, count=0)：返回通过使用 repl 替换在 string 最左边非重叠出现的 pattern 而获得的字符串。
        如果样式没有找到，则不加改变地返回 string。
      - repl 可以是字符串或函数。如果 repl 是一个函数，该函数接受单个 Match 参数，并返回替换字符串。
      - 可选参数 count 是要替换的最大次数；count 必须是非负整数。如果省略这个参数或设为 0，所有的匹配都会被替换。
    - re.split(pattern, string, maxsplit=0)：用 pattern 分开 string 。 如果在 pattern 中捕获到括号，那么所有的组里的文字也会包含在列表里。如果 maxsplit 非零， 最多进行 maxsplit 次分隔， 剩下的字符全部返回到列表的最后一个元素。

    原始字符串：r""，对""中的\ 不进行转义

"""
# #搜索数字
# text_one = "今天是2026年1月25日，天气不错。2026年5月1日不知道天气怎么样？"
# print(re.search(r"\d+", text_one)) #<re.Match object; span=(3, 7), match='2026'>
# print(re.match(r"\d+", text_one))#None
# print(re.findall(r"\d+", text_one))#['2026', '1', '25', '2026', '5', '1']
#
# text_two = "2026年2月16日是除夕，2026年5月1日是劳动节！"
# print(re.search(r"\d+", text_two)) #<re.Match object; span=(0, 4), match='2026'>
# print(re.match(r"\d+", text_two)) #<re.Match object; span=(0, 4), match='2026'>
# print(re.findall(r"\d+", text_two)) #['2026', '2', '16', '2026', '5', '1']

#返回的Match对象
# text_three = "今天是2026年1月25日，天气不错。"
# match_obj= re.search(r"\d+", text_three)
# print(match_obj)
# print("匹配的位置：" ,match_obj.span())
# print("匹配的值：", match_obj.group())
# print("匹配的值：", match_obj.group(0))

# #捕获组
# text_four = "今天是2026年1月25日，天气不错。"
# #提前出text_four文本中的日期值：年份值，月份值，日期值
# match_obj= re.search(r"((\d{4})年((\d{1,2})月(\d{1,2})日))", text_four)
# print(match_obj)
# print("匹配的总值：",match_obj.group())
# print("匹配的总值：",match_obj.group(0))
# print("匹配第1组：",match_obj.group(1))
# print("匹配第2组：",match_obj.group(2))
# print("匹配第3组：",match_obj.group(3))
# print("匹配第4组：",match_obj.group(4))
# print("匹配第5组：",match_obj.group(5))
# # print("匹配第6组：",match_obj.group(6))#报错
"""
    group()和group(0)是一样，整个正则的匹配总的结果
    grou(1)~ group(n)依次是第n个捕获组的匹配结果
    组的序号从1开始，从左往右依次数(，没遇到一个(，就是一个新的组
    例如：((\d{4})年((\d{1,2})月(\d{1,2})日))
    第1组：((\d{4})年((\d{1,2})月(\d{1,2})日))
    第2组：(\d{4})
    第3组：((\d{1,2})月(\d{1,2})日)
    第4组：(\d{1,2})
    第5组：(\d{1,2})
"""
# text_five = "出生日期：2002年5月6日，毕业日期：2025-7-1，入职日期：2026/3/8"
# all_date = re.findall(r"\d{4}[年/-]\d{1,2}[月/-]\d{1,2}日?",text_five)
# print("所有的日期值：", all_date)

# text_six = "123hello89world45python472"
# text_six = text_six.replace(r"\d","abc") #不支持正则

# 去除字符串首尾的数字
# text_six = re.sub(r"^\d+|\d+$","",text_six)
# print("去掉首尾的数字：",text_six)

# 去掉字符串中的所有数字
# text_six = re.sub(r"\d+","",text_six)
# print("去掉所有的数字：", text_six)

# 非开头和结尾的数字替换为-
# text_six = re.sub(r"(?<=\D)\d+(?=\D)", "-",text_six)
# print(text_six)
"""
    (?<=\D)\d+ ：找数字，但是在数字前面（<）搜索非数字，找到非数字，那么说明该数字是咱们本次要查找的数字。否则该数字就不是我们要查找的目标。
            例如：123数字，但是在123前面没有找其他非数字，所以123不是本次要查找的数字目标
            例如：89数字，但是在89前面找到了其他非数字o，所以89可能是本次要查找的数字目标
    \d+(?=\D)：找数字，但是在数字后面（没有<）搜索非数字，找到非数字，那么说明该数字是咱们本次要查找的数字。否则该数字就不是我们要查找的目标。
            例如：89数字，但是在89后面找到了其他非数字w，所以89是本次要查找的数字目标
            例如：472数字，但是在472前面找到其他非数字n，所以472可能是本次要查找的数字目标
                         但是在472后面没找到其他非数字n，所以472不是本次要查找的数字目标
                
"""
# text_seven = "I have 2 apples and 3 oranges."
# #将数字替换为对应的单词
# num_map = {"1": "one", "2": "two", "3": "three", "4": "four", "5": "five"}

# #使用之前的知识
# table = str.maketrans(num_map)
# text_seven = text_seven.translate(table)
# print(text_seven)

# text_seven = re.sub(r"\d+", lambda x: num_map[x.group()],text_seven)
# print(text_seven)

# 按多个分隔符分割
text_eight = "apple,banana;orange:grape"
# result = text_eight.split(",") #不支持正则。   字符串类型str的split方法
# print(result)

# result = re.split(r"[,;:]",text_eight) #这是re模块，正则的split函数
patten = "[" + string.punctuation +"]"
result = re.split(patten,text_eight) #这是re模块，正则的split函数
print(result)