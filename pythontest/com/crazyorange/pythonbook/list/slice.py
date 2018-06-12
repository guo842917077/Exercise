"""
切片 和range一样
从起始位置开始 到 结束位置-1 停止
"""
a=list(range(0,20))
print(a[0:4])
#不指定开头 将从头开始
print(a[:4])
#不指定结尾 将默认遍历到结尾
print(a[0:])
#倒序输出 ，输出最后3个数据
print(a[-3:])
#省略后三个数据
print(a[:-3])
#复制整个列表
b=a[:]
print(b)
#生成一个字符串列表
str='The first three items in the list are:'.split(' ')
print(str[0:3])
print(str[-3:])