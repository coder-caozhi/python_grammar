# -*- coding: utf-8 -*-  # 声明文件编码，确保中文注释和字符串正常显示
"""迷你电商订单系统：用真实业务流程练习 Python 语法。"""  # 模块文档字符串，说明本文件的用途

from __future__ import annotations  # 延迟解析类型注解，允许类型注解引用后面定义的类
import asyncio  # 导入异步编程模块，用于模拟订单通知
import json  # 导入 JSON 模块，用于导出订单数据
from dataclasses import dataclass, field  # 导入数据类装饰器和字段工厂函数
from datetime import datetime  # 导入日期时间类，用于生成订单编号和创建时间
from decimal import Decimal, ROUND_HALF_UP  # 使用 Decimal 处理金额，避免浮点数精度问题
from enum import Enum  # 导入枚举基类，用于定义订单状态和支付方式
from functools import wraps  # 导入 wraps，保留装饰前函数的名称等信息
from pathlib import Path  # 导入 Path，使用面向对象的方式操作文件路径
from typing import Any, Callable, Iterator  # 导入类型注解工具，说明函数参数和返回值类型


# ============================================================  # 模块分隔：业务异常
# 一、业务异常  # 将可预期的业务错误与普通程序错误区分开
# ============================================================  # 模块分隔：业务异常

class BusinessError(Exception):  # 定义业务异常基类，其他业务异常继承它
    """所有业务异常的父类。"""  # 类文档字符串，说明该异常的用途


class ProductNotFoundError(BusinessError):  # 商品不存在时使用的异常类型
    pass  # pass 表示暂时不需要增加实现，直接继承父类行为


class InsufficientStockError(BusinessError):  # 商品库存不足时使用的异常类型
    pass  # 使用独立异常类型，方便调用方精确捕获


class CouponError(BusinessError):  # 优惠券不可用时使用的异常类型
    pass  # 空类使用 pass 占位


class PaymentError(BusinessError):  # 支付失败或支付方式不支持时使用的异常类型
    pass  # 当前异常只用于标识错误类别


# ============================================================  # 模块分隔：枚举和常量
# 二、订单状态、支付方式与业务配置  # 用枚举和常量统一管理固定值
# ============================================================  # 模块分隔：枚举和常量

class OrderStatus(Enum):  # 继承 Enum，定义订单状态枚举
    PAID = "paid"  # 已支付状态
    PENDING_PAYMENT = "pending_payment"  # 等待支付状态，例如货到付款
    CANCELLED = "cancelled"  # 已取消状态


class PaymentMethod(Enum):  # 定义系统支持的支付方式
    CARD = "card"  # 银行卡支付
    WALLET = "wallet"  # 电子钱包支付
    CASH = "cash"  # 货到付款


FREE_SHIPPING_LIMIT = Decimal("300.00")  # 商品金额达到 300 元时免运费
SHIPPING_FEE = Decimal("12.00")  # 未达到免运费门槛时收取 12 元运费
LOW_STOCK_LIMIT = 5  # 库存小于或等于 5 件时触发低库存提醒
Cart = dict[str, int]  # 定义类型别名：购物车是 SKU 到购买数量的映射


# ============================================================  # 模块分隔：商品模型
# 三、商品模型  # 商品类负责保存商品信息和管理自身库存
# ============================================================  # 模块分隔：商品模型

@dataclass  # dataclass 自动生成 __init__、__repr__ 等常用方法
class Product:  # 定义商品类，用于创建商品对象
    sku: str  # 商品唯一编码
    name: str  # 商品名称
    category: str  # 商品分类
    price: Decimal  # 商品单价使用 Decimal 表示
    stock: int  # 当前库存数量
    active: bool = True  # 是否上架，默认值为 True

    def __post_init__(self) -> None:  # dataclass 初始化完成后自动调用该方法
        self.sku = self.sku.strip().upper()  # strip 去除空白，upper 将 SKU 统一转成大写
        if self.price <= 0:  # if 判断商品价格是否大于零
            raise ValueError("商品价格必须大于 0")  # raise 主动抛出异常，阻止创建非法商品
        if self.stock < 0:  # 判断库存是否为负数
            raise ValueError("商品库存不能小于 0")  # 库存不合法时抛出 ValueError

    @property  # property 将方法变成可通过对象属性访问的只读属性
    def inventory_value(self) -> Decimal:  # 声明库存总价值属性的返回类型
        return self.price * self.stock  # 商品单价乘以库存数量，得到库存总价值

    @property  # 再定义一个只读属性
    def available(self) -> bool:  # 返回商品当前是否可购买
        return self.active and self.stock > 0  # and 要求商品已上架且库存大于零

    @classmethod  # classmethod 将方法绑定到类，第一个参数 cls 代表当前类
    def from_record(cls, data: dict[str, Any]) -> Product:  # 从字典记录创建商品对象
        return cls(data["sku"], data["name"], data["category"], Decimal(str(data["price"])), int(data["stock"]), bool(data.get("active", True)))  # 读取字典字段并转换成商品对象需要的数据类型

    def reduce_stock(self, quantity: int) -> None:  # 定义扣减库存的方法
        if quantity <= 0:  # 检查购买数量是否为正数
            raise ValueError("扣减库存的数量必须大于 0")  # 数量不合法时抛出异常
        if quantity > self.stock:  # 检查购买数量是否超过当前库存
            raise InsufficientStockError(f"{self.name} 库存不足，当前库存为 {self.stock}")  # f-string 将商品名称和库存插入错误消息
        self.stock -= quantity  # -= 是增强赋值运算符，等价于 self.stock = self.stock - quantity

    def increase_stock(self, quantity: int) -> None:  # 定义增加库存的方法，取消订单时会调用
        if quantity <= 0:  # 检查增加数量是否为正数
            raise ValueError("增加库存的数量必须大于 0")  # 数量不合法时抛出异常
        self.stock += quantity  # += 是增强赋值运算符，将库存增加指定数量


# ============================================================  # 模块分隔：优惠券模型
# 四、优惠券模型  # 优惠券类负责校验优惠规则和计算折扣
# ============================================================  # 模块分隔：优惠券模型

@dataclass  # 使用 dataclass 自动生成优惠券对象的初始化方法
class Coupon:  # 定义优惠券类
    code: str  # 优惠券编码
    rate: Decimal  # 折扣比例，例如 0.10 表示优惠 10%
    minimum_amount: Decimal  # 使用优惠券需要达到的最低商品金额
    max_discount: Decimal | None = None  # 联合类型表示最大优惠金额可以是 Decimal 或 None
    active: bool = True  # 优惠券默认启用

    def __post_init__(self) -> None:  # 在对象初始化完成后执行数据校验
        self.code = self.code.strip().upper()  # 统一优惠券编码的大小写和空格
        if not Decimal("0") < self.rate <= Decimal("1"):  # 链式比较检查折扣比例是否在合法范围
            raise ValueError("折扣比例必须大于 0 且小于或等于 1")  # 不合法时抛出异常

    def calculate(self, subtotal: Decimal) -> Decimal:  # 根据商品总金额计算优惠金额
        if not self.active:  # 判断优惠券是否已停用
            raise CouponError(f"优惠券 {self.code} 已停用")  # 抛出优惠券业务异常
        if subtotal < self.minimum_amount:  # 判断商品金额是否达到优惠券使用门槛
            raise CouponError(f"使用 {self.code} 至少需要消费 {self.minimum_amount} 元")  # 告知用户未达到使用条件
        discount = subtotal * self.rate  # 按照折扣比例计算优惠金额
        if self.max_discount is not None:  # is not None 明确判断是否设置优惠上限
            discount = min(discount, self.max_discount)  # min 取较小值，避免优惠金额超过上限
        return discount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)  # quantize 保留两位小数并使用四舍五入


# ============================================================  # 模块分隔：订单模型
# 五、订单模型  # 将订单明细和订单整体信息拆分
# ============================================================  # 模块分隔：订单模型

@dataclass  # 自动生成订单明细对象的初始化方法
class OrderItem:  # 定义订单中的一条商品明细
    sku: str  # 商品 SKU
    product_name: str  # 下单时的商品名称快照
    unit_price: Decimal  # 下单时的商品单价快照
    quantity: int  # 购买数量

    @property  # 将明细金额包装成只读属性
    def line_total(self) -> Decimal:  # 定义订单明细总金额
        return self.unit_price * self.quantity  # 单价乘以数量得到明细金额


@dataclass  # 自动生成订单对象的初始化方法
class Order:  # 定义订单实体，保存一次交易的完整信息
    order_id: str  # 订单编号
    customer: str  # 客户名称
    items: list[OrderItem]  # 订单包含的商品明细列表
    discount: Decimal  # 优惠金额
    shipping: Decimal  # 运费
    payment_method: PaymentMethod  # 支付方式枚举
    status: OrderStatus  # 订单状态枚举
    coupon_code: str | None = None  # 使用的优惠券编码，没有使用时为 None
    created_at: datetime = field(default_factory=datetime.now)  # default_factory 为每个订单单独生成创建时间

    @property  # 将商品金额汇总逻辑包装成属性
    def subtotal(self) -> Decimal:  # subtotal 表示优惠前的商品总金额
        return sum((item.line_total for item in self.items), start=Decimal("0.00"))  # 生成器表达式逐项计算金额，再用 sum 求和

    @property  # 将最终应付金额包装成属性
    def total(self) -> Decimal:  # total 表示用户最终需要支付的金额
        return self.subtotal - self.discount + self.shipping  # 商品总额减优惠金额再加运费

    def __str__(self) -> str:  # __str__ 定义对象被 print 输出时的展示内容
        return f"{self.order_id} | {self.customer} | {self.status.value} | ￥{self.total:.2f}"  # 返回易读的订单摘要字符串


# ============================================================  # 模块分隔：装饰器
# 六、业务日志装饰器  # 不修改原函数，也可以给业务操作增加日志
# ============================================================  # 模块分隔：装饰器

def log_action(func: Callable[..., Any]) -> Callable[..., Any]:  # 定义一个接收函数并返回函数的装饰器
    @wraps(func)  # 保留原函数的名称和文档字符串等信息
    def wrapper(*args: Any, **kwargs: Any) -> Any:  # *args 收集位置参数，**kwargs 收集关键字参数
        print(f"[日志] 开始执行：{func.__name__}")  # __name__ 获取原函数名称
        try:  # try 中放置可能发生异常的业务调用
            result = func(*args, **kwargs)  # 将参数传给原函数，并保存它的返回结果
        except Exception as error:  # except 捕获异常对象
            print(f"[日志] 执行失败：{error}")  # 输出失败原因，真实项目中通常写入日志系统
            raise  # 不带参数的 raise 会重新抛出当前异常
        else:  # try 中没有发生异常时执行 else
            print(f"[日志] 执行成功：{func.__name__}")  # 记录业务函数执行成功
            return result  # 将原函数返回值交还给调用方
    return wrapper  # 返回包装函数，完成装饰器定义


# ============================================================  # 模块分隔：订单服务
# 七、订单服务  # 负责协调购物车、商品、优惠券、支付和订单
# ============================================================  # 模块分隔：订单服务

class OrderService:  # 定义订单服务类，将相关业务操作集中管理
    def __init__(self, products: list[Product], coupons: list[Coupon] | None = None) -> None:  # 初始化服务并接收商品和优惠券
        self.products = {product.sku: product for product in products}  # 字典推导式建立 SKU 到商品对象的索引
        self.coupons = {coupon.code: coupon for coupon in (coupons or [])}  # 使用 or 提供空列表默认值，再建立优惠券索引
        self.orders: list[Order] = []  # 创建订单列表，保存本次程序运行期间创建的订单

    @staticmethod  # staticmethod 定义静态方法，不自动接收 self 或 cls
    def normalize_code(value: str) -> str:  # 定义统一处理商品编码和优惠券编码的方法
        return value.strip().upper()  # 去除两端空白并转换成大写

    def add_to_cart(self, cart: Cart, sku: str, quantity: int = 1) -> None:  # 定义加入购物车方法，quantity 默认值为 1
        sku = self.normalize_code(sku)  # 规范化用户输入的商品 SKU
        if quantity <= 0:  # 检查购买数量是否大于零
            raise ValueError("购买数量必须大于 0")  # 数量不合法时抛出异常
        product = self.products.get(sku)  # dict.get 根据 SKU 查找商品，不存在时返回 None
        if product is None:  # is None 判断是否没有找到商品
            raise ProductNotFoundError(f"商品 {sku} 不存在")  # 商品不存在时抛出自定义异常
        if not product.available:  # not 对布尔值取反，判断商品当前是否不可购买
            raise InsufficientStockError(f"商品 {product.name} 当前不可购买")  # 商品下架或无库存时拒绝加入购物车
        cart[sku] = cart.get(sku, 0) + quantity  # get 读取原数量，随后将本次数量累加到购物车
        print(f"已加入购物车：{product.name} x {quantity}")  # 输出加入购物车的业务结果

    def _build_items(self, cart: Cart) -> list[OrderItem]:  # 下划线前缀表示这是类内部使用的辅助方法
        if not cart:  # 空字典在布尔判断中为 False，可直接判断购物车是否为空
            raise BusinessError("购物车不能为空")  # 购物车为空时不能创建订单
        if any(quantity <= 0 for quantity in cart.values()):  # any 检查是否至少有一个购买数量不合法
            raise BusinessError("购物车中存在不合法的购买数量")  # 存在非法数量时终止下单
        items: list[OrderItem] = []  # 创建空列表，用来保存订单明细
        for sku, quantity in cart.items():  # items 同时遍历字典中的键和值，分别得到 SKU 和数量
            product = self.products.get(sku)  # 根据 SKU 查找商品
            if product is None:  # 判断商品是否存在
                raise ProductNotFoundError(f"商品 {sku} 不存在")  # 商品不存在时抛出异常
            if not product.active:  # 判断商品是否已经下架
                raise BusinessError(f"商品 {product.name} 已下架")  # 已下架商品不能下单
            if quantity > product.stock:  # 判断购买数量是否超过库存
                raise InsufficientStockError(f"{product.name} 库存不足，当前库存：{product.stock}")  # 库存不足时抛出业务异常
            items.append(OrderItem(sku, product.name, product.price, quantity))  # 创建订单明细对象并添加到列表
        return items  # 返回已经通过校验的订单明细

    def _calculate_discount(self, subtotal: Decimal, code: str | None) -> Decimal:  # 根据订单金额和优惠券编码计算优惠金额
        if code is None or code.strip() == "":  # 没有传入优惠券编码时不进行优惠
            return Decimal("0.00")  # 没有优惠券就返回零优惠
        code = self.normalize_code(code)  # 规范化优惠券编码
        coupon = self.coupons.get(code)  # 根据编码查找优惠券对象
        if coupon is None:  # 判断优惠券是否存在
            raise CouponError(f"优惠券 {code} 不存在")  # 不存在时抛出优惠券异常
        return coupon.calculate(subtotal)  # 将优惠规则交给 Coupon 对象计算，体现职责分离

    def _calculate_shipping(self, subtotal: Decimal) -> Decimal:  # 根据商品金额计算运费
        if subtotal >= FREE_SHIPPING_LIMIT:  # 判断是否达到免运费门槛
            return Decimal("0.00")  # 达到门槛时免运费
        return SHIPPING_FEE  # 未达到门槛时返回标准运费

    def _pay(self, method: PaymentMethod, amount: Decimal) -> OrderStatus:  # 模拟支付流程，并返回支付后的订单状态
        if amount <= 0:  # 检查最终应付金额是否大于零
            raise PaymentError("支付金额必须大于 0")  # 非正金额不允许支付
        match method:  # match-case 根据支付方式选择不同处理逻辑，要求 Python 3.10+
            case PaymentMethod.CARD:  # 匹配银行卡支付
                print(f"银行卡支付成功：￥{amount:.2f}")  # 模拟银行卡支付成功
                return OrderStatus.PAID  # 返回已支付状态
            case PaymentMethod.WALLET:  # 匹配电子钱包支付
                print(f"电子钱包支付成功：￥{amount:.2f}")  # 模拟电子钱包支付成功
                return OrderStatus.PAID  # 返回已支付状态
            case PaymentMethod.CASH:  # 匹配货到付款
                print("已选择货到付款")  # 输出货到付款提示
                return OrderStatus.PENDING_PAYMENT  # 返回等待支付状态
            case _:  # 下划线表示兜底匹配
                raise PaymentError(f"暂不支持支付方式：{method}")  # 不支持的支付方式抛出异常

    @log_action  # 使用装饰器记录 checkout 方法的执行过程
    def checkout(self, customer: str, cart: Cart, *, coupon_code: str | None = None, payment_method: PaymentMethod = PaymentMethod.CARD) -> Order:  # * 后面的参数必须通过关键字传递
        customer = customer.strip()  # 清理客户名称两端的空白字符
        if not customer:  # 空字符串在布尔判断中为 False
            raise BusinessError("客户名称不能为空")  # 客户名称为空时拒绝下单
        items = self._build_items(cart)  # 第一步：校验购物车并构建订单明细，暂时不修改库存
        subtotal = sum((item.line_total for item in items), start=Decimal("0.00"))  # 使用生成器表达式和 sum 汇总商品金额
        discount = self._calculate_discount(subtotal, coupon_code)  # 第二步：计算优惠金额
        shipping = self._calculate_shipping(subtotal)  # 第三步：计算运费
        total = subtotal - discount + shipping  # 第四步：计算最终应付金额
        status = self._pay(payment_method, total)  # 第五步：模拟支付，支付失败时还没有扣减库存
        order_id = f"ORD-{datetime.now():%Y%m%d%H%M%S}-{len(self.orders) + 1:03d}"  # 使用当前时间和订单数量生成演示用订单编号
        order = Order(order_id, customer, items, discount, shipping, payment_method, status, self.normalize_code(coupon_code) if coupon_code else None)  # 根据计算结果创建订单对象
        assert order.total == total, "订单金额计算不一致"  # assert 验证内部金额是否一致，不成立时抛出 AssertionError
        for item in items:  # 遍历订单明细，逐个扣减对应商品库存
            self.products[item.sku].reduce_stock(item.quantity)  # 调用商品对象的方法扣减库存
        self.orders.append(order)  # 将订单保存到订单列表
        cart.clear()  # 下单成功后清空购物车，避免重复提交
        return order  # 将创建完成的订单返回给调用方

    @log_action  # 为取消订单操作增加日志
    def cancel_order(self, order_id: str) -> Order:  # 根据订单编号取消订单
        order = next((item for item in self.orders if item.order_id == order_id), None)  # next 从生成器表达式中取出首个匹配订单，找不到时返回 None
        if order is None:  # 判断订单是否存在
            raise BusinessError(f"订单 {order_id} 不存在")  # 不存在的订单不能取消
        if order.status is OrderStatus.CANCELLED:  # is 判断枚举成员身份，防止重复取消
            raise BusinessError("订单已经取消，不能重复取消")  # 防止重复恢复库存
        for item in order.items:  # 遍历订单中的每一条商品明细
            self.products[item.sku].increase_stock(item.quantity)  # 将下单时扣减的库存恢复
        order.status = OrderStatus.CANCELLED  # 更新订单状态
        return order  # 返回取消后的订单对象

    def search_products(self, keyword: str) -> list[Product]:  # 根据关键词搜索商品名称或分类
        keyword = keyword.strip().lower()  # 去除空格并转成小写，降低大小写差异
        return [product for product in self.products.values() if keyword in product.name.lower() or keyword in product.category.lower()]  # 列表推导式筛选符合关键词的商品

    def list_products_by_price(self) -> list[Product]:  # 按商品价格从低到高返回商品
        return sorted(self.products.values(), key=lambda product: product.price)  # sorted 返回新列表，lambda 指定排序依据

    def low_stock_products(self, limit: int = LOW_STOCK_LIMIT) -> Iterator[Product]:  # 返回迭代器类型，调用方可以逐个读取低库存商品
        for product in self.products.values():  # 遍历所有商品
            if product.active and (stock := product.stock) <= limit:  # 海象运算符 := 在判断时同时把库存赋值给 stock
                yield product  # yield 逐个产生结果，不需要一次性创建完整列表

    def orders_by_status(self, status: OrderStatus) -> list[Order]:  # 根据订单状态查询订单
        return [order for order in self.orders if order.status is status]  # 列表推导式筛选指定状态的订单

    def export_order(self, order: Order, directory: Path = Path("order_exports")) -> Path:  # 将订单导出为 JSON 文件，directory 有默认值
        directory.mkdir(parents=True, exist_ok=True)  # 创建导出目录，目录已存在时不报错
        file_path = directory / f"{order.order_id}.json"  # 使用 Path 的 / 运算符拼接文件路径
        data = {  # 创建准备写入 JSON 文件的字典
            "order_id": order.order_id,  # 保存订单编号
            "customer": order.customer,  # 保存客户名称
            "status": order.status.value,  # 枚举对象取 value 后才能作为普通字符串写入 JSON
            "payment_method": order.payment_method.value,  # 保存支付方式
            "subtotal": str(order.subtotal),  # Decimal 转成字符串，避免 JSON 无法直接序列化 Decimal
            "discount": str(order.discount),  # 保存优惠金额
            "shipping": str(order.shipping),  # 保存运费
            "total": str(order.total),  # 保存最终应付金额
            "created_at": order.created_at.isoformat(),  # 使用 ISO 格式保存日期时间
            "items": [{"sku": item.sku, "name": item.product_name, "price": str(item.unit_price), "quantity": item.quantity, "line_total": str(item.line_total)} for item in order.items],  # 列表推导式将订单明细转换成 JSON 可序列化的字典列表
        }  # 订单数据字典结束
        with file_path.open("w", encoding="utf-8") as file:  # with 自动关闭文件，w 表示覆盖写入
            json.dump(data, file, ensure_ascii=False, indent=2)  # 将字典写入 JSON，保留中文并设置缩进
        return file_path  # 返回文件路径，方便调用方查看导出位置

    def print_inventory(self) -> None:  # 输出当前库存报表
        print("\n========== 库存报表 ==========")  # \n 表示换行，让报表更清晰
        products = sorted(self.products.values(), key=lambda product: product.stock)  # 按库存从低到高排序
        for index, product in enumerate(products, start=1):  # enumerate 同时提供序号和商品对象，序号从 1 开始
            if not product.active:  # 已下架商品不显示在可售库存报表中
                continue  # continue 跳过当前循环，直接处理下一件商品
            print(f"{index}. {product.name} | 库存 {product.stock} | 库存价值 ￥{product.inventory_value:.2f}")  # 输出商品库存和库存总价值


# ============================================================  # 模块分隔：异步通知
# 八、异步业务通知  # 模拟订单创建后发送通知和低库存提醒
# ============================================================  # 模块分隔：异步通知

async def send_order_notification(order: Order) -> None:  # async def 定义协程函数，调用时需要 await 或事件循环执行
    print(f"\n正在向 {order.customer} 发送订单通知……")  # 输出通知开始信息
    await asyncio.sleep(0.2)  # await 等待异步操作完成，期间事件循环可以调度其他任务
    print(f"订单通知发送成功：{order.order_id}")  # 模拟通知发送完成


async def send_low_stock_notification(products: list[Product]) -> None:  # 定义异步低库存提醒函数
    if not products:  # 空列表在布尔判断中为 False
        print("\n当前没有低库存商品")  # 没有低库存商品时输出提示
        return  # return 结束函数执行
    await asyncio.sleep(0.1)  # 模拟调用外部告警服务的异步等待
    names = "、".join(product.name for product in products)  # join 将生成器表达式产生的商品名称连接成字符串
    print(f"\n低库存提醒：{names}")  # 输出低库存商品名称


# ============================================================  # 模块分隔：演示数据
# 九、准备模拟商品和优惠券  # 模拟从数据库读取商品和优惠券记录
# ============================================================  # 模块分隔：演示数据

PRODUCT_DATA = [  # 列表用于保存多条商品记录
    {"sku": "KB-001", "name": "机械键盘", "category": "电脑外设", "price": "199.00", "stock": 10},  # 商品记录一：机械键盘
    {"sku": "MS-002", "name": "无线鼠标", "category": "电脑外设", "price": "79.90", "stock": 5},  # 商品记录二：无线鼠标
    {"sku": "HD-003", "name": "移动硬盘", "category": "存储设备", "price": "259.00", "stock": 3},  # 商品记录三：移动硬盘，库存较低
    {"sku": "ST-004", "name": "笔记本支架", "category": "办公用品", "price": "89.00", "stock": 20},  # 商品记录四：笔记本支架
    {"sku": "CB-005", "name": "USB-C 数据线", "category": "电脑外设", "price": "29.90", "stock": 2},  # 商品记录五：数据线，库存较低
]  # 商品数据列表结束

COUPONS = [  # 创建优惠券对象列表
    Coupon("SAVE10", Decimal("0.10"), Decimal("200.00"), Decimal("30.00")),  # SAVE10：满 200 元打 9 折，最多优惠 30 元
    Coupon("SAVE20", Decimal("0.20"), Decimal("500.00"), Decimal("100.00")),  # SAVE20：满 500 元打 8 折，最多优惠 100 元
]  # 优惠券列表结束


# ============================================================  # 模块分隔：主流程
# 十、运行完整下单流程  # 将前面定义的模型和服务组合成一个完整业务案例
# ============================================================  # 模块分隔：主流程

async def main() -> None:  # 定义异步主函数，作为演示程序的业务入口
    products = [Product.from_record(record) for record in PRODUCT_DATA]  # 列表推导式将原始字典转换成 Product 对象列表
    service = OrderService(products, COUPONS)  # 创建订单服务，并传入商品和优惠券数据
    cart: Cart = {}  # 创建空购物车，类型注解说明它是 SKU 到数量的字典
    try:  # try 包裹下单流程，集中处理可能出现的业务异常
        service.add_to_cart(cart, "kb-001", 1)  # 加入一把机械键盘，演示 SKU 自动转大写
        service.add_to_cart(cart, "MS-002", 2)  # 加入两只无线鼠标
        order = service.checkout(customer="George", cart=cart, coupon_code="save10", payment_method=PaymentMethod.CARD)  # 使用关键字参数提交订单并使用优惠券
    except BusinessError as error:  # 捕获库存不足、优惠券不可用等业务异常
        print(f"\n订单创建失败：{error}")  # 输出业务失败原因
    except ValueError as error:  # 单独捕获参数校验或数据校验错误
        print(f"\n输入数据不合法：{error}")  # 输出数据校验错误
    else:  # try 中没有发生异常时执行 else 分支
        print("\n========== 订单创建成功 ==========")  # 输出订单成功提示
        print(order)  # 调用 Order.__str__，展示订单摘要
        for index, item in enumerate(order.items, start=1):  # 遍历订单明细并生成从 1 开始的序号
            print(f"{index}. {item.product_name} x {item.quantity} = ￥{item.line_total:.2f}")  # 输出商品名称、数量和明细金额
        print(f"商品金额：￥{order.subtotal:.2f}")  # 输出优惠前商品总金额
        print(f"优惠金额：￥{order.discount:.2f}")  # 输出优惠金额
        print(f"运费：￥{order.shipping:.2f}")  # 输出运费
        print(f"实付金额：￥{order.total:.2f}")  # 输出最终应付金额
        export_path = service.export_order(order)  # 将订单导出为 JSON 文件并接收导出路径
        print(f"\n订单文件：{export_path.resolve()}")  # resolve 获取文件的绝对路径
        await send_order_notification(order)  # 使用 await 等待订单通知发送完成
        low_stock = list(service.low_stock_products())  # list 消费生成器，将低库存商品转换为列表
        await send_low_stock_notification(low_stock)  # 异步发送低库存提醒
        service.print_inventory()  # 输出下单扣减库存后的库存报表
        print("\n========== 商品搜索 ==========")  # 输出商品搜索区域标题
        for product in service.search_products("电脑"):  # 遍历搜索到的商品
            print(f"{product.sku} | {product.name} | ￥{product.price:.2f}")  # 输出商品编码、名称和价格
        paid_orders = service.orders_by_status(OrderStatus.PAID)  # 查询所有已支付订单
        print(f"\n已支付订单数量：{len(paid_orders)}")  # len 获取订单列表的元素数量
    finally:  # finally 无论是否发生异常，通常都会执行
        print("\n========== 程序执行结束 ==========")  # 输出程序结束提示


if __name__ == "__main__":  # 只有直接运行本文件时，__name__ 才等于 "__main__"
    asyncio.run(main())  # asyncio.run 创建事件循环并运行异步主函数
