# =====================================================================
# 06. 封装
# ---------------------------------------------------------------------
# 【思路】     把属性"藏"起来（用 _ / __ 命名），对外只暴露方法来读写
# 【传统写法】 手动定义 get_age / set_age 这类函数
# 【property】 用 @property 把方法变成"属性"，读写时不用写括号
#              @property       → get 方法（读）
#              @属性名.setter  → set 方法（写）
#              只写 @property   → 只读属性，赋值会报错
# =====================================================================


# ---------------------------------------------------------------------
# 一、定义类
# ---------------------------------------------------------------------
print("=" * 40)
print("一、定义类")
print("=" * 40)

class Person:
    """这是一个Person类"""

    home = "earth"                # 类属性，所有实例共享

    def __init__(self, name, age, gender):
        self.name = name          # 公共属性，相当于 Java 中的 public
        self._age = age           # 受保护属性，相当于 Java 中的 protected
        self.__gender = gender    # 私有属性，相当于 Java 中的 private

    # ------------------ 传统写法：手动定义 get / set ------------------
    def get_age(self):
        return self._age

    def set_age(self, age):
        self._age = age

    # ---------------- property 写法：把方法当属性来用 ----------------
    @property
    def gender(self):
        """get 方法：读取 p.gender 时自动调用"""
        print("获取__gender属性的get函数被调用了")
        return self.__gender

    @gender.setter
    def gender(self, gender):
        """set 方法：执行 p.gender = 值 时自动调用"""
        print("设置__gender属性的set函数被调用了")
        self.__gender = gender

    @property
    def email(self):
        """只读属性：只有 get 没有 setter，所以不能赋值"""
        return f"{self.name}@atguigu.cn"

    def __str__(self):
        """相当于 Java 中的 toString；内部用到了 self.gender，会触发 get"""
        return f"Person(name={self.name},age={self._age},gender={self.gender})"


# ---------------------------------------------------------------------
# 二、传统 get / set 方式读写受保护属性
# ---------------------------------------------------------------------
print("=" * 40)
print("二、传统 get / set")
print("=" * 40)

p = Person("王飞龙", 18, "女")
print(p.get_age())                # 输出：18
p.set_age(24)                     # 修改 _age
print(p)                          # 触发 __str__ → self.gender → 顺便打印 get 的提示语


# ---------------------------------------------------------------------
# 三、property 方式读写私有属性（像普通属性一样，不加括号）
# ---------------------------------------------------------------------
print("=" * 40)
print("三、property 读写")
print("=" * 40)

print(p.gender)                   # 触发 get
p.gender = "男"                   # 触发 set
print(p)                          # 输出：Person(name=王飞龙,age=24,gender=男)


# ---------------------------------------------------------------------
# 四、只读属性
# ---------------------------------------------------------------------
print("=" * 40)
print("四、只读属性")
print("=" * 40)

print(p.email)                    # 输出：王飞龙@atguigu.cn

# 只读属性不能赋值，放开注释会报错：
#   AttributeError: property 'email' of 'Person' object has no setter
# p.email = "wangfeilong@atguigu.cn"
