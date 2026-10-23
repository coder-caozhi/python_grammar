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

    def __iter__(self): #返回生成器对象，生成器对象自带__next__方法
        node = self.head
        while node:
            yield node.item
            node = node.next

    def __str__(self):
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

    for item in link:
        print(item)

    # print(link)