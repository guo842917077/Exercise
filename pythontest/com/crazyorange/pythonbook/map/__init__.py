"""
1.map操作符
将数据依次执行表达式
"""
data=list(map(lambda x,y:x+y,"ABC","234"))
for x in data:
    print(x)

"""
zip 平行从多个数据源接收参数，聚合成元组
"""

x=zip([1,2,3],"ABC")
##使用dict方法变成字典
print(dict(x))