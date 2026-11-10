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

    #该方法的作用是返回一个迭代器对象(iterator)。
    def __iter__(self):
        return self

    #任何迭代器对象都必须包含__next__()方法，用于遍历容器中的元素。
    # 每一次调用__next__()方法能得到一个元素。
    def __next__(self):
        if self.index < -len(self.sequence):
            raise StopIteration
        item = self.sequence[self.index]
        self.index -= 1
        return item

    #__iter__方法与__next__方法可以在同一个类中，也可以不在同一个类中。


list_demo = [1,2,3,4,5]
r  = ReverseIterator(list_demo)
# while True:
#     try:
#         item = r.__next__()
#         print(item)
#     except StopIteration:
#         break

for i  in r:
    print(i)