"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import copy

"""
    2、浅拷贝
    变量1 = copy.copy(变量2)
"""
# one = [1, 2, [3, 4]]
# two = copy.copy(one)
# print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
# print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")
#
# two[0] = 100
# two[2][0] = 200
#
# print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
# print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")

def func(one): #传参的过程等价于 one = copy.copy(nums)  ，浅拷贝
    print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
    one[0] = 100
    one[2][0] = 200
nums = [1, 2, [3, 4]]
func(copy.copy(nums))
print(f"{nums=}，地址值：{id(nums)}，嵌套的列表的地址：{id(nums[2])}")
#nums=[1, 2, [200, 4]]，地址值：2694347166080，嵌套的列表的地址：2694347167936