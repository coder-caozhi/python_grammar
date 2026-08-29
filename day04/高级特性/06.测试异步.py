import asyncio
import time


# 模拟耗时IO操作（如HTTP请求、数据库查询）
async def download_url(url: str):
    """异步下载URL（非阻塞）"""
    print(f"开始下载: {url}")
    await asyncio.sleep(1)  # 模拟网络延迟（非阻塞，事件循环可处理其他任务）
    print(f"下载完成: {url}")
    return f"{url} 数据"


def sync_download_url(url: str):
    """同步下载URL（阻塞）"""
    print(f"开始下载: {url}")
    time.sleep(1)  # 阻塞，CPU闲置
    print(f"下载完成: {url}")
    return f"{url} 数据"


# 异步主函数
async def async_main():
    start = time.time()
    # 创建协程任务列表
    tasks = [
        download_url("http://baidu.com"),
        download_url("http://google.com"),
        download_url("http://python.org")
    ]
    # 并发执行所有任务（总耗时≈1秒）
    results = await asyncio.gather(*tasks)
    end = time.time()
    print(f"\n异步总耗时: {end - start:.2f} 秒")
    print("异步结果:", results)


# 同步主函数
def sync_main():
    start = time.time()
    # 串行执行（总耗时≈3秒）
    results = [
        sync_download_url("http://baidu.com"),
        sync_download_url("http://google.com"),
        sync_download_url("http://python.org")
    ]
    end = time.time()
    print(f"\n同步总耗时: {end - start:.2f} 秒")
    print("同步结果:", results)


# 运行测试
if __name__ == "__main__":
    print("=== 异步执行 ===")
    asyncio.run(async_main())  # 运行异步程序

    print("\n=== 同步执行 ===")
    sync_main()


# 输出结果：
# === 异步执行 ===
# 开始下载: http://baidu.com
# 开始下载: http://google.com
# 开始下载: http://python.org
# 下载完成: http://baidu.com
# 下载完成: http://google.com
# 下载完成: http://python.org
# 异步总耗时: 1.00 秒
#
# === 同步执行 ===
# 开始下载: http://baidu.com
# 下载完成: http://baidu.com
# 开始下载: http://google.com
# 下载完成: http://google.com
# 开始下载: http://python.org
# 下载完成: http://python.org
# 同步总耗时: 3.00 秒