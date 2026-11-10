# 三引号表示多行字符串；文件开头的字符串也是模块文档字符串。
"""个人记账本：使用标准库实现一个可以持久化的命令行程序。

建议按文件从上到下跟敲。先理解业务，再留意注释中的 Python 语法。
运行示例见同目录 README.md；本程序不需要安装第三方依赖。
"""

# from 模块 import 名称用于导入名称；此处延迟处理类型注解，必须放在普通导入之前。
from __future__ import annotations

# import 导入模块；通过模块名.名称访问其中的功能。
import argparse
import logging
import sqlite3
import sys
from dataclasses import dataclass
from datetime import date
# 逗号可以分隔多个要导入的名称。
from decimal import Decimal, InvalidOperation
from functools import wraps
from pathlib import Path
from typing import Callable, Iterator, TypeVar

# 常量通常使用全大写；Path 可以跨平台拼接和处理文件路径。
# = 将右侧的值绑定给变量；引号表示字符串，点号访问属性或方法，括号调用函数。Path 的 / 用来拼接路径。
DEFAULT_DB = Path(__file__).resolve().parent / "data" / "expenses.db"
# __name__ 是模块名；直接执行文件时它是 "__main__"。
LOGGER = logging.getLogger(__name__)
# TypeVar 创建类型变量；bound= 是关键字参数，Callable[..., object] 表示参数不限的可调用对象。类型注解不会自动校验参数。
F = TypeVar("F", bound=Callable[..., object])


# class 定义类，括号内是父类；冒号后缩进的代码属于类体。这里定义自定义异常。
class ValidationError(ValueError):
    """输入不符合业务规则时抛出，调用者可以单独捕获。"""


# def 定义函数；参数后的 : F 和 -> F 分别是参数、返回值类型注解；缩进表示函数体。
def log_operation(func: F) -> F:
    """装饰器：给操作增加日志；@wraps 保留原函数的名称等信息。"""
    # @ 是装饰器语法；wraps 帮助包装函数保留原函数的名称和文档等信息。
    @wraps(func)
    # 函数可以嵌套定义；*args 收集位置参数为元组，**kwargs 收集关键字参数为字典。
    def wrapper(*args: object, **kwargs: object) -> object:
        # 对象.方法(...) 调用方法；这里 %s 是 logging 格式化占位符。
        LOGGER.info("开始执行：%s", func.__name__)
        # 调用时 * 和 ** 分别解包位置参数和关键字参数，调用结果赋给 result。
        result = func(*args, **kwargs)
        LOGGER.info("执行完成：%s", func.__name__)
        # return 返回结果并结束函数；函数也是对象，可以作为返回值。
        # 不带表达式的 return 结束函数并返回 None。
        return result

    # type: ignore 是静态类型检查器指令，不影响运行。
    return wrapper  # type: ignore[return-value]


def parse_amount(text: str) -> int:
    """将金额字符串转换成整数分，避免用 float 处理货币的精度问题。"""
    # try 包含可能出错的代码；except 捕获匹配的异常。
    try:
        amount = Decimal(text)
    # except 异常类型 as exc 捕获异常并绑定到变量 exc。
    except InvalidOperation as exc:
        # raise 主动抛出异常；from exc 保留原异常作为原因。
        raise ValidationError("金额必须是数字，例如 12.50") from exc
    # if 条件成立才执行缩进代码；not 表示取反，or 表示任一条件成立，<= 表示小于或等于。
    if not amount.is_finite() or amount <= 0:
        raise ValidationError("金额必须是大于 0 的有限数字")
    # 限制范围既便于业务使用，也保证整数分能存入 SQLite。
    # > 是大于；Decimal 使用十进制计算，适合表示货币。
    if amount > Decimal("1000000000"):
        raise ValidationError("单笔金额不能超过 1000000000 元")
    # 链式访问先调用 as_tuple() 再读取 exponent；< 是小于，-2 是负整数。
    if amount.as_tuple().exponent < -2:
        raise ValidationError("金额最多保留两位小数")
    # * 是乘法；int(...) 转换成整数，嵌套调用先计算内部表达式。
    return int(amount * 100)


def parse_date(text: str) -> str:
    """检查日期并统一为 ISO 格式，例如 2026-11-01。"""
    try:
        return date.fromisoformat(text).isoformat()
    except ValueError as exc:
        raise ValidationError("日期必须是有效的 YYYY-MM-DD 格式") from exc


# 参数之间用逗号分隔；单独的 * 后是只能用关键字传入的参数，= 100 指定默认值。
def clean_text(text: str, field: str, *, limit: int = 100) -> str:
    """* 后面的参数只能通过关键字传入，例如 limit=20。"""
    # strip() 返回去除首尾空白的新字符串。
    value = text.strip()
    # 空字符串在条件判断中为假，因此 not value 可检查空字符串。
    if not value:
        # f 字符串的 {表达式} 会插入变量或表达式的结果。
        raise ValidationError(f"{field}不能为空")
    # len 求长度；any 判断是否存在真值。括号内是生成器表达式；in 判断成员，\r、\n、\t 是转义字符。
    if len(value) > limit or any(ch in value for ch in "\r\n\t"):
        raise ValidationError(f"{field}不能超过 {limit} 个字符，也不能包含换行或制表符")
    return value


def format_money(cents: int) -> str:
    """整数分格式化为两位小数；divmod 返回商和余数。"""
    # 序列解包：将 divmod 返回的商和余数分别赋给两个变量。
    yuan, fen = divmod(cents, 100)
    # 格式说明符 02d 表示整数至少两位，不足时左侧补零。
    return f"{yuan}.{fen:02d}"


# 带参数的类装饰器：dataclass 自动生成初始化等方法；frozen=True 禁止重新赋值，slots=True 限制实例属性。True 和 False 是布尔值。
@dataclass(frozen=True, slots=True)
class Expense:
    """一条支出记录。frozen=True 让对象创建后不可修改。"""
    # 类中的“名称: 类型”是字段注解，dataclass 根据字段生成初始化方法。
    id: int
    spent_on: str
    category: str
    amount_cents: int
    note: str

    # @property 将方法包装为属性，访问时不用加括号。
    @property
    # 实例方法的第一个参数通常叫 self，代表当前实例，调用时由 Python 传入。
    def amount(self) -> str:
        return format_money(self.amount_cents)

    # @classmethod 定义类方法；第一个参数 cls 代表当前类。
    @classmethod
    def from_row(cls, row: sqlite3.Row) -> Expense:
        # 方括号按键取值；row["id"] 读取结果行的 id 列。
        return cls(row["id"], row["spent_on"], row["category"], row["amount_cents"], row["note"])


class ExpenseRepository:
    """负责数据库读写；业务输入校验放在调用它之前。"""

    # __init__ 是实例初始化方法；-> None 表示没有有意义的返回值。
    def __init__(self, db_path: Path) -> None:
        # 左侧给实例属性赋值，右侧是传入的参数。
        self.db_path = db_path
        # parents=True 和 exist_ok=True 是关键字参数，分别允许创建父目录和忽略目录已存在。
        self.db_path.parent.mkdir(parents=True, exist_ok=True)
        self._initialize()

    # 单下划线前缀按惯例表示内部使用，不是严格的访问权限。
    def _connect(self) -> sqlite3.Connection:
        connection = sqlite3.connect(self.db_path)
        connection.row_factory = sqlite3.Row
        return connection

    def _initialize(self) -> None:
        # connection 的上下文管理器处理事务，但不会关闭连接；finally 负责关闭。
        connection = self._connect()
        try:
            # with 使用上下文管理器；这里成功时提交事务，异常时回滚。
            with connection:
                connection.execute(
                    # 三引号也可创建普通多行字符串；此处内容是 SQL 语句。
                    """CREATE TABLE IF NOT EXISTS expenses (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        spent_on TEXT NOT NULL,
                        category TEXT NOT NULL,
                        amount_cents INTEGER NOT NULL CHECK (amount_cents > 0),
                        note TEXT NOT NULL
                    )"""
                )
        # finally 用于无论是否发生异常都需要执行的清理操作，这里关闭连接。
        finally:
            connection.close()

    # 这里使用前面定义的装饰器，包装 add 方法并记录日志。
    @log_operation
    def add(self, spent_on: str, category: str, amount_cents: int, note: str) -> int:
        connection = self._connect()
        try:
            with connection:
                # 使用占位符传参，避免把用户输入拼接进 SQL。
                cursor = connection.execute(
                    "INSERT INTO expenses (spent_on, category, amount_cents, note) VALUES (?, ?, ?, ?)",
                    # 逗号分隔的值构成元组；这里作为 SQL 占位符参数。
                    (spent_on, category, amount_cents, note),
                )
                # assert 条件为假时抛出 AssertionError；is not None 判断不是 None。assert 可能被优化模式跳过，不用于校验用户输入。
                assert cursor.lastrowid is not None
                return cursor.lastrowid
        finally:
            connection.close()

    # list[Expense] 是泛型类型注解，表示元素为 Expense 的列表。
    def list_all(self) -> list[Expense]:
        connection = self._connect()
        try:
            rows = connection.execute(
                "SELECT id, spent_on, category, amount_cents, note FROM expenses ORDER BY spent_on DESC, id DESC"
            ).fetchall()
            # 列表推导式：将每一行转换成 Expense 对象。
            return [Expense.from_row(row) for row in rows]
        finally:
            connection.close()

    @log_operation
    def delete(self, expense_id: int) -> bool:
        connection = self._connect()
        try:
            with connection:
                # (expense_id,) 是单元素元组；逗号不能省略。
                cursor = connection.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
                return cursor.rowcount > 0
        finally:
            connection.close()


# str | None 表示可以是字符串或 None；Iterator[Expense] 表示 Expense 的迭代器。
def filter_expenses(items: list[Expense], month: str | None) -> Iterator[Expense]:
    """生成器：按需产出记录；yield 会暂停函数并保留当前位置。"""
    # for 变量 in 可迭代对象：逐个遍历元素，并执行缩进的循环体。
    for item in items:
        # is None 判断是否为 None；+ 可以拼接字符串，startswith 检查开头。
        if month is None or item.spent_on.startswith(month + "-"):
            # yield 产出一个值并暂停函数；包含 yield 的函数返回生成器。
            yield item


def validate_month(text: str) -> str:
    # 用完整日期复用标准库的日期校验，且要求月份为两位。
    # != 表示不相等；text[4] 按下标取字符，下标从 0 开始。
    if len(text) != 7 or text[4] != "-":
        raise ValidationError("月份格式必须是 YYYY-MM")
    parse_date(text + "-01")
    return text


def print_records(items: list[Expense]) -> None:
    if not items:
        print("没有找到支出记录。")
        return
    print("ID | 日期 | 分类 | 金额（元） | 备注")
    for item in items:
        print(f"{item.id} | {item.spent_on} | {item.category} | {item.amount} | {item.note}")
    # sum 求和；其中的 for 是生成器表达式，逐个提供金额。
    print(f"共 {len(items)} 笔，合计 {format_money(sum(item.amount_cents for item in items))} 元")


def print_summary(items: list[Expense]) -> None:
    # 变量也可带类型注解；dict[str, int] 描述字典键和值的类型，{} 创建空字典。
    totals: dict[str, int] = {}
    for item in items:
        # 字典用 [键] 读写值；get(键, 默认值) 在键不存在时返回默认值。
        totals[item.category] = totals.get(item.category, 0) + item.amount_cents
    if not totals:
        print("没有可统计的支出记录。")
        return
    # lambda 是短小的匿名函数；按金额降序，同金额时按分类排序。
    # sorted 返回新列表；lambda 创建匿名函数作为排序依据，元组先比较第一项，负号实现金额降序。循环时解包两个值。
    for category, cents in sorted(totals.items(), key=lambda pair: (-pair[1], pair[0])):
        print(f"{category}: {format_money(cents)} 元")
    print(f"总计: {format_money(sum(totals.values()))} 元")


def build_parser() -> argparse.ArgumentParser:
    # 名称=值是关键字参数；argparse 按配置解析命令行。
    parser = argparse.ArgumentParser(description="个人记账本：记录、查看和统计支出")
    parser.add_argument("--db", type=Path, default=DEFAULT_DB, help="数据库路径（默认保存在项目 data 目录）")
    # action="store_true" 表示指定该选项时为 True，否则为 False。
    parser.add_argument("--verbose", action="store_true", help="显示操作日志")
    # 子命令区分操作；required=True 要求选择一个子命令。
    commands = parser.add_subparsers(dest="command", required=True)

    add = commands.add_parser("add", help="新增一笔支出")
    add.add_argument("amount", help="金额（元），例如 12.50")
    add.add_argument("category", help="分类，例如 餐饮")
    add.add_argument("--date", default=date.today().isoformat(), help="日期，默认今天，格式 YYYY-MM-DD")
    add.add_argument("--note", default="", help="可选备注")

    # 嵌套元组存放多组值；循环时把每组两个值解包到两个变量。
    for name, help_text in (("list", "查看记录"), ("summary", "按分类统计")):
        command = commands.add_parser(name, help=help_text)
        command.add_argument("--month", help="只查看指定月份，例如 2026-11")

    delete = commands.add_parser("delete", help="按 ID 删除一笔记录")
    delete.add_argument("id", type=int, help="记录 ID")
    return parser


# 参数默认值为 None；调用时也可以传入字符串列表。
def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    # “值1 if 条件 else 值2”是条件表达式，根据条件选取一个值。
    logging.basicConfig(level=logging.INFO if args.verbose else logging.WARNING, format="%(levelname)s: %(message)s")
    try:
        # 先校验，再打开数据库，避免错误输入产生不必要的文件。
        # == 比较值是否相等；点号读取解析结果对象的属性。
        if args.command == "add":
            amount = parse_amount(args.amount)
            category = clean_text(args.category, "分类", limit=30)
            spent_on = parse_date(args.date)
            note = clean_text(args.note, "备注") if args.note else ""
            repository = ExpenseRepository(args.db)
            new_id = repository.add(spent_on, category, amount, note)
            print(f"已新增记录，ID：{new_id}")
        # elif 在前面的条件不成立时继续判断；{...} 此处创建集合，in 检查成员。
        elif args.command in {"list", "summary"}:
            month = validate_month(args.month) if args.month else None
            repository = ExpenseRepository(args.db)
            items = list(filter_expenses(repository.list_all(), month))
            if args.command == "list":
                print_records(items)
            # else 是对应条件不成立时执行的分支。
            else:
                print_summary(items)
        elif args.command == "delete":
            if args.id <= 0:
                raise ValidationError("ID 必须是正整数")
            repository = ExpenseRepository(args.db)
            if not repository.delete(args.id):
                print(f"未找到 ID 为 {args.id} 的记录。", file=sys.stderr)
                return 1
            print(f"已删除 ID 为 {args.id} 的记录。")
        return 0
    # except 使用异常类型元组，可以统一处理多种异常。
    except (ValidationError, sqlite3.Error, OSError) as exc:
        # print 的 file 参数指定输出流；sys.stderr 是标准错误输出。
        print(f"操作失败：{exc}", file=sys.stderr)
        return 1


# 只有直接运行本文件时才执行；被其他模块 import 时不会自动运行。
# 程序入口判断：直接运行文件时成立，作为模块导入时不成立。
if __name__ == "__main__":
    # SystemExit 携带进程退出状态，通常 0 表示成功，非 0 表示失败。
    raise SystemExit(main())
