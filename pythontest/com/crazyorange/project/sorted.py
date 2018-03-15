####对字典进行排序
from random import randint

dict_data = {x: randint(60, 100) for x in 'xyzabc'}
a=sorted(dict_data)
print(a)

####使用元组进行排序
###元组比较，先比较第一个元素（97，a）>(50,b)
####1.使用zip函数将字典转换成元组 将两个数组中的元素合并成元组
p=zip(dict_data.values(),dict_data.keys())
print(sorted(p))


####直接使用sorted的key参数定义使用哪一个部分进行排序
####这里key=lambda x：x[1] 表示 x 使用 字典中index为1的地方 ，表示使用值进行排序
print(sorted(dict_data.items(),key=lambda x:x[1]))



####如何快速查找多个字典中的公共键
####sample取样
from random import randint,sample
####每次从集合中 寻出3到6个数
#name=sample('abcdefg',randint(3,6))

s1={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s2={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
s3={x:randint(1,4) for x in sample('abcdefg',randint(3,6))}
####1.使用map函数 对传入集合中的每一个元素执行 Function所对应的方法
###这里是对字典S1,S2执行取key的操作 并得出新的集合
iter=map(dict.keys,[s1,s2,s3])
####使用reduce使集合中的两个元素执行funtion,得出的结果与下一个元素再次执行function
###对集合中的所有元素执行与操作 直到没有相同的
from functools import reduce
print(reduce(lambda x,y:x&y,iter))


"""
让字典保持有序的
"""
###使用有序的字典，该字典可以让集合中的元素，按照进入的顺序打印
from collections import OrderedDict
d=OrderedDict();
d['p']=5
d['a']=6
d['s']=10
for t in d.keys():
   print(t)