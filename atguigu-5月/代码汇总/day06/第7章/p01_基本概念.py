"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    1、什么是IO？
    i：input，输入，把数据从文件、控制台、网络接收过来，保存到当前程序的某个变量/容器中。
    o：output，输出，把当前程序中的变量、容器中的数据 写到/输出到 控制台、文件、网络中。
    
    2、什么是文件和目录？
    目录：在windows中是文件夹，用来装很多文件一个结构。
    文件：含后缀名或扩展名。 文件名.xx
        扩展名通常代表文件的类型，是图片，word文档，ppt，python脚本。
             .jpg, .png 等 是图片
             .doc, .docx 是word文档
             .py 是python脚本
    
    3、相对路径和绝对路径
    在程序中如何描述一个文件或目录，都必须指定路径。即告诉python解释器怎么定位到这个文件或目录。
    绝对路径：
        在windows环境下，从盘符开始，例如：d:\\atguigu\\ai\\BJ20260511.xlsx        
        在linux环境下或macOS环境下，从/（根路径）开始就是绝对路径
        
    相对路径：
        在windows环境下，不是以盘符开始都是相对路径，例如：day06_code\\hello.txt
                                                 .\\day06_code\\hello.txt
                                                 ..\\..\\day06_code\\hello.txt
                                                 .代表当前路径，..代表上级路径
         在linux环境下或macOS环境下，不是以/开始的就是相对路径                                       
        
    路径分隔符：
        windows早期只支持\，现在也支持/，默认仍然是\。（在python中\会被用于转义，所以表示路径的时候可能会用到\\
        linux等支持/ 
"""
# filename = "day06_code\\hello.txt" #从p01_基本概念.py这个文件的所在目录（第7章）开始找day06_code文件夹，然后再找hello.txt
# open(filename)#错误，找不到

filename = "documents/atguigu.txt"
open(filename)

filename = "documents/test\\world.txt"
open(filename)

filename = "..\\第6章\\p01_晨考题.py"
open(filename)

"""
    4、文件的分类
    （1）纯文本文件：它里面只能出现文本字符，不能出现图片等
        .txt，.py，.js，.css，.js, .md等
        在读取和写入时，可以以字符为单位写和读，一次至少写或读一个完整的字符
        纯文本文件通常需要指定字符编码方式：GBK,UTF-8等，
            不同的编码方式，一个字符的宽度是不同的，
                GBK中英文字母是1个字节，中文是2个字节
                UTF-8英文字母是1个字节，中文是3个字节，emoji表情字符是4个字节
    （2）其他非纯文本文件：其他的文件都是非纯文本文件，例如：.doc，.ppt，.xls等
        在读取和写入时，只能以字节为单位写和读，一次可能能读取一个完整的字符，也可能只是读取了一个字符的其中1个字节。
    
"""
