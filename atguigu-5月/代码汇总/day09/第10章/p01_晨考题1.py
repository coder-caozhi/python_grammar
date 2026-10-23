"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
背景：实现不同车型的租赁费用计算。
要求：
1. 父类Vehicle包含私有属性_base_rate（日基础租金）和_rent_days（租的天数）。方法calculate_cost()返回基础租金×天数。
2. 子类：
   - Car：额外收取每天50元保险费，重写calculate_cost()。
   - Truck：基础租金×天数 + 每公里5元（公里数作为额外参数传入），因此重写calculate_cost(km)。
3. 封装：_base_rate只能通过构造函数设置，不能直接修改。提供set_rent_days()方法修改租车的天数。
4. 创建Car和Truck对象测试
"""
class Vehicle:
    def __init__(self, base_rate, rent_days):
        self._base_rate = base_rate
        self._rent_days = rent_days

    def calculate_cost(self):
        return self._base_rate * self._rent_days

    # def get_rent_days(self):
    #     return self._rent_days

    # def set_rent_days(self, rent_days):
    #     self._rent_days = rent_days

    @property
    def rent_days(self):
        return self._rent_days

    @rent_days.setter
    def rent_days(self, rent_days):
        self._rent_days = rent_days

class Car(Vehicle):
    def calculate_cost(self):
        # return super().calculate_cost() + 50 * self._rent_days #对
        # return super().calculate_cost() + 50 * self.get_rent_days() #对
        return super().calculate_cost() + 50 * self.rent_days #对

class Truck(Vehicle):
    def calculate_cost(self,km):
        return super().calculate_cost() + 5 * km

#测试
car = Car(50,3)
print("car的租金：",car.calculate_cost())

truck = Truck(100,5)
print("truck的租金：",truck.calculate_cost(500))
