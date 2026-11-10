"""
    @Author:Irene
    @Time:2026/5/22
    @Desc:
"""
"""
    以单继承为例演示：
    （1）子父类如果属性重名了怎么办？
    （2）子父类的属性应该重名吗？
    
    1、类属性：
        非私有，_属性（约定式私有）：可以被子类直接使用，使用方式：类名.属性 或 类名._属性。出现重名不会覆盖。
        __属性（强制私有，名称改写式私有）：不可以被子类直接使用，如果非要使用，可以通过 父类名._父类名__属性。出现重名不会覆盖。
                子类的__属性，改写后的名称是  _子类名__属性
                父类的__属性，改写后的名称是  _父类名__属性
                
    但是，虽然不会覆盖，但是仍然不建议重名，会导致可读性大大降低。
        如果子父类的同名属性，逻辑意义相同，那么子类没必要重复定义。
        如果子父类的同名属性，逻辑意义不同，那么子类应该换一个名字，最好见名知意，通过名称能够区分最好。
        
    2、实例属性
        非私有，_属性（约定式私有）：可以被子类直接使用，使用方式：self.属性 或 self._属性。出现重名会覆盖。
        __属性（强制私有，名称改写式私有）：不可以被子类直接使用。不存在覆盖一说。
        
    3、结论：子父类的属性应该重名吗？不应该
        
"""
class Base:
    a = 1
    _b = 1
    __c = 1

    def __init__(self):
        self.x = 1
        self._y = 1
        self.__z = 1

class Sub(Base):
    a = 2
    _b = 2
    __c = 2

    def __init__(self):
        self.x = 2
        self._y = 2
        self.__z = 2

    def show(self):
        # print("Sub.a=", Sub.a)
        # print("Base.a=", Base.a)
        #
        # print("Sub._b=", Sub._b)
        # print("Base._b=", Base._b)
        #
        # print("Sub.__c=", Sub.__c)
        # # print("Base.__c=", Base.__c) #错误
        # print("Base.__c=", Base._Base__c) #访问改写后的名称

        print("Sub类中定义的self.x = ", self.x)
        # print("Base类中定义的self.x = ", super().x)  #错误
        # print("Base类中定义的self.x = ", super.x)  #错误
        # print("Base类中定义的self.x = ", super(Base,self).x)  #错误

        print("Sub类中定义的self._y = ", self._y)
        # print("Base类中定义的self._y = ", self._y)#覆盖了

        print("Sub类中定义的self.__z = ", self.__z)
        # print("Base类中定义的self.__z = ", self._Base__z)#错误

s = Sub()
s.show()






