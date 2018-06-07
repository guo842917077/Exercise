"""
1。pop 根据位置来删除，并且返回删除元素
2。remove 根据值删除
3。append 在队尾插入元素
4。insert 在指定位置插入元素
5.使用sort来对列表进行永久性修改的排序
"""
names=['guo','yang','duan']
print(len(names))
print(names[0].title())
#插到队尾
names.append('haha')
print(names[-1])
#插入指定位置
names.insert(0,'xing')
print(names[0])
#删除指定的元素
del names[0]
print(names[0])
#删除指定元素，并返回删除的对象，在不指定位置的情况下删除队尾元素
first_name=names.pop(0)
print(first_name)

#remove根据值来删除
names.remove('yang')


country=['America','Britain','Italy','Australia']
#reverse方法返回值为None，直接调用reverse方法将对country进行永久性的反序排列
country.reverse()
print(country)
for c in sorted(country):
    print(c)



d=[a for a in range(1,20)]
print(d[0:3])