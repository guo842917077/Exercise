"""
python 中的迭代可以迭代list，dict ，tuple
如果需要向java一样迭代 需要enumerate
"""
###判断一个对象是否可以迭代
#from collections import Iterable
#print(isinstance('abc',Iterable))
#迭代整个循环

listA = list(range(20))
for x in listA:
    print(x)
###迭代字典的key和value
dic = {1: "hha", 2: "hehe"}
for key in dic:
    print(key)
for value in dic.values():
    print(value)
###判断一个对象是否可以迭代
from collections import Iterable
print(isinstance("sss",Iterable))
###迭代索引和数据
for i,value in enumerate(listA):
    print(i,value)