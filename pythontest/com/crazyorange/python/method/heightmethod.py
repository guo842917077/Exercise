"""
高阶函数的调用
1。python中变量可以指向函数
2。可以用变量代替函数 x=abs   a=x(10)
3.python中函数名就是一个代表函数的变量
4。函数可以接收函数名变量
"""
from _functools import reduce


def andMethod(a, b, function):
    return function(a) + function(b)


##注意这里不能传入abs() 要传入函数名 代表这个函数
print(andMethod(1, -5, abs))

"""
map函数 将方法作用在集合中的每一个元素中 map接收两个参数 map（f（x）,iterator）
"""
r = list(map(str, [1, 2, 3, 4, 5, 6]))
print(r)


def xx(a):
    return a * a


print(list(map(xx, [1, 2, 3, 4, 5, 6])))

"""
reduce 和map类似 传入两个值的方法和数组  函数执行的结果和数组中下一个元素继续执行 传入的方法 直到
元素全部被取出
"""


def sum1(a, b):
    return a * 10 + b


print(reduce(sum1, [1, 3, 5, 7, 9, 10]))

"""
filter 根据函数条件过滤出满足条件的集合
"""
def testfilter(a):
    return a % 2 == 0
print(list(filter(testfilter,[1,3,5,7,9,10,12,16])))