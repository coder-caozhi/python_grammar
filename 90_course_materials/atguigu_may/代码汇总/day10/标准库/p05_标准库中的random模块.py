"""
    @Author:Irene
    @Time:2026/5/25
    @Desc:
"""
import random

"""
    
"""
# import random
# print("产生[0,1)的随机浮点数：",random.random())
# print("产生[a,b]的随机整数：",random.randint(1,20)) #[1,20]每一个数都有可能
# print("产生[a,b]的随机浮点数：",random.uniform(1,20))
# print("产生[a,b]的随机整数：",random.randrange(1,20, 3)) #[1,4,7,10,13,16,19]

names = ["张三","李四","王五","赵六","熊大","熊二","光头强"]
print("从上面的列表中随机选取1个：",random.choice(names))
print("从上面的列表中随机选取3个：",random.choices(names,k=3))
print("从上面的列表中随机选取3个：",random.choices(names,weights=[1,1,10,1,100,1,50],k=3)) #可重复选择
print("从上面的列表中随机选取3个：",random.sample(names,k=3)) #不重复选择
print(f"{names=}")
random.shuffle(names)#洗牌
print("打乱顺序：",names)