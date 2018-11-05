"""
python中类是多继承的
字段分为：
1.类变量：直接在类中声明或通过类名.字段的方式
2.实例字段：在构造方法中声明或者通过实例.字段的方式声明
3.使用单下滑线声明私有变量
"""


class Animals():

    def __init__(self, name):
        self.name = name


class Dog(Animals):
    __a = 3

    def __init__(self, name):
        super().__init__(name)
        self.name = name
        self.type = DogType()

    # 声明属性只读
    @property
    def getType(self):
        return self.type.getTypeName()

    def setName(self, name):
        self.name = name
    #静态方法
    @staticmethod
    def name():
       return "dog"

class DogType():
    def __init__(self):
        self.type = 'dog'
        print('dogtype : ' + self.type)

    def getTypeName(self):
        return self.type
