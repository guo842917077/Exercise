####统计元素出现的频次
from random import randint
data=[randint(0,20) for x in range(30)]
print(data)
####生成字典 data--key  0--defaultValue
# dict_data=dict.fromkeys(data,0)
# for x in dict_data:
#     dict_data[x]+=1
# print(dict_data)
###使用counter对象 查询出现频次最多的元素
from collections import Counter
c2=Counter(data)
print(c2.most_common(3))

####对词频做统计
import  re
###使用正则表达式对此条进行分割
txt=re.split('\W+',"word name function word")
####使用counter对txt进行记数
c3=Counter(txt)
####打印出现频率最高的1个词
print(c3.most_common(1))
