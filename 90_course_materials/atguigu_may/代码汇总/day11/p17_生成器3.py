"""
    @Author:Irene
    @Time:2026/5/26
    @Desc:
"""
"""
    刚才的生成器是单向工作，生成器给我们提供值，
    现在我们想要实现双向通信，
    （1）生成器可以给我们返回值
    （2）我们也可以给生成器发送值。通过发送值，我们可以干扰或控制生成器的功能。
      如果要给生成器发送值，需要通过send()函数。
      send()函数 VS next()函数
      
      next()函数：生成器给我们提供1个值
      send()函数：生成器给我们提供1个值 +  我们给生成器发送1个值
"""
# def func():
#     value = yield 1 #第一次执行到yield 1，此时value= 这个部分没有走
#     print("value =", value)
#     value = yield 2
#     print("value =", value)
#     value  = yield 3
#     print("value =", value)
#
# g = func() #调用func()此时不执行func()的函数体语句，而是创建了一个生成器对象
# print(next(g)) #开始执行func()函数的函数体语句
#                #第一次next()从 func():开始走到第一句yield 1
# print(next(g))#第二次next()从 yield 1的下一个动作，value=开始执行，到下一个yield 2
#                 #因为这里没有通过send给生成器发送值，所以本次value=接收的是一个None
# print(g.send(100)) #第三次执行send() 从yield 2的下一个动作，value=开始执行，到下一个yield 3
#                     #因为这里有通过send给生成器发送值，所以本次value=100
#
# print(g.send(200))#第三次执行send() 从yield 3的下一个动作，value=开始执行，到末尾，发生StopIteration异常
#                 #因为这里有通过send给生成器发送值，所以本次value=200

# def func():
#     value = yield 1 #第一次执行到yield 1，此时value= 这个部分没有走
#     print("value =", value)
#     value = yield 2
#     print("value =", value)
#     value  = yield 3
#     print("value =", value)
#
# # g = func() #调用func()此时不执行func()的函数体语句，而是创建了一个生成器对象
# # print(g.send(100)) #开始执行func()函数的函数体语句
#                   # 第一次执行send()从 func():开始走到第一句yield 1 ，因为此时它刚开始，无法用变量接收你给它发的值，所以报错
#
# g = func() #调用func()此时不执行func()的函数体语句，而是创建了一个生成器对象
# print(g.send(None))#开始执行func()函数的函数体语句
#                   # 第一次执行send()从 func():开始走到第一句yield 1 ，因为send的是一个None，所以等价于 next()，没有给它值
# print(g.send(100))
# print(g.send(200))
# print(g.send(300))

#需求：有一个生成器，可以产生数字，数字从1开始，如果数字到达100之后，重新从1开始。也可以产生字母，字母从a开始，如果到达z之后，重新从a开始
#生成器默认产生数字，我们可以通过给它发送值，让它选择产生数字还是字母。通过task变量控制，task=0表示产生数字，task=1表示产生字母。
def func():
    task = 0
    num = 1
    letter = 'a'
    while True:
        match task:
            case 0:
                value = yield num #value用于接收用户通过send发送给生成器的值。如果外面没有send新值，那么value=None
                num += 1
                if num > 100:
                    num = 1
            case 1:
                value = yield letter #value用于接收用户通过send发送给生成器的值。如果外面没有send新值，那么value=None
                letter = chr(ord(letter) + 1)
                if letter > 'z':
                    letter = 'a'
        task = value if value != None else task
        # if value != None  当value不为None条件成立，无论value是0,1，还是其他都是不为None
        # if value   当value不为None，不为0，不为""，不为[] 才成立，是None,0,"",[]都表示不成立

g = func()
for i in range(5):#打印1-5，task=0
    print(next(g))

print(g.send(1)) #'a'， task=1

for i in range(5):#打印b,c,d,e,f ,task=1
    print(next(g))

print(g.send(0)) #6， task=0

for i in range(5):#打印7-11，task=0
    print(next(g))