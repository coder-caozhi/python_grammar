"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
# fr = open("1.txt","r",encoding="utf-8")
# while fr.read(3):
#     print(fr.read(3))
# fr.close()
#以上写法的错误在于，循环一次读取2次。第一次读取的作为条件，第二次读取的内容用于输出

# fr = open("1.txt","r",encoding="utf-8")
# while s:=fr.read(3): #把fr.read(3)的返回值赋值给s，再用s的内容作为条件
#     print(s,end="")
# fr.close()

# fr = open("1.txt","r",encoding="utf-8") #fr本质上是一个可迭代对象，同时也是迭代器
# for s in fr:#默认一次读取一行
#     print(s,end="")
# fr.close()

print("=" * 50)
# fr = open("1.txt","r+",encoding="utf-8")
# print(fr.read(3))
# fr.write("柴") #无论前面读了几个字符，写的时候，会把游标移动到末尾写
# fr.close()

# fr = open("1.txt","r+",encoding="utf-8")
# fr.write("柴") #如果前面没有开始读，相当于遍历过程没有开始，那么光标默认在最开始，写，就会覆盖原来的内容
# fr.close()

# fw = open("1.txt","w+",encoding="utf-8")#w覆盖模式，打开的瞬间就清空原来的内容
# print(fw.read()) #没有写，直接读，什么也读不到
# fw.close()

# fw = open("1.txt","w+",encoding="utf-8")
# fw.write("柴林燕")#先写了一些内容
# print(fw.read())#光标已经到达默认了，读不到
# fw.close()

fw = open("documents/1.txt", "w+", encoding="utf-8")
fw.write("柴林燕")#先写了一些内容
fw.seek(0) #光标回到起始的位置
print(fw.read())
fw.close()