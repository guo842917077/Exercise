"""
dict 字典：相当于java的map  使用{}表示
set：通过传入一组存储的集合，存储一组key，并且key不能重复 使用set方法生成一个集合
"""

maps={1:'haha',2:'heihei',3:'yoyo'}
print("key 1 value : "+maps.get(1))
maps.pop(2)
if 2 in maps:
    print("maps key 2 value "+maps.get(2))
else:
    print("maps has no key 2 ")


keys=[1,2,3,4,5]
sets=set(keys)
sets.add(6)
for x in sets:
    print("sets value : %s"%(x))