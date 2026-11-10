"""迭代器：理解 iter、next、StopIteration，以及一次性消费。"""


class Countdown:
    """这是迭代器：对象自身记录下一次应该返回的值。"""

    def __init__(self, start: int):
        self.current = start

    def __iter__(self):
        # 迭代器的 iter() 返回自己，而不是重新开始。
        return self

    def __next__(self):
        if self.current <= 0:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value


class CountdownSequence:
    """这是可重复遍历的可迭代对象，每次 iter() 都创建新迭代器。"""

    def __init__(self, start: int):
        self.start = start

    def __iter__(self):
        return Countdown(self.start)


def main():
    print("一、列表可迭代，但列表本身不是迭代器")
    names = ["小王", "小李"]
    cursor = iter(names)
    assert iter(cursor) is cursor
    print(next(cursor))                 # 小王
    print(next(cursor))                 # 小李
    print(next(cursor, "已经读完"))     # 设置默认值，避免耗尽时抛异常

    try:
        next(cursor)
    except StopIteration:
        print("没有默认值时，耗尽会抛出 StopIteration")

    print("\n二、for 循环会反复 next，并在 StopIteration 时结束")
    countdown = Countdown(3)
    assert list(countdown) == [3, 2, 1]
    assert list(countdown) == []         # 消费后不会自动重置
    assert list(Countdown(0)) == []      # 检查边界：没有可返回的元素
    print("同一个迭代器再次遍历：", list(countdown))

    print("\n三、可重复遍历需要每次创建独立迭代器")
    sequence = CountdownSequence(3)
    first, second = iter(sequence), iter(sequence)
    assert first is not second
    assert next(first) == next(second) == 3
    assert list(sequence) == list(sequence) == [3, 2, 1]
    print("两次遍历：", list(sequence), list(sequence))

    # 练习：实现 EvenNumbers(stop)，依次返回小于 stop 的非负偶数。
    # 自测目标：list(EvenNumbers(7)) == [0, 2, 4, 6]。
    print("迭代器案例检查通过")


if __name__ == "__main__":
    main()
