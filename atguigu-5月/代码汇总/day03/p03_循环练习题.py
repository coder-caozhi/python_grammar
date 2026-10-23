"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
练习题5：计算 1 到 100 的和
用 for 循环计算：1 + 2 + 3 + … + 100 的结果
"""
# total = 0
# for num in range(1,101):
#     total += num
# print(total)

# total = (1+100)/2 * 100
# print(total)

"""
练习题6：统计列表中大于 30 的数
给定列表：
    scores = [25, 42, 19, 66, 31, 15]
用 for 循环统计有多少个数大于 30，并输出总个数。
"""
# count = 0
# scores = [25, 42, 19, 66, 31, 15]
# for s in scores:
#     if s > 30:
#         print(s)
#         count+=1
# print("总个数：",count)

"""
练习题7：求列表所有数的平均值
给定列表：
    nums = [5, 8, 13, 27, 10]
用 for 循环求出平均值并输出。提示：len(列表)可以获取列表元素个数
"""
nums = [5, 8, 13, 27, 10]
total = 0
for num in nums:
    total += num
print(f"总和：{total}，平均值：{total/len(nums)}")