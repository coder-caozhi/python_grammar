"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
题1：文件读取、字符串拆分
任务：编写函数count_words_in_file(filename)，读取指定文本文件，返回文件中的总单词数（单词以空格等分隔）。
示例：假设test.txt内容如下，则函数返回4。
    Hello world
    Hello Python
"""
# def count_words_in_file(filename:str):
#     fr = open(filename,"r",encoding="utf-8")
#     data = fr.read()
#     word_count = len(data.split())
#     fr.close()
#     return word_count

# def count_words_in_file(filename:str):
#     fr = open(filename,"r",encoding="utf-8")
#     word_count = 0
#     while line:=fr.readline():
#         word_count += len(line.split())
#     fr.close()
#     return word_count
#
# print(f"单词的数量：{count_words_in_file("test.txt")}")

"""
题2：文件写入、字典操作

任务：编写函数save_contacts(contacts, filename)，将通讯录字典（键为姓名，值为电话）保存到文件中，
每行格式为姓名:电话。再编写load_contacts(filename)，从文件中读取并重建字典。
"""
# def save_contacts(contacts:dict, filename:str)->None:
#     fw = open(filename, 'a',encoding='utf-8')
#     # for contact in contacts.items(): #contact是一个元组(key,value)
#     for key,value in contacts.items():
#         fw.write(key+':'+str(value)+'\n')
#     fw.close()
#
# tel_contacts = {"张三":"10086","李四":"10010","王五":110}
# save_contacts(tel_contacts, "tel_contacts.txt")

# def load_contacts(filename):
#     fr = open(filename,"r",encoding="utf-8")
#     contacts_dict = {}
#     for line in fr: #逐行遍历文件中的内容
#         key,value =  line.strip().split(":")
#         contacts_dict[key] = value
#     fr.close()
#     return contacts_dict
# print(load_contacts("tel_contacts.txt"))

"""
任务：有一个日志文件log.txt，每行格式为时间 - 级别 - 消息，例如2023-01-01 10:00 - ERROR - Disk full。
编写函数count_log_levels(filename)，统计并返回一个字典，记录每个日志级别（INFO、WARNING、ERROR）出现的次数。
示例：{"ERROR": 5, "WARNING": 3, "INFO": 10}
"""
# def count_log_levels(filename):
#     log_levels_dict = {"INFO":0,"WARNING":0,"ERROR":0}
#     fr = open(filename,"r",encoding="utf-8")
#     for line in fr:
#         # time,level,info = line.strip().split(" - ")
#         _,level,_ = line.strip().split(" - ")
#         log_levels_dict[level] += 1
#     fr.close()
#     return log_levels_dict

def count_log_levels(filename):
    log_levels_dict = {}
    fr = open(filename,"r",encoding="utf-8")
    for line in fr:
        # time,level,info = line.strip().split(" - ")
        _,level,_ = line.strip().split(" - ")
        if level in log_levels_dict:
            log_levels_dict[level] += 1
        else:
            log_levels_dict[level] = 1
    fr.close()
    return log_levels_dict

print(count_log_levels("log.txt"))