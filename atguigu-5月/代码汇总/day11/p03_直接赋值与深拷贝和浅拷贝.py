"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    1、直接赋值
    变量1 = 变量2  这是直接赋值
"""
# one = [1, 2, [3, 4]]
# two = one #直接赋值
# print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
# print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")
#
# two[0] = 100
# two[2][0] = 200

print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")

def func(one): #传参的过程等价于 one = nums  ，直接赋值
    print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
    two = one #直接赋值
    print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")
    two[0] = 100
    two[2][0] = 200
nums = [1, 2, [3, 4]]
func(nums) #nums把地址值给one，one又给了two，这里2个动作都是直接赋值
print(f"{nums=}，地址值：{id(nums)}，嵌套的列表的地址：{id(nums[2])}")