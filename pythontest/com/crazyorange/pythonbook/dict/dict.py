"""
字典练习
"""
favorite_name = {
    'first_name': 'guojinlong',
    'last_name': '郭景然'
    , 'age': '25'
    ,'pinyin':'guojinlong'
}
print('first name is : '+favorite_name['first_name'])
#删除字典中的key
del favorite_name['last_name']
print(favorite_name)
#给字典添加值
favorite_name['last_name']='郭金龙'
#遍历字典
for key,value in favorite_name.items():
    print(key+" : "+value)
    #遍历key
for key in favorite_name.keys():
    print(key)
#遍历值 set方法去除集合中重复的元素
for value in set(favorite_name.values()):
    print(value)

#字典数组
aliens=[]
for num in range(20):
    alien={'name':'alien','num':num}
    aliens.append(alien)
print(aliens[0:5])
#字典中存储数组
alien={
    'name':'yoyo'
    ,'point':[200,300]
}
print('x : '+str(alien['point'][0])+' y : '+str(alien['point'][1]))


#在复制tp的基础上添加c：4的键值对
tp={"a":1,"b":2}
copy2=dict(tp,c=4)
print(copy2)

from collections import OrderedDict
orderD=OrderedDict()
orderD['a']=0
orderD['g']=1
print(orderD)