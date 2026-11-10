"""生成器：yield 暂停、惰性计算、yield from 与逐项处理管道。"""

from itertools import islice


def squares(limit: int):
    print("生成器函数开始执行")
    for number in range(limit):
        print(f"现在计算 {number} 的平方")
        yield number * number
        # yield 保留局部变量和执行位置；下次 next 从这里继续。
    print("生成器执行完毕")


def flatten(groups):
    for group in groups:
        # 等价于：for item in group: yield item
        yield from group


def parse_orders(lines):
    """输入是迭代器也可以；不需要先读完整个数据集。"""
    for line in lines:
        name, amount = line.strip().split(",")
        yield name, int(amount)


def main():
    print("一、创建生成器时，函数体尚未开始执行")
    values = squares(3)
    print("已经创建；下面第一次 next 才开始计算")
    assert next(values) == 0
    assert next(values) == 1
    assert list(values) == [4]
    assert list(values) == []  # 生成器也是迭代器，只能消费一次

    print("\n二、生成器表达式可以只消费所需的前几个结果")
    large = (number * number for number in range(1_000_000))
    first_three = list(islice(large, 3))
    assert first_three == [0, 1, 4]
    assert next(large) == 9
    print("前三项：", first_three)
    # 惰性计算不等于绝对不占内存：仍保存迭代状态，也可能引用输入数据。
    # 如果再调用 list(large)，就会把所有剩余结果收集到内存。

    print("\n三、yield from 展平一层分组")
    assert list(flatten([[1, 2], [], [3]])) == [1, 2, 3]
    print(list(flatten([["语法", "函数"], ["FastAPI"]])))

    print("\n四、解析 → 过滤 → 汇总：模拟逐行处理订单")
    # 示例使用小列表，实际也可传入打开的文本文件对象。
    lines = ["键盘,199", "鼠标,79", "显示器,1299"]
    orders = parse_orders(lines)
    expensive = (amount for name, amount in orders if amount >= 100)
    total = sum(expensive)
    assert total == 1498
    assert list(orders) == []
    print("金额不少于 100 的订单合计：", total)

    # 练习：写 running_total(numbers)，逐次 yield 累计和。
    # 自测目标：list(running_total([3, 5, 2])) == [3, 8, 10]。
    print("生成器案例检查通过")


if __name__ == "__main__":
    main()
