"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    1、try-except搭配else或finally使用
    try:
        可能发生异常的业务代码①
        可能发生异常的业务代码②
        可能发生异常的业务代码③
    except 异常或错误类型1:
        处理异常或错误的代码
        或
        打印异常或错误的代码（打印到控制台，输出到日志文件中）
    except 异常或错误类型2 as 变量: #该变量用于接收异常对象
        处理异常或错误的代码
        或
        打印异常或错误的代码（打印到控制台，输出到日志文件中）
    except: #可以匹配所有类型的异常或错误
        处理异常或错误的代码
        或
        打印异常或错误的代码（打印到控制台，输出到日志文件中）
    else:
        当try没有发生异常时，需要执行的代码。如果try发生了异常，无论except能不能捕获，都不执行。
        如果前面的代码执行了return，它就不执行了。
    finally:
        无论try中有没有发生异常，也不管except能不能捕获异常，哪怕前面有return都要执行的代码。
        例如：资源释放代码 xx.close()，或 网络断开等。
"""
import sys
def one():
    try:
        a = 8
        b = 3
        print(a/b)
        return
    except:
        print("发生异常")
    else:
        print("没有发生异常，程序正常结束")
    finally:
        print("finally")

def two():
    try:
        a = 8
        b = 0
        print(a/b)
        # sys.exit(1)
        return
    except:
        print("发生异常")
    else:
        print("没有发生异常，程序正常结束")
    finally:
        print("finally")

one()
print("=" * 30)
two()