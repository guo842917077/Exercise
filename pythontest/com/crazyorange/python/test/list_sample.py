# python 表示list 用[]符号，使用append 表示添加元素  pop表示删除元素  -1表示最后一个元素

names = ['guo', 'wang', 'xing', 'duan']
print('first name is : ' + names[0])
names.append("yang")
print('last name is ' + names[-1])
names.pop(2)
print('second name is ' + names[2] + " length of names %s" % (len(names)))

###使用()表示元组 python中一个不可以修改的集合
tupleNames = ('guo', 'wang', 'xing', 'duan')
#查看全局 命名和引用的映射关系
"""
{... 'names': ['guo', 'wang', 'duan', 'yang'], 'tupleNames': ('guo', 'wang','xing', 'duan')}
"""
print(locals())