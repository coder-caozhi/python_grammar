"""
    @Author:Irene
    @Time:2026/5/18
    @Desc:
"""
"""
题2：默认值参数
编写函数 calc_area(width, height, unit="cm")
计算矩形面积：面积 = 宽 × 高，输出格式：矩形面积：xx 平方xx
分别使用位置传参和关键字传参调用calc_area函数。
"""
# def calc_area(width, height, unit="cm"):
#     return f"矩形面积：{width * height}平方{unit}"
#
# print(calc_area(10, 5))
# print(calc_area(10, 5, "m"))
# print(calc_area(width=10, height=5, unit="m"))

"""
题3：默认值参数
编写函数print_rectangle(line, column, sign='*')，实现打印line行column列由sign接收的字符组成的矩形。
如果sign没有接收参数，则图形由*组成。line和column必须是正整数，否则不打印。
"""
# def print_rectangle(line, column, sign='*'):
#     if not isinstance(line, int) or not isinstance(column, int):
#         print(f"行和列必须是整数，{line}或{column}不符合要求")
#         return #提前结束当前函数
#     if line < 1 or column < 1:
#         print(f"行和列必须是正整数，{line}或{column}不符合要求")
#         return #提前结束当前函数
#     # for i in range(line):
#     #     for j in range(column):
#     #         print(sign, end='')
#     #     print()
#     for i in range(line):
#         print(sign * column)
# # print_rectangle(10, 5)
# print_rectangle(10, 5,"#")
# # print_rectangle(-10, 5,"#")
"""
题4：可变传参
定义函数 get_even(*nums)，接收任意多个整数，返回由其中所有偶数组成的列表。
"""
# def get_even(*nums): #nums在这里是一个元组
#     return [i for i in nums if i%2==0]
# lst = [8,9,7,6,5,4,3]
# result = get_even(*lst) #解包传参
# print(result)
"""
题5：可变传参
定义函数 statistic(*nums)，接收任意多个数字，返回一个元组 (总和, 个数, 平均值)，未传参数时提示暂无数据，返回 (0, 0, 0)
"""
# def statistic(*nums):
#     if not nums:
#         return 0,0,0
#
#     # return (sum(nums),len(nums), sum(nums)/len(nums))
#     # return sum(nums),len(nums), sum(nums)/len(nums)
#     #在python中，函数可以同时返回“多个值”，即return后面可以写多个值，但是底层多个值会用一个元组装起来返回，
#     # 实际返回的是元组这个容器对象的首地址
#     total = sum(n for n in nums if n) #累加非空值
#     return total,len(nums),total/len(nums)
#
# print("统计分析：", statistic(1,2,3,4,5))
# total,count,avg = statistic(1,2,3,4,5) #把statistic(1,2,3,4,5)函数的返回值的元组的各个元素拆解出来赋值给3个变量
# print(f"总和：{total}，个数：{count}，平均值：{avg}")
# print("统计分析：",statistic())
# print("统计分析：",statistic(*[]))
# print("统计分析：",statistic(None)) # nums=(None,)

"""
题6：可变传参
定义函数 build_str(prefix, suffix, sep,*parts)，实现将parts部分的多个字符串拼接为一个字符串，
多个字符串之间使用sep分隔，最后加上前缀prefix和后缀suffix。
    print(build_str("[","]","-", "我", "爱", "Python")) # [我-爱-Python]
"""
def build_str(prefix, suffix, sep, *parts):
    return prefix + sep.join(parts) + suffix

print(build_str("[","]","-", "我", "爱", "Python"))
print(build_str("[","]","-"))