####可迭代对象，迭代器对象
####由可迭代对象可以得到迭代器对象 iter('str')
####对象自身带 __iter或者是一个序列
"""
1。实现一个迭代器对象  next 方法返回下一个对象
2.实现一个可迭代对象  _iter

一个可迭代对象的内部是有一个iter方法的，iter返回一个迭代器，一个迭代器内需要有一个next方法 返回数据
"""
from collections import Iterable, Iterator


def getWeather():
    return ['sunny', 'rain']


###迭代器对象 具有next方法 继承iterator
class WeatherIterator(Iterator):
    def __init__(self, cities):
        self.cities = cities
        self.index = 0

    def __next__(self):
        if self.index == len(self.cities):
            raise StopIteration
        city = self.cities[self.index]
        self.index += 1
        return city


"""
可迭代对象
"""
class WeatherIterable(Iterable):
    def __init__(self, cities):
        self.cities = cities

    def __iter__(self):
        return WeatherIterator(self.cities)


weathers = WeatherIterable(getWeather())
for w in weathers:
    print(w)

"""
使用生成器函数实现可迭代对象
包含yeild的函数 就是可迭代函数,yield 会保存程序运行的状态，下一次运行从上一次保存的位置开始
"""

def nextFunction():
    print(1)
    yield
    print(2)
    yield
    print(3)
    yield

for n in nextFunction():
    n
