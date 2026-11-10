"""打包与解包：赋值中的 *、调用中的 */**、定义中的 *args/**kwargs。"""


def build_order(customer, /, *items, discount=0, **metadata):
    """/ 前只接受位置参数；*items 后的 discount 只能按关键字传入。

    items 把多余的位置参数打包为元组；metadata 把多余关键字打包为字典。
    args、kwargs 不是关键字，真正起作用的是 * 和 **。
    """
    return customer, items, discount, metadata


def main():
    print("一、赋值：打包成元组，再按位置解包")
    point = 10, 20
    x, y = point
    assert isinstance(point, tuple) and (x, y) == (10, 20)
    head, *middle, tail = [1, 2, 3, 4]
    assert (head, middle, tail) == (1, [2, 3], 4)
    # 星号接收的是列表，可能为空；一次赋值的同一层最多有一个星号目标。
    first, *rest = [7]
    assert first == 7 and rest == []

    print("\n二、函数定义负责打包，函数调用负责解包")
    products = ["键盘", "鼠标"]
    options = {"discount": 20, "source": "学习案例", "paid": True}
    customer, items, discount, metadata = build_order("小王", *products, **options)
    assert items == ("键盘", "鼠标")
    assert discount == 20 and metadata["paid"] is True
    print(customer, items, discount, metadata)

    print("\n三、合并列表与字典")
    merged = [0, *range(1, 4), 4]
    defaults = {"timeout": 10, "retries": 2}
    custom = {"timeout": 30}
    settings = {**defaults, **custom}  # 字典构造中后面的同名键覆盖前面
    assert merged == [0, 1, 2, 3, 4]
    assert settings == {"timeout": 30, "retries": 2}
    print("合并配置：", settings)

    print("\n四、函数调用的重复关键字会报错，不会自动覆盖")
    try:
        build_order("小王", discount=10, **{"discount": 20})
    except TypeError:
        print("捕获预期错误：discount 被传入两次")
    else:
        raise AssertionError("重复关键字应当抛出 TypeError")
    try:
        left, right = [1, 2, 3]
    except ValueError:
        print("捕获预期错误：解包目标数量不匹配")
    else:
        raise AssertionError("数量不匹配应当抛出 ValueError")

    # 练习：实现 summarize(*scores, passed=60)，返回总人数和及格人数。
    # 自测目标：summarize(59, 60, 90) == (3, 2)。
    print("打包解包案例检查通过")


if __name__ == "__main__":
    main()
