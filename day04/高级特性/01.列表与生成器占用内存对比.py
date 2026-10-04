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
first_value = None
last_value = None
for i in my_generator:
    if first_value is None:
        first_value = i  # 记录第一个值
    last_value = i       # 每次覆盖，循环结束后即为最后一个值
print(first_value)
print(last_value)