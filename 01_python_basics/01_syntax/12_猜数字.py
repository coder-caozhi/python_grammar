# 猜数字游戏
import random

# 1. 生成1到100之间的随机数
target_num = random.randint(1, 100)
# target_num = 100
count = 0 # 记录猜测次数

print("=" * 30)
print("欢迎来到猜数字游戏")
print("请随机输入游戏数字，输入q退出游戏")
print("=" * 30)

while True:
    user_input = input("请随意输入一个整数数字")

    if user_input == 'q' or user_input == 'Q':
        print("你退出了游戏")
        break

    if user_input.isdigit():
        guess_num = int(user_input)
    else:
        print("请输入一个数字")
        continue

    count += 1

    if guess_num > target_num:
        print("猜大了")
    elif guess_num < target_num:
        print("猜小了")
    else:
        print(f"恭喜你猜对了, 正确的目标数字是{target_num}")
        print(f"你猜了{count}次")
        break


