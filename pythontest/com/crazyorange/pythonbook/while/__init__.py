"""
while 集合遍历数组和字典
"""
names=['guo','yang','li']
#遍历集合，之道集合为空
t=0
while 'yang' in names:
     names.remove('yang')
while names:
    print(names.pop().title())

