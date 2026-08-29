# 统计test2.txt文件的行数及 忙 字在文件中出现的次数
# 读取文件
with open("test2.txt",mode="r",encoding="utf-8") as f:
    line_count = 0
    word_count = 0
    for line in f:
        # 循环一次读一行，行的数量加1
        line_count += 1
        # 统计当前行中包含多少个忙，然后加到word_count中
        word_count += line.count("忙")
    print(f"文件的行数是：{line_count}")
    print(f"'忙'字出现的次数是：{word_count}")