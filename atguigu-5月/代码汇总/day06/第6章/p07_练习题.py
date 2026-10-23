"""
    @Author:Irene
    @Time:2026/5/19
    @Desc:
"""
import heapq

"""
有一组商品信息：
    product_price = {
        "苹果": 5.99,
        "香蕉": 3.50,
        "牛奶": 12.80,
        "面包": 8.50,
        "笔记本电脑": 4999.99,
        "无线耳机": 299.99,
        "运动鞋": 399.00,
        "保温杯": 69.90
    }
（1）筛选出价格高于100的商品
（2）按照商品价格排序
"""
product_price = {
    "苹果": 5.99,
    "香蕉": 3.50,
    "牛奶": 12.80,
    "面包": 8.50,
    "笔记本电脑": 4999.99,
    "无线耳机": 299.99,
    "运动鞋": 399.00,
    "保温杯": 69.90
}
# for item in product_price.items():
#     print(item)

# print(list(filter(lambda x: x[1]>100,product_price.items())))
# print(dict(filter(lambda x: x[1]>100,product_price.items())))
"""
 filter本身的函数中会对你指定的可迭代对象进行遍历，
 （1）如果写product_price
    for x in product_price:
        x是key
 （2）如果写product_price.items()
    for x in product_price.items():
        x是(key,value)
"""
# print(dict(sorted(product_price.items(), key=lambda x:x[1])))



"""
有一组商品信息：
    goods_stock = [
        {"商品名称": "苹果", "库存量": 120, "价格": 5.99},
        {"商品名称": "香蕉", "库存量": 85, "价格": 3.50},
        {"商品名称": "牛奶", "库存量": 200, "价格": 12.80},
        {"商品名称": "面包", "库存量": 150, "价格": 8.50},
        {"商品名称": "笔记本电脑", "库存量": 30, "价格": 4999.99},
        {"商品名称": "无线耳机", "库存量": 55, "价格": 299.99},
        {"商品名称": "运动鞋", "库存量": 78, "价格": 399.00},
        {"商品名称": "保温杯", "库存量": 99, "价格": 69.90}
    ]
（1）按照商品库存量升序排序
（2）找出库存量最多的3个商品的名称
（3）库存量最多的3个商品的库存量总和有多少
"""
goods_stock = [
        {"商品名称": "苹果", "库存量": 120, "价格": 5.99},
        {"商品名称": "香蕉", "库存量": 85, "价格": 3.50},
        {"商品名称": "牛奶", "库存量": 200, "价格": 12.80},
        {"商品名称": "面包", "库存量": 150, "价格": 8.50},
        {"商品名称": "笔记本电脑", "库存量": 30, "价格": 4999.99},
        {"商品名称": "无线耳机", "库存量": 55, "价格": 299.99},
        {"商品名称": "运动鞋", "库存量": 78, "价格": 399.00},
        {"商品名称": "保温杯", "库存量": 99, "价格": 69.90}
    ]
# print(sorted(goods_stock, key=lambda x:x["库存量"]))
# # result = heapq.nlargest(3,goods_stock,key=lambda x:x["库存量"])
# # print(result)
# # result = [goods["商品名称"] for goods in result]
# # print(result)
# # print([goods["商品名称"] for goods in heapq.nlargest(3,goods_stock,key=lambda x:x["库存量"])])
#
# max_save_amount = heapq.nlargest(3,goods_stock,key=lambda x:x["库存量"])
# print(max_save_amount)
# print("库存量最多的3个商品的名称：",[goods["商品名称"] for goods in max_save_amount])
# print("库存量最多的3个商品的库存量总和：", sum(goods["库存量"] for goods in max_save_amount))

"""
（1）随机生成10个[1,100]的整数
（2）定义一个判断x是不是质数的函数
（3）筛选出所有质数
（4）求所有质数的和
"""
import random
nums = [random.randint(1, 100) for _ in range(10)]

def isprime(n):
    if n<=1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

prime_nums = list(filter(isprime, nums))
print("所有的质数：",prime_nums)
print("所有的质数的和：",sum(prime_nums))


