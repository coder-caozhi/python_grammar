"""
    @Author:Irene
    @Time:2026/5/27
    @Desc:
"""
import time
import traceback

"""
    1、什么是池Pool？
    生活中：蓄水池，游泳池
        池：有一定的水，已经准备好一些水
           有边界，定量
           水可以重复使用
           
    2、为什么要用池？
    如果不用进程池：
    （1）所有的进程对象需要我们自己创建
    （2）进程的数量没法限制，在一些高峰期会导致过多的进程对象被创建，
        每一个进程都需要一块独立的内存，会导致内存资源被耗尽，服务器就崩了
    （3）进程任务完成后，就销毁了，有点浪费
    
    如果有进程池：
    （1）池中的进程对象不需要手动创建
    （2）池中的进程数量是可控的
    （3）池中的进程可以重复使用
    
    3、如何创建进程池？
    multiprocessing.Pool()
    
    4、如何把任务提交给进程池
    map适用于多个进程完成的任务函数是相同的。
"""
from multiprocessing import Pool
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
    # 第一步：准备测试文件
    # test_files = ["document/python1.txt", "document/python2.txt",
    #               "document/python3.txt", "document/python4.txt",
    #               "document/python5.txt"]

    test_files = [("document/python1.txt","UTF-8"),
                  ("document/python2.txt", "GBK"),
                  ("document/python3.txt", "GBK"),
                  ("document/python4.txt", "UTF-8"),
                  ("document/python5.txt", "GBK")]
    #第二步：创建进程池
    # with Pool() as p:
    # with Pool(5) as p: #如果传了5，表示池中有5个进程同时完成任务
    with Pool(2) as p: #如果传了2，表示池中有2个进程同时完成任务
        # results = p.map(word_count,test_files) #map的任务函数 通常是没有参数或只有1个参数
        results = p.starmap(word_count,test_files) #starmap的任务函数，可以是多个参数
        print(results)

