"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
import traceback

#复习之前IO操作
#输出一句话到hello.txt文件中
fr = None
try:
    fr = open("hello.txt", "r",encoding="utf-8")
    fr.write("hello world")
except:
    traceback.print_exc()
finally:
    if fr:
        fr.close()