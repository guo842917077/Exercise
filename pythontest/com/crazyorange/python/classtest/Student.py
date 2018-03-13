"""
1。python中分为实例属性和类属性。实例属性是通过变量.属性 或者self来做的。
2。同样可以使用类的对象.属性 来进行声明
3。初始化一个对象使用类名（） 参数
4。私有属性的声明 __属性名称
5.继承一个类 要在类的后面括号中加入该类
6.python的多台不同于其它的静态语音的多态。它不是很松的多态。一个方法要求传入
7.自定义类作为参数 需要类型需要小写
8.判断对象的类型isinstance(obj，Type)是否是指定的类型
9.查看对象的类型dir，type
10.类属性 直接在类里面声明
"""


class Student(object):
    '类属性'
    className = "7"
    grade = 10
    "实例属性"
    def __init__(self, name1, score2):
        self.name = name1
        self.score = score2
        self.__address = ""

    def run(self):
        print("student is run : ")


class Animal(object):
    def run(self):
        print("animal is running")


class Duck(Animal):
    def run(self):
        print("duck is running")


def test():
    student = Student("111", 20)
    student.name = "guo"
    student.age = 24
    student.score = 100;
    print(student.score, student.name, student.age)


"""
python的多态是轻松的，只要传入的对象含有指定的方法就可以
即：只要你有指定类型的特性，就认为你是该类型
"""


def duotai(animal):
    animal.run()


test()
duotai(Student("wang", 80))
duotai(Duck())
"""
dir方法 打印对象所有的属性
"""
print(dir(Duck()))
