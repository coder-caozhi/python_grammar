"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
from collections import deque
"""
定义函数sliding_max(nums:list, k:int)给定一个列表和一个窗口大小 k，使用 deque 实现滑动窗口最大值。
列表：[1,3,-1,-3,5,3,6,7]
窗口大小 k=3
输出：[3,3,5,5,6,7]
"""
# def sliding_max(nums:list, k:int):
#     #方式一：不考虑时间复杂度，这里的时间复杂度是n的平方
#     d = deque(nums[:k]) #初始化第1个窗口，把nums的[0],[1],[2]。。。[k-1]元素放到队列中
#     result = [max(d)]
#     for i in range(k, len(nums)):
#         d.popleft() #移走窗口队列左边的元素
#         d.append(nums[i]) #添加新元素到窗口队列的右边
#         result.append(max(d))
#     return result

def sliding_max(nums:list, k:int):
    d = deque()
    #初始化窗口期
    for i in range(k):
        #如果队列不是空的
        #while d表示队列不是空的，如果队列是空的，while d是False
        #d[-1]<=nums[i] 队列的最后一个元素 小于 新要添加的元素nums[i]，就删除队尾的元素
        #while循环直到队列空或者队尾元素比即将新添加的元素大才结束
        while d and d[-1]<nums[i]:
            d.pop()
        d.append(nums[i])
    #上面for循环结束后，处理了k个元素，首个窗口形成了
    result = [d[0]] #队列的第一个元素就是首个窗口的最大值

    #滑动窗口
    for i in range(k, len(nums)):
        #判断d[0]是不是上次窗口的左边界元素
        if d[0] == nums[i-k]:
            d.popleft()

        #新元素进来之前，看现有的队尾元素是否比新要进来的元素小，如果小，就去掉
        while d and d[-1]<nums[i]:
            d.pop()

        d.append(nums[i]) #新元素进来
        result.append(d[0]) #窗口中最左边的元素是最大值
    return result

# print(sliding_max([1,3,-1,-3,5,3,6,7],3))
# print(sliding_max([1],1))
print(sliding_max([-7,-8,7,5,7,1,6,0],4))