"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import traceback
from concurrent.futures import ThreadPoolExecutor

#map是一键提交任务，多个线程的任务是相同的
#定义任务函数：统计某个文件的单词的数量
def word_count(filename, encoding="UTF-8"):
    print(f"开始解析{filename}文件")
    try:
        with open(filename, "r", encoding=encoding) as fr:
            data = fr.read() #仅限于文件不大的情况，一口气读完
            words_list = data.split()
            # time.sleep(2)
        print(f"{filename}文件解析完成")
        return f"{filename}中的单词数量：{len(words_list)}"
    except Exception as e:
        traceback.print_exc()
        print(f"{filename}读取文件失败")

if __name__ == "__main__":
    test_files = ["document/python1.txt", "document/python2.txt",
                  "document/python3.txt", "document/python4.txt",
                  "document/python5.txt"]
    encodings = ["UTF-8","GBK","GBK","UTF-8","GBK"]
    with ThreadPoolExecutor () as pool:
        # test_files是给5个任务函数的filename参数赋值，encodings是给5个任务函数的encoding参数赋值
        # 任务函数word_count有几个参数，就需要传入几个列表或元组，每一个列表或元组对应一个参数
        results = pool.map(word_count,test_files,encodings)
        for r in results:
            print(r)