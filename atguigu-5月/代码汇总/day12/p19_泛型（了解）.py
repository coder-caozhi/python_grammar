"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
def func(nums:list[int]):
    for i in nums:
        print(f"元素的值：{i}，类型是{type(i)}")

if __name__ == "__main__":
    func([1,2,3])
    func(["hello","world","python"])
