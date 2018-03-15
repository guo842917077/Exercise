"""
过滤集合中的数据进行筛选
"""
from random import randint

##列表生成器 从-10到10之间生成10个随机数
####randint 生成值的范围  range索引的范围
###randint表示的是值生成的范围  range（10）是索引的个数
data = [randint(-10, 10) for x in range(10)]
###使用filter过滤函数进行筛选
result = filter(lambda x: x < 0, data)
for a in result:
    print(a)

###列表解析
###查找x元素  x 元素从data列表中迭代  条件是 取出的元素小于0
result2 = [x for x in data if x < 0]
for a in result2:
    print(a)

#####字典解析
###字典生成式 v=randint(60,100) x=range(1,21)
d = {x: randint(60, 100) for x in range(1, 21)}
data={k: v for k, v in d.items() if v > 60}
print("%s" % (data))

# p={x:randint(-10,60) for x in range(10)}
# print(p)

# p = [randint(10, 20) for x in range(10)]
# print(p)


####集合生成器
s=set(data)
result3={r for r in s if r%2==0}
print(result3)


