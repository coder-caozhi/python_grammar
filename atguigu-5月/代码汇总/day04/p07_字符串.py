"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
"""
    1、字符串str的特点
    （1）有序：可以通过索引操作
    （2）可以重复
    （3）不可变 => 有intern()共享机制
         字面量字符串，不包含空格等空白字符的字符串，可以共享。
         
    （4）代表的数据结构：数组
    
    2、字符串的创建
    （1）""， ''， 三个双引号开头结尾，三个单引号开头结尾
    （2）str(内容)
    （3）原始字符串 r"内容" 或 r'内容'  应用场景有：A：文件路径表示，B：正则
"""
# s1 = "helloworld"
# s2 = "helloworld"
# print(id(s1), id(s2)) #查看地址值
# print(s1 is s2) #比较地址值
# print(s1 == s2) #比较内容
#
# s1 = "hello world"
# s2 = "hello world"
# print(id(s1), id(s2)) #查看地址值
# print(s1 is s2) #比较地址值
# print(s1 == s2) #比较内容

# s1 = "hello\nworld"
# print(s1)
#
# s2 = r"hello\nworld"
# print(s2)

"""
    3、字符串增删改查
    没有直接的增、删的方法。
    字符串.replace(旧字符，新字符)：会返回新的字符串，不是对原字符串直接修改的
    根据索引/下标访问1个元素：字符串[索引]
    根据访问切片多个元素：字符串[start:end:step]
    查询某个元素的下标/索引： 字符串.index(元素)  元素不存在报错
                         字符串.find(元素)   元素不存在返回-1（这里-1代表不存在，不是最后一个元素）
                         无论是index还是find返回的 下标都是正向下标[0, len(字符串)-1]
    查找元素的最大值：max(字符串)  返回Unicode编码值最大的字符
                  max(字符串, key=函数) 返回按照函数计算结果最大，函数会对每一个字符进行计算
    查找元素的最小值：min(字符串)  返回Unicode编码值最大的字符
                 min(字符串, key=函数)返回按照函数计算结果最小，函数会对每一个字符进行计算
    查找某个元素重复几次：字符串.count(目标元素)
    获取元素的总个数：en(字符串)    
    判断某个元素在不在序列中：元素 in 字符串           
    字符串的遍历：        
    (1)for 元素 in 序列:
          语句
    (2)for 下标 in range(start,end,step):
            语句
      range(start,end,step)：产生的是一个等差数列。
        step为正：递增数列
        step为负：递减数列
        start,end可以使用正下标体系，也可以使用负下标体系
    (3)for 下标,元素 in enumerate(序列):
        语句           
        
    4、字符串排序，反转？ 没有   
    字符串本身没有排序方法，但是内置函数sorted(字符串)返回排序后的列表 
"""
# s = "hello"
# print(s)
# # s += "world" #字符串拼接
# # print(s)
#
# s = s.replace("e","a") #此处必须接收，否则无法看到修改结果
# print(s)
#
# print(s[0])
# print(s[1:3])
# print(s.index('l'))
# # print(s.index('w'))#报错
# print(s.find('l'))
# print(s.find('w'))

# s = "hello"
# r = sorted(s)
# print(r)