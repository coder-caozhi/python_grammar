"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import random
from collections import defaultdict

"""
    1、collections中的defaultdict
"""
# #需求1：统计单词出现的次数
# words = ["hello", "world", "hello", "hello", "atguigu", "python"]
#
# #不使用defaultdict，使用之前的dict
# words_count_dict = {} #words中的单词是字典的key，该单词的次数是value
# for word in words:
#     if word in words_count_dict:
#         words_count_dict[word] += 1
#     else:
#         words_count_dict[word] = 1
# print("每一个单词的次数：",words_count_dict)
#
# #使用defaultdict
# words_count_dict = defaultdict(int) #int代表的是字典中value的类型
# #因为如果某个key不存在，那么defaultdict会给这个key自动添加一个(key,value)，此时value的默认值与类型有关。
# #如果是int类型，默认值0
# #如果是list类型，默认值[]
# for word in words:
#     words_count_dict[word] += 1
# print("每一个单词的次数：",dict(words_count_dict))


#需求2：统计单词，分为2组，一组是包含a字母，一组不包含a字母
# words = ["hello", "world", "hello", "hello", "atguigu", "python","chai"]
#不使用defaultdict，使用之前的dict
# words_count_dict = {} #key是2个，一个key是"包含a字母"，另一个key是“不包含a字母"。value是列表
#结果类似于：{"包含a字母":["atguigu","chai"], "不包含a字母":["hello","world","hello", "hello","python"]}
#结果类似于：{"包含a字母":["atguigu","chai"], "不包含a字母":["hello","world","python"]}
# words_count_dict = {"包含a字母":[], "不包含a字母":[]}
# for word in words:
#     if "a" in word:
#         words_count_dict["包含a字母"].append(word)
#     else:
#         if word not in words_count_dict["不包含a字母"]:
#             words_count_dict["不包含a字母"].append(word)
# print("单词分组：",words_count_dict)

#使用defaultdict
# words_count_dict = defaultdict(list)
# for word in words:
#     if "a" in word:
#         words_count_dict["包含a字母"].append(word)
#     else:
#         if word not in words_count_dict["不包含a字母"]:
#             words_count_dict["不包含a字母"].append(word)
# print("单词分组：",words_count_dict)


#需求：随机产生10个[1,100]的整数，然后把偶数和奇数分开2组
# nums = [random.randint(1,100) for _ in range(10)]
# #使用defaultdict
# even_odd_dict = defaultdict(list)
# for num in nums:
#     if num % 2 == 0:
#         even_odd_dict["even"].append(num)
#     else:
#         even_odd_dict["odd"].append(num)
# print("数字统计结果：",dict(even_odd_dict))

"""
    2、Counter（计数器）：专门用来统计xx的个数。它像是defaultdict的一个子类别，专门用于统计个数的场景。
"""
# from collections import Counter
# # #需求1：统计单词出现的次数
# words = ["hello", "world", "hello", "hello", "atguigu", "python"]
# word_count = Counter(words)
# print("单词次数统计结果：",word_count)
#
# other = ["chai","atguigu","hello"]
# word_count.update(other) #类似与追加统计数据
# print("单词次数统计结果：",word_count)
#
# print("单词次数前3多的单词：", word_count.most_common(3))
# print("统计情况遍历：")
# for item in  word_count.elements():#按照添加顺序遍历。但是item出现的次数是按照统计频率
#     print(item)


"""
   
    补充几个数据结构的知识点：
    数据结构分为物理结构和逻辑结构：
    1、物理结构是底层实现方式，大致分为两种：
    （1）数组：一个数组在内存中是开辟一整块内存空间，元素是连续存储的，那么元素可以快速的通过“索引”来访问，效率非常高，时间复杂度是O(1)。
            缺点是增、删时处理比较麻烦，如果是静态数组，根本无法增删。如果是动态数组，那么增需要扩容和移动元素，删除需要移动元素。
    （2）链式结构：元素之间位置不一定是相邻的，可以散落在内存的任意位置。如何把相关的元素串起来，那么必须有“结点”。
        结点：包含当前元素本身以及与它有关系的其他结点的地址
        单链表：   结点包含当前元素本身 + 下一个结点的地址
        双链表：   结点包含当前元素本身 + 上一个结点的地址 + 下一个结点的地址
        二叉树：   结点包含当前元素本身 + 父结点的地址 + 左子结点的地址 + 右子结点的地址
        图
        ....
    
    2、逻辑结构：数据的逻辑特点
    线性关系：元素是one by one，像数组、单链表、双链表、栈、队列等
    非线性关系：树等
     
    栈：先进后出（想象成一个桶）。有栈顶和栈底的概念。咱们只能操作栈顶元素。放进去的新元素在栈顶，取的元素也只能取栈顶。
    队列：
        普通队列：只能一个头进另一个头出。或者是从队头出，从队尾进。  遵循先进先出
        双端队列：两头都可以进出。但是，单纯从一个头看，是栈结构。两头一起看，才是先进先出。  
        
    3、collections.deque：双端队列（高效增删）
    使用容器主要围绕这么几个问题？
    （1）该容器对应的数据结构是什么
    （2）该容器的对象是否可变，元素是否可重复，是否有序
    （3）如果可变，创建容器，增删改查遍历操作
        如果不可变，创建容器，查询遍历操作
        
    deque：双端队列，可变，无序（不能按照索引直接操作），可重复
    
    
"""
from collections import deque
deque_demo = deque() #创建容器
deque_demo.append("张三") #追加到队尾
deque_demo.append("李四")#追加到队尾
deque_demo.append("王五")#追加到队尾
deque_demo.appendleft("柴林燕") #添加到队头
deque_demo.append("熊大")#追加到队尾
deque_demo.append("熊二")#追加到队尾
deque_demo.append("光头强")#追加到队尾

print("遍历：")
for item in deque_demo:
    print(item)

deque_demo.remove("李四")
print("删除后：",deque_demo)

print("删除：", deque_demo.pop()) #删除队尾
print("删除：", deque_demo.popleft()) #删除队头

print("右侧扩展：", deque_demo.extend(["张杰","孙俪"]))
print("左侧扩展：", deque_demo.extendleft(["大海","宋红康"]))
print("扩展后：",deque_demo)

# deque_demo.rotate(3)
# print("队列的旋转：", deque_demo)

deque_demo.rotate(-3)
print("队列的旋转：", deque_demo)






