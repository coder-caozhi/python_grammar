"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
"""
    1、复制文件
    步骤：
    （1）打开2个通道，一个用于读，一个用于写
    （2）一边读一边写
    （3）关闭2个通道
"""
#复制1.txt，复制后的文件名是1_副本.txt
# fr = open("1.txt","r",encoding="utf-8")
# fw = open("1_副本.txt","w",encoding="utf-8")
# fw.write(fr.read())
# fw.close()
# fr.close()

#假设文件比较大
fr = open("documents/1.txt", "r", encoding="utf-8")
fw = open("documents/1_副本.txt", "w", encoding="utf-8")
while True:
    data = fr.read(1024)
    if not data:
        break
    fw.write(data)
fw.close()
fr.close()
