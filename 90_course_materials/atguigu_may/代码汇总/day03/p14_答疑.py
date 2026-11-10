"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    range与下标/索引有什么关系？本质上没有关系，我们把range范围中数拿来当下标用
    range本身是产生一个等差数列，可能是递增，可能是递减的
"""
# for i in range(1, 5, 2): #递增 step为正
#     print(i)
#
# print("=" * 20)
# for i in range(5, 1, -2): #递减 step为负
#     print(i)
#
# print("=" * 20)
#
# for i in range(-10, -5, 2): #递增 step为正
#     print(i)
#
# print("=" * 20)
# for i in range(-5, -10, -2):  #递减 step为负
#     print(i)

list_demo = [10, 20, 30, 40, 50, 60, 70, 80, 90]
# for i in range(1,5,1): #产生了一个等差数列 [1,2,3,4]递增
#     print(list_demo[i]) # list_demo[1], list_demo[2],list_demo[3],list_demo[4]
# print("=" * 20)
# for i in range(5,1,-1):#产生了一个等差数列 [5,4,3,2]递减
#     print(list_demo[i])  # list_demo[5], list_demo[4],list_demo[3],list_demo[2]
#
# print("=" * 20)
# for i in range(-1,-5, -1): #递减数列 [-1, -2, -3, -4] ，起点start是负数，递减只能是负数
#     print(list_demo[i])

# print("=" * 20)
# for i in range(1,5,1): #产生了一个等差数列 [1,2,3,4]递增，起点start是正数，递增只能是正数
#     print(list_demo[i]) # list_demo[1], list_demo[2],list_demo[3],list_demo[4]

print("=" * 20)
for i in range(-1,5, 1): #递增数列[-1,0,1,2,3,4]，正负数都有
    print(list_demo[i])

print("=" * 20)
for i in range(3,-3, -1): #递减数列[3,2,1,0，-1，-2]，正负数都有
    print(list_demo[i])