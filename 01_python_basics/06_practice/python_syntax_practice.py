# -*- coding: utf-8 -*-  # 声明源文件编码，便于在文件中书写中文注释
# Python 语法综合练习：从上到下亲手抄写、运行，并尝试修改每个例子。
# 运行环境：Python 3.10+，因为本文件使用了 match-case 和联合类型注解。

# ============================================================  # 分隔线：注释不会被 Python 执行
# 1. 输出、变量与基本数据类型  # 井号后面的内容是单行注释
# ============================================================  # 分隔线：帮助组织代码结构

print("Hello, Python!")  # print() 用于向控制台输出内容
name = "George"  # 使用等号 = 将右侧的值赋给变量
age = 25  # 整数类型 int
height = 1.78  # 浮点数类型 float
is_learning = True  # 布尔类型 bool，只有 True 和 False 两种值
nothing = None  # None 表示空值或暂时没有值
print(name, age, height, is_learning, nothing)  # print() 可以同时输出多个值
print(type(name), type(age), type(height), type(is_learning))  # type() 用于查看对象的数据类型

# ============================================================  # 分隔线：注释不会被执行
# 2. 类型转换与变量赋值  # 变量不需要提前声明类型
# ============================================================  # 分隔线：帮助组织代码结构

number_text = "100"  # 当前变量保存的是字符串
number_int = int(number_text)  # int() 将可以转换的值转换为整数
number_float = float("3.14")  # float() 将字符串转换为浮点数
number_string = str(2026)  # str() 将数值转换为字符串
truth_value = bool(1)  # bool() 将值转换为布尔值
first, second = 10, 20  # 多重赋值：一次给多个变量赋值
first, second = second, first  # 使用元组解包交换两个变量的值
x = y = z = 0  # 链式赋值：多个变量引用同一个初始值
print(type(number_string))
print(number_int, number_float, number_string, truth_value)  # 输出类型转换结果
print(first, second, x, y, z)  # 输出赋值结果

# ============================================================  # 分隔线：注释不会被执行
# 3. 常见运算符  # 运算符用于执行计算、比较和逻辑判断
# ============================================================  # 分隔线：帮助组织代码结构

a = 10  # 定义第一个参与运算的整数
b = 3  # 定义第二个参与运算的整数
print(a + b)  # + 表示加法
print(a - b)  # - 表示减法
print(a * b)  # * 表示乘法
print(a / b)  # / 表示普通除法，结果通常是浮点数
print(a // b)  # // 表示整除，向下取整
print(a % b)  # % 表示取余数
print(a ** b)  # ** 表示幂运算，即 a 的 b 次方
a += 2  # += 是增强赋值，等价于 a = a + 2
print(a == b, a != b, a > b, a <= b)  # 比较运算符会返回 True 或 False
print(a > 5 and b < 5)  # and 表示逻辑与，左右条件都为真才为真
print(a > 5 or b > 5)  # or 表示逻辑或，左右条件至少一个为真
print(not is_learning)  # not 表示逻辑非，对布尔值取反
print("Py" in "Python")  # in 用于判断元素是否存在于容器中
print("Java" not in ["Python", "Go"])  # not in 用于判断元素是否不存在
print(name is not None)  # is / is not 用于判断两个引用是否指向同一对象
if (length := len(name)) > 3:  # := 是海象运算符，可在表达式中赋值并使用变量
    print("名字长度：", length)  # 使用海象运算符刚刚赋值的 length

# ============================================================  # 分隔线：注释不会被执行
# 4. 字符串与格式化  # 字符串用于保存文本
# ============================================================  # 分隔线：帮助组织代码结构

single_quote = '单引号字符串'  # 字符串可以使用单引号定义
double_quote = "双引号字符串"  # 字符串也可以使用双引号定义
# 三引号可以定义多行字符串，也常用于编写模块或函数说明。
multi_line = """第一行\n第二行"""  # 三引号字符串可以保存包含换行符的多行文本
raw_text = r"C:\Users\George\Documents"  # r 前缀表示原始字符串，反斜杠通常不转义
message = f"你好，{name}，你今年 {age} 岁"  # f-string 可以把变量或表达式嵌入字符串
print(single_quote, double_quote, multi_line, raw_text, message)  # 输出不同形式的字符串
print(message.upper())  # upper() 返回大写形式
print(message.lower())  # lower() 返回小写形式
print("  Python  ".strip())  # strip() 去掉字符串两端的空白字符
print("a,b,c".split(","))  # split() 按指定分隔符拆分字符串并返回列表
print("-".join(["2026", "11", "01"]))  # join() 使用指定字符串连接多个字符串
print("Python".replace("Py", "My"))  # replace() 替换字符串中的指定内容
print(message[0])  # 使用索引访问字符串中的单个字符，索引从 0 开始
print(message[-1])  # 负数索引从字符串末尾开始计数
print(message[0:4])  # 切片 [start:end] 获取子字符串，不包含 end 位置
print(message[:2])  # 省略 start 表示从开头开始切片
print(message[2:])  # 省略 end 表示切片到字符串末尾
print(message[::-1])  # 步长为 -1 可以反转字符串

# ============================================================  # 分隔线：注释不会被执行
# 5. 列表 list  # 列表有序、可修改，可以保存多个元素
# ============================================================  # 分隔线：帮助组织代码结构

fruits = ["apple", "banana", "orange"]  # 使用方括号 [] 创建列表
fruits.append("grape")  # append() 在列表末尾添加一个元素
fruits.extend(["pear", "peach"])  # extend() 将另一个可迭代对象中的元素逐个添加
fruits.insert(1, "kiwi")  # insert() 在指定索引位置插入元素
fruits.remove("banana")  # remove() 删除第一个匹配的元素
last_fruit = fruits.pop()  # pop() 删除并返回指定位置的元素，默认删除最后一个
fruits.sort()  # sort() 对原列表进行原地排序
fruits.reverse()  # reverse() 将原列表中的元素顺序反转
print(fruits, last_fruit)  # 输出列表和 pop() 返回的元素
print(fruits[0], fruits[-1])  # 使用索引访问列表元素
print(fruits[1:3])  # 使用切片获取列表的一部分
print(len(fruits), "apple" in fruits)  # len() 获取元素数量，in 判断元素是否存在
fruit_copy = fruits.copy()  # copy() 创建一个浅拷贝列表
numbers = [5, 2, 8, 1]  # 创建一个整数列表
print(sorted(numbers))  # sorted() 返回排序后的新列表，不修改原列表
print(numbers)  # 原列表仍保持原来的顺序

# ============================================================  # 分隔线：注释不会被执行
# 6. 元组 tuple、集合 set、字典 dict  # 三种常见内置容器
# ============================================================  # 分隔线：帮助组织代码结构

coordinates = (10, 20)  # 使用圆括号创建元组，元组通常不能修改
one_item_tuple = ("Python",)  # 只有一个元素的元组需要保留末尾逗号
print(coordinates[0], one_item_tuple)  # 元组可以通过索引访问元素
unique_numbers = {1, 2, 2, 3, 3}  # 使用花括号创建集合，重复元素会被自动去重
unique_numbers.add(4)  # add() 向集合中添加一个元素
unique_numbers.update([5, 6])  # update() 可以批量添加元素
print(unique_numbers)  # 集合不保证按插入顺序展示
print({1, 2, 3} | {3, 4, 5})  # | 表示集合并集
print({1, 2, 3} & {2, 3, 4})  # & 表示集合交集
print({1, 2, 3} - {2})  # - 表示集合差集
person = {"name": "George", "age": 25, "city": "Shanghai"}  # 使用键值对创建字典
print(person["name"])  # 通过 key 获取 value，不存在的 key 会触发 KeyError
print(person.get("job", "未知"))  # get() 获取值，key 不存在时可以返回默认值
person["job"] = "Developer"  # 通过 key 赋值可以新增或修改字典元素
person.update({"age": 26, "active": True})  # update() 可以批量更新字典
print(person.keys())  # keys() 获取所有键
print(person.values())  # values() 获取所有值
print(person.items())  # items() 获取由键和值组成的可迭代视图
for key, value in person.items():  # 遍历字典时可以同时取得 key 和 value
    print(key, "=", value)  # 输出当前键值对

# ============================================================  # 分隔线：注释不会被执行
# 7. 条件判断 if、elif、else 和 match-case  # 根据条件选择执行路径
# ============================================================  # 分隔线：帮助组织代码结构

score = 86  # 定义一个用于判断的分数
if score >= 90:  # if 用于判断第一个条件
    print("优秀")  # 条件为 True 时执行缩进代码块
elif score >= 60:  # elif 表示前面的条件不成立时继续判断
    print("及格")  # 当前 elif 条件成立时执行
else:  # else 表示前面所有条件都不成立时执行
    print("需要继续努力")  # else 分支不需要额外条件
level = "B"  # 定义一个用于模式匹配的等级
match level:  # match-case 是 Python 3.10+ 提供的结构化模式匹配语法
    case "A":  # case 用于匹配指定的值
        print("等级 A")  # 匹配 A 时执行
    case "B" | "C":  # | 在模式中表示匹配多个备选值
        print("等级 B 或 C")  # 匹配 B 或 C 时执行
    case _:  # 下划线 _ 表示匹配其他所有情况
        print("其他等级")  # 没有匹配到前面分支时执行

# ============================================================  # 分隔线：注释不会被执行
# 8. 循环 for、while、break、continue  # 重复执行一段代码
# ============================================================  # 分隔线：帮助组织代码结构

for item in fruits:  # for 用于依次遍历可迭代对象中的元素
    print(item)  # 输出本次循环取得的元素
for index, item in enumerate(fruits, start=1):  # enumerate() 同时提供索引和值
    print(index, item)  # 输出当前元素的序号和值
for number in range(1, 6):  # range(start, stop) 生成从 start 到 stop-1 的整数序列
    print(number)  # 输出当前数字
for left, right in zip([1, 2, 3], ["a", "b", "c"]):  # zip() 将多个可迭代对象按位置配对
    print(left, right)  # 输出当前配对结果
count = 0  # 初始化 while 循环的计数变量
while count < 3:  # while 在条件为 True 时重复执行代码块
    print("count =", count)  # 输出当前计数值
    count += 1  # 每次循环都让计数值加一，避免无限循环
for number in range(5):  # 再次遍历 0 到 4
    if number == 1:  # 判断当前数字是否为 1
        continue  # continue 跳过本轮循环剩余代码，进入下一轮
    if number == 4:  # 判断当前数字是否为 4
        break  # break 立即结束整个循环
    print("循环数字：", number)  # 输出没有被跳过或中断的数字
for number in range(2):  # for 循环也可以使用 else 子句
    print("正常循环：", number)  # 输出每轮循环的数字
else:  # 循环没有被 break 中断时，执行 for-else 的 else 分支
    print("循环正常结束")  # 输出循环结束提示

# ============================================================  # 分隔线：注释不会被执行
# 9. 推导式与生成器表达式  # 用简洁语法创建容器或生成数据
# ============================================================  # 分隔线：帮助组织代码结构

squares = [number ** 2 for number in range(5)]  # 列表推导式：根据表达式生成列表
even_squares = [number ** 2 for number in range(10) if number % 2 == 0]  # 推导式末尾可以添加筛选条件
number_set = {number for number in [1, 1, 2, 3]}  # 集合推导式会自动去重
number_dict = {number: number ** 2 for number in range(4)}  # 字典推导式生成键值对
number_generator = (number ** 2 for number in range(3))  # 圆括号中的推导式创建生成器表达式
print(squares, even_squares, number_set, number_dict)  # 输出推导式创建的容器
print(list(number_generator))  # list() 消费生成器并将结果转换为列表

# ============================================================  # 分隔线：注释不会被执行
# 10. 函数、参数与返回值  # 函数用于封装可重复使用的逻辑
# ============================================================  # 分隔线：帮助组织代码结构

def greet(user_name: str, greeting: str = "你好") -> str:  # def 定义函数，冒号后是函数体，注解描述参数和返回值类型
    return f"{greeting}，{user_name}！"  # return 结束函数并把结果返回给调用者
print(greet("George"))  # 调用函数时省略 greeting，使用默认参数
print(greet(user_name="George", greeting="早上好"))  # 使用关键字参数指定参数名
def add_all(*args: int) -> int:  # *args 收集任意数量的位置参数，形成元组
    return sum(args)  # sum() 计算可迭代对象中数值的总和
print(add_all(1, 2, 3, 4))  # 调用可变位置参数函数
def show_profile(name: str, *, city: str, **kwargs: object) -> None:  # * 后参数必须使用关键字传递，**kwargs 收集额外关键字参数
    print(name, city, kwargs)  # 打印普通参数、仅限关键字参数和额外参数
show_profile("George", city="Shanghai", role="Developer", level=3)  # 调用包含多种参数形式的函数
def get_user_info() -> tuple[str, int]:  # 函数可以声明返回元组类型
    return "George", 25  # 用逗号分隔多个值，Python 会将它们打包成元组
user_name, user_age = get_user_info()  # 使用解包语法接收多个返回值
print(user_name, user_age)  # 输出解包后的变量
multiply = lambda x, y: x * y  # lambda 定义只有一个表达式的匿名函数
print(multiply(3, 4))  # 调用匿名函数
print(list(map(lambda value: value * 2, [1, 2, 3])))  # map() 将函数应用到可迭代对象的每个元素
print(list(filter(lambda value: value > 2, [1, 2, 3, 4])))  # filter() 根据函数返回值筛选元素

# ============================================================  # 分隔线：注释不会被执行
# 11. 异常处理  # 避免程序因为可预期的错误直接中断
# ============================================================  # 分隔线：帮助组织代码结构

try:  # try 中放置可能发生异常的代码
    result = 10 / 0  # 除数为 0 会触发 ZeroDivisionError
except ZeroDivisionError as error:  # except 捕获指定异常，as 将异常对象赋值给变量
    print("发生异常：", error)  # 输出异常信息
else:  # try 中没有发生异常时执行 else
    print("计算成功：", result)  # 输出正常计算结果
finally:  # finally 无论是否发生异常通常都会执行
    print("异常处理流程结束")  # 输出流程结束提示
def check_age(value: int) -> None:  # 定义一个用于演示主动抛出异常的函数
    if value < 0:  # 判断传入的年龄是否小于零
        raise ValueError("年龄不能小于 0")  # raise 用于主动抛出异常
    assert value < 150, "年龄数值不合理"  # assert 用于调试时验证一个条件
check_age(25)  # 传入合法数据，不会触发异常

# ============================================================  # 分隔线：注释不会被执行
# 12. 文件读写与 with 上下文管理器  # 演示最常见的文本文件操作
# ============================================================  # 分隔线：帮助组织代码结构

from pathlib import Path  # Path 提供面向对象的路径操作接口
file_path = Path("python_practice_demo.txt")  # 创建一个指向当前工作目录中文件的路径对象
file_path.write_text("第一行\n第二行", encoding="utf-8")  # write_text() 将文本写入文件，encoding 指定字符编码
file_content = file_path.read_text(encoding="utf-8")  # read_text() 读取文件中的全部文本
print(file_content)  # 输出读取到的文件内容
with file_path.open("a", encoding="utf-8") as file:  # with 自动管理文件资源，a 模式表示追加写入
    file.write("\n第三行")  # write() 将字符串写入已经打开的文件
print(file_path.exists())  # exists() 判断路径对应的文件或目录是否存在

# ============================================================  # 分隔线：注释不会被执行
# 13. 类、对象、继承与属性  # 面向对象编程的基础语法
# ============================================================  # 分隔线：帮助组织代码结构

class Animal:  # class 定义一个类，用于描述一类对象的共同特征和行为
    category = "动物"  # 类属性由类本身持有，实例通常可以访问它

    def __init__(self, name: str) -> None:  # __init__ 是初始化方法，创建实例时自动调用
        self.name = name  # self 指向当前实例，实例属性通常通过 self.xxx 定义

    def speak(self) -> str:  # 定义实例方法，第一个参数通常是 self
        return f"{self.name} 发出声音"  # 使用实例属性生成返回值

    @classmethod  # 装饰器：将下面的方法声明为类方法
    def get_category(cls) -> str:  # 类方法的第一个参数通常是 cls，代表当前类
        return cls.category  # 通过 cls 访问类属性

    @staticmethod  # 装饰器：将下面的方法声明为静态方法
    def is_animal(value: object) -> bool:  # 静态方法不自动接收 self 或 cls
        return isinstance(value, Animal)  # isinstance() 判断对象是否属于指定类型

class Dog(Animal):  # 在类名后的括号中填写父类名称即可实现继承
    def __init__(self, name: str, breed: str) -> None:  # 子类可以定义自己的初始化方法
        super().__init__(name)  # super() 用于调用父类中的方法，这里复用父类初始化逻辑
        self.breed = breed  # 定义 Dog 类独有的实例属性

    def speak(self) -> str:  # 子类可以重写父类的方法，这称为方法重写
        return f"{self.name} 汪汪叫"  # 返回子类自己的行为结果

dog = Dog("小白", "柴犬")  # 调用类创建对象，这个过程也称为实例化
print(dog.name, dog.breed, dog.speak())  # 通过对象访问属性和方法
print(dog.category, Dog.get_category())  # 通过实例或类访问类属性和类方法
print(Animal.is_animal(dog))  # 通过类名调用静态方法
print(isinstance(dog, Animal), isinstance(dog, Dog))  # 继承关系中的实例也属于其父类

# ============================================================  # 分隔线：注释不会被执行
# 14. property 属性装饰器  # 将方法包装成像属性一样的访问方式
# ============================================================  # 分隔线：帮助组织代码结构

class Temperature:  # 定义一个用于保存温度的类
    def __init__(self, celsius: float) -> None:  # 初始化摄氏温度
        self._celsius = celsius  # 下划线前缀是约定俗成的内部属性命名方式

    @property  # property 让方法可以通过对象.属性的形式访问
    def celsius(self) -> float:  # 定义读取属性时调用的方法
        return self._celsius  # 返回内部保存的摄氏温度

    @celsius.setter  # 定义给 celsius 属性赋值时调用的方法
    def celsius(self, value: float) -> None:  # setter 方法接收准备设置的新值
        if value < -273.15:  # 判断温度是否低于绝对零度
            raise ValueError("温度不能低于绝对零度")  # 不符合规则时抛出异常
        self._celsius = value  # 验证通过后更新内部属性

temperature = Temperature(25.0)  # 创建温度对象
print(temperature.celsius)  # 访问 property 属性时会执行 getter 方法
temperature.celsius = 30.0  # 给 property 属性赋值时会执行 setter 方法
print(temperature.celsius)  # 输出更新后的温度

# ============================================================  # 分隔线：注释不会被执行
# 15. dataclass 与枚举 Enum  # 快速定义数据类和一组固定选项
# ============================================================  # 分隔线：帮助组织代码结构

from dataclasses import dataclass  # 导入 dataclass 装饰器
from enum import Enum  # 导入 Enum 基类，用于创建枚举类型

@dataclass  # dataclass 会自动生成常用的数据类方法，例如 __init__ 和 __repr__
class Product:  # 定义一个主要用于保存数据的类
    name: str  # 字段注解说明 name 字段的类型
    price: float  # 字段注解说明 price 字段的类型
    in_stock: bool = True  # 字段可以设置默认值，默认值字段通常放在必填字段之后

product = Product("键盘", 199.0)  # 创建 dataclass 实例时可以使用位置参数
print(product)  # dataclass 自动提供易读的对象字符串表示

class OrderStatus(Enum):  # 继承 Enum 创建枚举类
    PENDING = "pending"  # 定义一个枚举成员
    PAID = "paid"  # 定义另一个枚举成员
    CANCELLED = "cancelled"  # 定义第三个枚举成员

status = OrderStatus.PAID  # 通过枚举类名和成员名访问枚举成员
print(status, status.value)  # value 属性用于获取枚举成员对应的值

# ============================================================  # 分隔线：注释不会被执行
# 16. 迭代器与生成器  # 按需逐个产生数据，而不是一次性保存全部数据
# ============================================================  # 分隔线：帮助组织代码结构

class CountDown:  # 定义一个可迭代对象
    def __init__(self, start: int) -> None:  # 保存倒计时的起始数字
        self.start = start  # 将起始数字保存为实例属性

    def __iter__(self):  # __iter__ 定义对象的迭代行为
        current = self.start  # 初始化当前数字
        while current > 0:  # 只要当前数字大于零就继续生成
            yield current  # yield 产生一个值，并在下次迭代时从这里继续
            current -= 1  # 每次生成后将数字减一

for remaining in CountDown(3):  # for 可以遍历实现了迭代协议的对象
    print("倒计时：", remaining)  # 逐个输出生成器产生的值

def simple_generator():  # 定义一个生成器函数
    yield "第一步"  # 第一次迭代时产生第一个值
    yield "第二步"  # 第二次迭代时产生第二个值
    yield "第三步"  # 第三次迭代时产生第三个值

for step in simple_generator():  # 调用含有 yield 的函数会得到生成器对象
    print(step)  # 每次循环从生成器中获取一个值

# ============================================================  # 分隔线：注释不会被执行
# 17. 装饰器  # 在不直接修改原函数代码的情况下扩展其行为
# ============================================================  # 分隔线：帮助组织代码结构

def log_call(func):  # 装饰器本质上是一个接收函数并返回函数的函数
    def wrapper(*args, **kwargs):  # 内层函数接收被装饰函数可能使用的参数
        print("函数开始执行：", func.__name__)  # __name__ 可以读取函数名称
        result = func(*args, **kwargs)  # 调用原函数并保存其返回值
        print("函数执行结束：", func.__name__)  # 原函数执行完成后输出提示
        return result  # 将原函数的返回值继续返回给调用者
    return wrapper  # 将包装后的函数返回出去

@log_call  # 使用 @语法将 log_call 应用到下面定义的函数
def say_hello() -> str:  # 定义一个将被装饰的普通函数
    return "Hello!"  # 返回字符串结果

print(say_hello())  # 调用装饰后的函数，会先后执行包装逻辑和原函数逻辑

# ============================================================  # 分隔线：注释不会被执行
# 18. 类型注解与联合类型  # 类型注解帮助阅读代码，也方便静态类型检查工具分析
# ============================================================  # 分隔线：帮助组织代码结构

def find_product(product_id: int) -> str | None:  # -> str | None 表示返回字符串或 None
    if product_id == 1:  # 判断是否找到指定商品
        return "机械键盘"  # 找到时返回商品名称
    return None  # 没找到时返回 None

found_product = find_product(1)  # 调用带类型注解的函数
print(found_product)  # 类型注解不会自动改变程序运行时的行为

# ============================================================  # 分隔线：注释不会被执行
# 19. 异步函数 async 与 await  # 用于编写异步任务，例如网络请求和异步 I/O
# ============================================================  # 分隔线：帮助组织代码结构

import asyncio  # 导入 Python 标准库中的异步 I/O 模块

async def fetch_data() -> str:  # async def 定义一个异步函数，也称为协程函数
    print("开始获取数据")  # 执行异步任务中的普通语句
    await asyncio.sleep(0.1)  # await 等待一个可等待对象完成，期间可以让出执行权
    return "数据获取完成"  # 异步函数也可以使用 return 返回结果

async def main() -> None:  # 定义异步程序的入口协程
    result = await fetch_data()  # 在另一个协程中使用 await 等待异步函数的结果
    print(result)  # 输出异步任务的返回结果

asyncio.run(main())  # asyncio.run() 创建并运行事件循环，执行 main 协程

# ============================================================  # 分隔线：注释不会被执行
# 20. 模块入口判断  # 区分文件被直接运行和被其他文件导入两种情况
# ============================================================  # 分隔线：帮助组织代码结构

def main() -> None:  # 约定俗成地使用 main() 组织程序的主要执行逻辑
    print("Python 语法综合练习完成！")  # 输出练习完成提示

if __name__ == "__main__":  # 只有文件被直接运行时，__name__ 才等于 "__main__"
    main()  # 调用主函数，作为整个脚本的程序入口
