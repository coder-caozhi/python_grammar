"""
    @Author:Irene
    @Time:2026/5/13
    @Desc:
 """
"""
    成员运算符是用于判断某个对象是不是容器中的一个元素。
    python中的容器有很多，
    例如：字符串str，用于装一组字符，每一个字符都是字符串容器中的一个元素   "hello"
        列表list   [10,5,7,9,5,4]
        集合set    {8,9,5,7}
        ....
        
    成员运算符 in  和 not in，运算结果也是布尔值
"""
s = "hello"
print("e" in s)#True
print("a" in s)#False
print("a" not in s) #True

print(15 in [10,5,7,9,5,4])