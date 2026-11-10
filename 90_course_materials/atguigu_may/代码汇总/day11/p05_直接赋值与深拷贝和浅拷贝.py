"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
import copy

"""
    3、深拷贝
    变量1 = copy.deepcopy(变量2)
"""
# one = [1, 2, [3, 4]]
# two = copy.deepcopy(one)
# print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
# print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")
#
# two[0] = 100
# two[2][0] = 200
#
# print(f"{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
# print(f"{two=}，地址值：{id(two)}，嵌套的列表的地址：{id(two[2])}")

def func(one): #传参的过程等价于 one = copy.deepcopy(nums)  ，浅拷贝
    print(f"初始{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
    one[0] = 100
    one[2][0] = 200
    print(f"修改后{one=}，地址值：{id(one)}，嵌套的列表的地址：{id(one[2])}")
nums = [1, 2, [3, 4]]
func(copy.deepcopy(nums))
print(f"调用函数后{nums=}，地址值：{id(nums)}，嵌套的列表的地址：{id(nums[2])}")


"""
    结论：传参时
        如果直接传参，实参和形参指向同一个对象，对于可变类型来说，形参对元素的修改直接影响实参。
        如果浅拷贝，实参和形参外层指向不同的对象，但是如果元素是可变类型，是指向相同对象。
            形参对外层元素的修改与实参无关，如果形参对内层可变类型的元素修改，影响实参。
        如果是深拷贝，实参和形参完全是独立的两个对象，从内到外都是，无论你对形参做什么修改，与实参都无关。
"""