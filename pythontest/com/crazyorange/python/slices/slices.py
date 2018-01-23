"""
python 切片功能  类似java中的substring，但在python中数组，元组和字符串都可以用切片来表示
obj[ t1：t2：a] t1:起始边界 t2 停止边界   a：每隔多少取一个
"""
listA=list(range(99))
str="my name is guo"
#获取前10个数字
print(listA[0:10])
#获取后10个数字
print(listA[-10:])
#获取中间的某段数字
print(listA[10:20])
#跳跃性的获取
print(listA[10:40:5])
#str类型的截取
print(str[3:5])