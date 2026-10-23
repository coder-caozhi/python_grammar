"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import traceback

"""
编写一段 Python 代码，尝试将字符串 "123abc" 转换为整数，
如果转换失败，捕获 ValueError 异常，将异常信息记录到一个文本文件 error.log 中。
"""
try:
    s = "123abc"
    num = int(s)
    print("数字：",num)
except ValueError as e:
    try:
        with open("error.log", "a", encoding="UTF-8") as fw:
            # fw.write(e) #e对象的类型不是str字符串。当我们用print()或str()时，才会自动调用e对象的__str__()
            # fw.write(str(e))
            fw.write(traceback.format_exc())#将异常的详细信息进行格式化转为字符串
            fw.write("\n")
    except Exception as e:
        print("写入日志文件失败")
        traceback.print_exc()


print("其他代码")

"""
    print(e) 与 str(e)   都是只将异常的描述信息打印或转为字符串
    traceback.print_exc() 与 traceback.format_exc()  将异常对象的堆栈跟踪的详细信息打印或转为字符串
"""