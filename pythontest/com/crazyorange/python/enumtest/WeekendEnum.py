from enum import Enum, unique

"""
定义枚举的方式
1。使用Enum方法
2。使用class继承Enum  int类型的值不能重复  并且用unique进行重复排查
"""
Month = Enum('Month', ('Jan', 'Feb', 'Mar'))
print(Month['Jan'])


@unique
class Month(Enum):
    Jan=1
    Feb=2
    Mar=3

print(Month.Feb)
