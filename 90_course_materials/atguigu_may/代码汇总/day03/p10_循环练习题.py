"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""

# 练习题10：完成九九乘法表
"""
   外循环i=1
     内循环j=1  完成 i*1=1
     换行
   外循环i=2
     内循环j=1,2  完成 2*1=2 2*2=2
     换行
  ...
  
  外循环i的值[1,9]
  内循环j，每一轮的值[1,i]
"""
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i}*{j}={i*j}", end="\t")
#     print()

# for i in range(1,10):
#     for j in range(1,i+1):
#         exp = f"{i}*{j}={i*j}"
#         print(f"{exp:<10}", end="")
#     print()

"""
*
**
***
****
*****
i = 1, j=1
i = 2, j=1,2
i = 3, j=1,2,3
i = 4, j=1,2,3,4
i = 5, j=1,2,3,4,5
"""
# for i in range(1,6):
#     for j in range(1,i+1):
#         print('*',end="")
#     print()

# for i in range(1,6):
#     # start = "*" * i
#     start = ""
#     for j in range(1, i + 1):
#         start += "*"
#     print(start)

"""
    *
   ***
  *****
 *******
*********
i=1,*数量1
i=2,*数量3
i=3,*数量5
i=4,*数量7
i=5,*数量9
    *数量 2*i-1
"""
# for i in range(1,6):
#     start = ""
#     for j in range(1, 2*i):
#         start += "*"
#     print(f"{start:^9}")

"""
i=1,空格4
i=2,空格3
i=3,空格2
i=4,空格1
i=5,空格0
    空格数量 5-i

i=1,*数量1
i=2,*数量3
i=3,*数量5
i=4,*数量7
i=5,*数量9
    *数量 2*i-1
"""
# for i in range(1,6):
#     #打印n个空格
#     for j in range(1,5-i+1):
#         print(" ",end="")
#
#     #打印m个*
#     for j in range(1,2*i):
#         print("*",end="")
#
#     # 换行
#     print()

"""
    *
   * *
  *   *
 *     *
*       *
 *     *
  *   *
   * *
    *
晚自习再做
"""

"""
练习题12：找出1000以内所有的完数
所谓完数是一个数等于它因子之和，例如：6=1+2+3
"""
# for num in range(1,1000):
#     #如何判断num是不是完数？
#     #（1）找到num的所有因子并且累加它们，因子：除去它本身的所有约数
#     #（2）它因子之和与num比较是否相等
#     total = 0
#     for j in range(1,num):
#         if num % j == 0: #j是num的因子
#             total += j
#     #整个内层for是用来找num的所有因子
#     if total == num:
#         print(num)

"""
练习题13：找出100以内所有的素数
所谓素数/质数是大于1的自然数且只能被1和它本身整除
"""
# for i in range(1,101):
#     """
#     思考：判断i是不是素数？如何判断i是不是只能被1和i本身整除？
#     方式一：求所有i的因子之和，是不是为1
#     方式二：求所有i的因子的个数，是不是为1
#     方式三：求所有i的约数之和是不是 1+i
#     方式四：在[2,i-1]范围内找有没有把i整除的数，如果有，说明i不是素数，如果没找到，说明i是素数
#     """
#     flag = True #True表示i是素数
#     for j in range(2, i):#j满足条件的值[2,3,4,i-1]，当j=i不满足条件，结束for循环
#         if i % j == 0: #证明i不是素数。 是不是可以凭借1个j能把i整除，就断定i不是素数？？可以
#             # print(f"{i}不是素数")
#             flag = False #False表示i不是素数
#             break
#         # else: #错误，因为不能凭借1个j不能把i整除，就说i是素数
#         #     print(f"{i}是素数")
#     #什么时候才能断定i是素数？必须把[2,i-1]范围的所有数判断完了，才能确定i是素数
#     #如果是break出来j什么特点，不是break出来j什么特点？
#     #不是break出来j==i
#     # if j==i:#如果没有进入内循环，j就没有初始值，就无法判断这个条件
#     #     print(f"{i}是素数")
#     if flag:
#         print(f"{i}是素数")

"""
优化一下，缩小判断范围
在[2,i的平方根]范围内找有没有把i整除的数，如果有，说明i不是素数，如果没找到，说明i是素数
    以36为例，它的约数1,2,3,4,6,9,12,18,36
    a * b = 36
"""
# import math
# for i in range(1,101):
#     flag = True #True表示i是素数
#     for j in range(2, int(math.sqrt(i))+1):#j满足条件的值[2,3,4,i-1]，当j=i不满足条件，结束for循环
#         if i % j == 0: #证明i不是素数。 是不是可以凭借1个j能把i整除，就断定i不是素数？？可以
#             flag = False #False表示i不是素数
#             break
#     if flag:
#         print(f"{i}是素数")


"""
练习题14：输入年、月、日的值，使用while或for循环完成统计这一天是这一年的第几天。
且要控制年、月、日的合法输入，如果输入不正确，让用户重新输入。
年份必须大于0，月份必须[1,12]，日期必须在 [1,这个月最大天数] 范围内。
"""
while True:
    year = int(input("请输入年份："))
    if year > 0:
        break
    else:
        print("年份必须是正数")

# 格式化快捷键Ctrl + Alt + L
while True:
    month = int(input("请输入月份："))
    if 1 <= month <= 12:
        break
    else:
        print("月份范围[1,12]")

#计算第month月的总天数
days_of_month = 31
if month in [4, 6, 9, 11]:
    days_of_month = 30
elif month == 2:
    days_of_month = 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28

#日期的输入
while True:
    day = int(input("请输入日期："))
    if 1 <= day <= days_of_month:
        break
    else:
        print(f"日期范围[1,{days_of_month}]")

print(f"{year}年{month}月{day}日")
#累加 [1, month-1]的所有满月天数，和第month月的day天
total_days = day
for i in range(1, month):
    if i in [4, 6, 9, 11]:
        total_days += 30
    elif i == 2:
        total_days += 29 if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 else 28
    else:
        total_days += 31
print(f"这一天是这一年的第{total_days}天")