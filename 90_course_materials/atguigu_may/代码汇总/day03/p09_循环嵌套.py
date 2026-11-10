"""
    @Author:Irene
    @Time:2026/5/15
    @Desc:
"""
"""
    循环嵌套：
        外层循环循环1次，内层循环需要走一轮
        循环嵌套可以是for套for，可以是while套while，也可以是for和while嵌套
        比喻：外循环是分针，内循环是秒针，内循环走一轮，外循环走一格
        
    循环结构嵌套一般不要超过3层
        
"""
"""
    需求：
        打印如下图形：
        1           i=1     j=1
        12          i=2     j=1,2
        123         i=3     j=1,2,3
        1234        i=4     j=1,2,3,4
        12345       i=5     j=1,2,3,4,5
"""
# for i in range(1,6): #循环5次 i依次是1,2,3,4,5
#     for j in range(1,i+1):
#         print(j, end='')
#     print()


"""
    需求：从控制台输入1个正整数，输入0结束，输入负数忽略。对正整数求它的所有因子
"""
while True:
    num = int(input("请输入1个正整数："))
    if num < 0:
        continue
    if num == 0:
        break
    #求num的所有因子，在[1, num)范围找哪些数可以把num整除
    print(f"{num}的因子有：",end="")
    for j in range(1,num):
        if num % j == 0:
            print(j,end=" ")
    print()


















