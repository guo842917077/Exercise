"""
抽象类的实现
1.引入ABCMeta，abstractmethod 或者继承ABC类
2.方法使用abstractmethod注解
"""
from abc import ABCMeta,abstractmethod
class AbsClass(metaclass=ABCMeta):
    def __init__(self,name):
        self.name=name

    @abstractmethod
    def getName(self):
        ...
"""
如果不实现getName方法 会报错
Can't instantiate abstract class ImpClass with abstract methods getName
"""
class ImpClass(AbsClass):
    def __init__(self,name):
        super().__init__(name)

    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name


cc=ImpClass("guo")

print(cc)