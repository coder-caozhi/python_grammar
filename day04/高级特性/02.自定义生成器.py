# range(n)函数可以生成0到n-1个数

#我们自定义一个生成器，可以生成1到n个数
def my_range(n):
    # 定义一个变量 i
    i = 1
    while i <= n:
        yield i # 代码执行到这时会暂停，同时将当前i的值返回
        i += 1

# 调用生成器，通过它帮我生成1到5的数字
my_num = my_range(5)
print(my_num)
# 获取第一个值
print(next(my_num)) # 1
print(next(my_num)) # 2
print(next(my_num)) # 3
print(next(my_num)) # 4
print(next(my_num)) # 5
print(next(my_num)) # 报错StopIteration