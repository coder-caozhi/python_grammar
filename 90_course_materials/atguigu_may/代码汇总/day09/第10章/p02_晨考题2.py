"""
    @Author:Irene
    @Time:2026/5/23
    @Desc:
"""
"""
背景：RPG游戏中角色有多种能力来源。
要求：
1. 创建三个基类：
   - 战士Fighter：包含属性__strength力量值、提供attack()方法输出“物理攻击”
   - 法师Mage：包含属性__intelligence智力值、提供cast_spell()方法输出“火球术”
   - 医师Healer：包含__wisdom智慧值、提供heal()方法输出“治疗术”。
   - 每个类都有get_power()方法返回不同数值（战士返回力量值，法师返回智力值等）。
2. 创建子类Paladin（圣骑士）同时继承Fighter和Healer，重写get_power()为(力量×0.6 + 智慧×0.4)。
    并拥有自己的holy_light()技能（输出“圣光普照”）。
3. 创建子类Spellblade（魔剑士）同时继承Fighter和Mage，重写get_power()为(力量×0.5 + 智力×0.5)，
    重写attack()为先施放一个附加魔法效果再物理攻击（调用两个父类对应方法）。
4. 多态：定义一个函数show_power(character)，调用其get_power()。演示不同角色传入时得到不同计算方式。
5. 封装：每个角色的力量/智力等属性设为私有，通过getter访问。
"""
class Fighter:
    def __init__(self, strength):
        self.__strength = strength

    def attack(self):
        print("物理攻击")

    def get_power(self):
        return self.__strength

    @property
    def strength(self):
        return self.__strength

class Mage:
    def __init__(self, intelligence):
        self.__intelligence = intelligence

    def cast_spell(self):
        print("火球术")

    def get_power(self):
        return self.__intelligence

    @property
    def intelligence(self):
        return self.__intelligence

class Healer:
    def __init__(self, wisdom):
        self.__wisdom = wisdom

    def heal(self):
        print("治疗术")

    def get_power(self):
        return self.__wisdom

    @property
    def wisdom(self):
        return self.__wisdom

class Paladin(Fighter,Healer):
    def __init__(self,strength,wisdom):
        #写法一：错误，两个都是调用Fighter的__init__
        # super().__init__(strength)
        # super().__init__(wisdom)
        #写法二：
        # Fighter.__init__(self, strength)
        # Healer.__init__(self, wisdom)

        #写法三：
        super().__init__(strength)
        super(Fighter,self).__init__(wisdom)

        #写法四：每一个__init__都需要加可变参数（略，参考mro初始化演示）

    def get_power(self):
        return self.strength * 0.6 + self.wisdom *0.4

    def holy_light(self):
        print("圣光普照")

class Spellblade(Fighter,Mage):
    def __init__(self, strength, intelligence):
        Fighter.__init__(self, strength)
        Mage.__init__(self, intelligence)

    def get_power(self):
        return self.strength * 0.5 + self.intelligence *0.5

    def attack(self):
        super().cast_spell() #或self.cast_spell()
        super().attack() #这里不可以写self.attack()否则会造成无限递归

def show_power(character):
    print("能力：", character.get_power())

p1 = Paladin(100,200)
s1 = Spellblade(100,200)
show_power(p1 )
show_power(s1 )
p1.holy_light()
p1.attack()

s1.attack()
s1.cast_spell()