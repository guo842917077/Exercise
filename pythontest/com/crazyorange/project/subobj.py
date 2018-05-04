"""
如何为创建大量实例节省内存
通过累的__slots__属性节省内存开销
对象内部会有一个__dict__方法，它是实现动态绑定属性的 是占用内存的
使用__slots 来绑定属性，可以避免实现动态绑定属性 没有dict方法
"""

"""
如何让对象支持上下文管理 
with。。as
1.需要在类中自己定义——enter __exit
这两个方法会在with语句开始和with语句结束时 
"""


class People:
    ###通过slots声明函数，避免对象动态绑定参数
    __slots__ = ['name', 'age', 'level']

    def __init__(self, name, age, level):
        self.name = name
        self.age = age
        self.level = level

    def __enter__(self):
        print("开始介入的对象名称是 %s" % (self.name))
        return self

    ####exc_type：异常类型  异常值 异常栈
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("结束")

    def start(self):
        print("haha %s" % (self.name))


with People('guo', '13', 5) as p:
    p.start()

###检查p的属性
print(dir(p))

"""
如何创建和管理对象的属性
避免对象.property的方式进行赋值
除get，set方法外
可以使用对象内置的property方法
"""


class Circle:
    def __init__(self):
        self.__radius=0

    def setR(self, raw):
         self.__radius=raw
    def getR(self):
        return self.__radius
    """
    1.参数一表示获取r值时的方法
    2.参数二表示给R赋值时调用什么方法
    """
    R = property(getR,setR)

cir=Circle()
cir.R=10
print("%s"%(cir.R))

"""
如何使用描述符 对实例属性做类型检查
"""

class Descript:
   def __get__(self, instance, owner):
       pass
   def __set__(self, instance, value):
       pass


"""
管理
"""