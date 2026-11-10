"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
#定义序列的反向迭代器，从右往左遍历
class ReverseIterator: #类名自己取
    def __init__(self,sequence):
        self.sequence = sequence #真正装元素的容器，它是一个序列
        self.index = -1

    #该方法的作用是返回一个生成器对象，它就是特殊的迭代器对象
    def __iter__(self):
        while self.index >= -len(self.sequence):
            yield self.sequence[self.index]
            self.index -=1


list_demo = [1,2,3,4,5]
# r  = ReverseIterator(list_demo).__iter__()
# while True:
#     try:
#         print(r.__next__())
#     except StopIteration:
#         break

r = ReverseIterator(list_demo)
for i in r:
    print(i)