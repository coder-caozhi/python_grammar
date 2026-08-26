# while循环
count = 0
while count < 10:
    if count == 6:
        break
    print(count)
    count += 1
else:
    print("当循环被break了之后else将不会执行")
print("这是循环和else下面打印的内容")

# for循环
my_list = ["罗志祥","陶喆","文章","林丹","吴秀波","马蓉","宋喆"]
# 遍历所有的明星
for star in my_list:
    print(f"生活糜烂的明星是：{star}")

print("*"*30)

my_str = "hello python"
for char in my_str:
    print(char)

# range()函数：左闭右开，例如：range(1,9)得到的是1到8的值
my_list2 = list(range(1,9))
for num in my_list2:
    if num == 5:
        break
       # continue
    print(num)
else:
    print("for执行结束")

# 打印一个九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={i*j}",end=" ")
    print("")

# pass：用来占位，没有实际逻辑
for i in range(1,11):
    pass