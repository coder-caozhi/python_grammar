"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    单链表
"""
#结点：
class Node:

    def __init__(self,item,next=None):
        self.item = item
        self.next = next


#单链表
class LinkedList:
    def __init__(self):
        self.head = None # 头结点，一开始是空的
        self.size = 0 #元素个数，同时也是结点的个数
        self.node = None

    def add(self, item):
        #创建一个新结点
        new_node = Node(item) #next默认为None

        #分情况讨论
        if not self.head:
            self.head = new_node #新结点就是单链表的第一个结点，就是头结点
        else:
            #查找末尾结点
            node = self.head
            while node.next: #如果node.next为None，while条件不成立，结束
                             #如果node.next不为None，循环继续，node右移
                node = node.next
            #把新结点链接到末尾结点的next
            node.next = new_node

        self.size += 1

    def __iter__(self): #包含这个方法，表示LinkedList的对象是可迭代对象
                      #该方法要返回一个迭代器对象（即包含__next__方法对象）
        self.node = self.head
        return self

    def __next__(self): #包含这个方法，用于遍历元素，一次返回一个元素
        # node = self.head
        if not self.node:
            raise StopIteration
        item = self.node.item
        self.node = self.node.next
        return item

    def __str__(self):
        # result = "["
        # node = self.head
        # while  node:
        #     result += node.item + ","
        #     node = node.next
        # return result + "]"

        return "[" + ",".join(self) +"]"

    def remove(self,item):
        pass

#测试
if __name__ == "__main__":
    link = LinkedList()
    link.add("hello")
    link.add("world")
    link.add("python")
    link.add("atguigu")
    print(link)

    # for item in link:
    #     print(item)
    #
    # print("第二次遍历")
    # for item in link:
    #     print(item)

    iterator_one = link.__iter__()
    print(id(iterator_one))
    while True:
        try:
            print(iterator_one.__next__())
        except StopIteration:
            break
    print("第二次遍历")
    iterator_one = link.__iter__()
    print(id(iterator_one))
    while True:
        try:
            print(iterator_one.__next__())
        except StopIteration:
            break
