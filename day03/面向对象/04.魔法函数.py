class DemoClass:
    def __new__(cls, name):
        """1. 创建实例（第一个调用）"""
        print(f"调用 __new__ 创建 {cls.__name__} 实例")
        instance = super().__new__(cls)
        return instance

    def __init__(self, name):
        """2. 初始化实例"""
        print("调用 __init__ 初始化属性")
        self.name = name

    def __str__(self):
        """3. 调用 str(实例) 时执行"""
        return f"DemoClass: name={self.name}"

    def __del__(self):
        """4. 实例销毁时执行"""
        print(f"调用 __del__ 销毁 {self.name} 实例")

# 演示流程
obj = DemoClass("test")  # 触发 __new__ + __init__
print(obj)          # 触发 __str__
del obj                  # 触发 __del__（引用计数为0时）