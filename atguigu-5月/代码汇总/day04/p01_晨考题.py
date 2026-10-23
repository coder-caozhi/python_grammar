"""
    @Author:Irene
    @Time:2026/5/16
    @Desc:
"""
# 编写一个while循环，计算 100 到 1000的整数之和。
# num = 100
# total = 0
# while num<=1000:
#     total += num
#     num += 1
# else:
#     print("100 到 1000的整数之和：", total)

# 输出100~1000中的所有水仙花数
# 水仙花数:3位正整数等于各个位数字的立方和，例如：153 == 1的立方 + 5的立方 + 3的立方 ？
# for i in range(100, 1000):
#     # 每一个i求它们的百位，十位，个位
#     bai = i // 100
#     shi = i // 10 % 10
#     ge = i % 10
#     if bai**3 + shi**3 + ge**3 == i:
#         print(i)


"""
编写程序，接收用户输入的一个字符串，使用循环将字符串中的字符逆序输出。
例如：输入 "hello"，输出 "olleh"。
    range(start,end,step)
    step为负数，倒序，递减数列
        h   e   l   l  o
    正向 0   1   2   3  4
    负向 -5  -4  -3 -2  -1

"""
word = input("请输入一个字符串：")
# for w in range(-1,-len(word)-1,-1):
#     print(word[w],end="")

# for w in range(len(word)-1,-1,-1):
#     print(word[w],end="")

print(word[::-1])