# 创建一个100万个数据的列表
import sys

my_list = [i for i in range(1000000)]
# print(my_list)
# 列表占用的内存大小
print(sys.getsizeof(my_list))

# 创建一个100个数据的生成器
my_generator = (i for i in range(1000000))
print(my_generator)
# 生成器占用的内存大小
print(sys.getsizeof(my_generator))
# 获取第一个值
print(next(my_generator)) # 0
print(next(my_generator)) # 1
print(next(my_generator)) # 2
print(next(my_generator)) # 3
# 当生成器是：my_generator = (i for i in range(4))时才会报一下异常
print(next(my_generator)) # StopIteration

# 创建一个for循环只在控制台打印生成器生成的第一个值和最后一个值
for i in my_generator:
    if i <= 10:
        print(i)