"""
    @Author:Irene
    @Time:2026/5/20
    @Desc:
"""
"""
1. 创建一个Goods商品类，包含实例属性：商品名称title和价格price
2. 创建一个ShoppingCart类，包含以下内容：
   - 类属性：store_name（商店名称）、total_carts（创建的购物车总数）
   - 实例属性：owner（拥有者）、items（商品列表，初始为空）、total_price（总价，初始为0）
3. 定义实例方法：
   - add_item(self,item_name, price)：添加商品Goods对象到购物车（更新items列表和total_price）
   - remove_item(self,item_name)：从购物车中移除指定商品Goods对象（更新items列表和total_price）
   - show_cart(self)：显示购物车中的所有商品和总价
4. 定义类方法：
   - set_store_name(cls, new_name)：修改商店名称
   - show_total_carts(cls)：显示创建的购物车总数
5. 定义静态方法：
   - calculate_discount(price, discount_rate)：计算折扣后的价格
6. 创建2个购物车对象（不同拥有者），并测试：
   - 分别添加3-4件物品
   - 从一个购物车中移除一件物品
   - 显示两个购物车的内容
   - 修改商店名称并验证
   - 使用静态方法计算某个物品的折扣价

"""
import functools
class Goods:
    def __init__(self,title,price):
        self.title = title
        self.price = price

    def __repr__(self):
        return f"商品名称：{self.title}，价格：{self.price}"

class ShoppingCart:
    store_name = None
    total_carts = 0

    """
    写法一：
        def __init__(self,owner,items=[]):
            ....
        python解释器加载p08_练习题.py文件时，从上往下检查代码。加载ShoppingCart类时，会对类进行初始化，
        因为类的信息也要从硬盘加载到内存。虽然__init__还未执行，但是类初始化需要先解析__init__形参列表进行解析。
        此时会对items=[]进行初始化，那么类的初始化只为进行一次。 
        所有__init__的形参items都被初始化为同一个[]。
        当我们创建ShoppingCart对象时，没有为它指定新的items对象时，就会导致大家共用同一个列表。
    """
    # def __init__(self,owner,items=[]):
    #     self.owner = owner
    #     self.items = items
    #     # self.total_price = 0 if not items else 累加items中所有商品的价格
    #     self.total_price = 0 if not items else functools.reduce(lambda g : g.price,items,0)
    #     ShoppingCart.total_carts+=1

    """
    写法二：
    """
    def __init__(self,owner,items=None):
        self.owner = owner
        self.items = [] if not items else items #这个语句只有在__init__方法被调用时才执行，每一个[]都是独立
        # self.total_price = 0 if not items else 累加items中所有商品的价格
        self.total_price = 0 if not items else functools.reduce(lambda g1,g2 : g1 + g2.price,items,0)
        ShoppingCart.total_carts+=1

    def add_item(self,item_name,price):
        # g = Goods(item_name,price)
        # self.items.append(g)
        self.items.append(Goods(item_name,price))
        self.total_price += price

    def remove_item(self,item_name):
        #怎么根据item_name商品名称从items中删除商品对象
        # self.items.remove(item_name) #错误
        for item in self.items:
            if item.title == item_name:
                self.total_price -= item.price
                self.items.remove(item)
                break

    def show_cart(self):
        return f"所有者：{self.owner}，所有的商品：{self.items}，总价格：{self.total_price}"

    @classmethod
    def set_store_name(cls,new_name):
        cls.store_name = new_name

    @classmethod
    def show_total_carts(cls):
        return cls.total_carts

    @staticmethod
    def calculate_discount(price,discount_rate):
        return price * discount_rate

#测试代码
c1 = ShoppingCart("柴林燕")
c2 = ShoppingCart("孙艺萌")

items = [Goods("手机",5000)]
c3 = ShoppingCart("大海", items)

c1.add_item("鼠标",99.9)
c1.add_item("键盘",199.9)
c2.add_item("牛奶",69.9)
c2.add_item("苹果",169.9)

print(c1.show_cart())
print(c2.show_cart())
print(c3.show_cart())

c1.remove_item("鼠标")
print(c1.show_cart())

print("之前的商品名称：",ShoppingCart.store_name)
ShoppingCart.set_store_name("谷粒商城")
print("之后的商品名称：",ShoppingCart.store_name)

print(ShoppingCart.calculate_discount(10000, 0.8))


