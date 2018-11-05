import array
import bisect
"""
数组的注意点
"""
#列表 []
"""
列表紧存储指针所以列表可以存储不同的类型
"""
a=[1,'ss',[1,2,3]]

class Users:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    #类似java的toString
    def __repr__(self):
        return f"{self.name},{self.age}"
# 列表排序使用sort，sorted方法
users=[Users(f"user{i}",i) for i in (13,11,15,14)]
copy=users.sort(key=lambda u:u.age)
print(copy)
#向有序数组插入元素 使用2分法插入元素 效率更高

c=[1,2,3,4]
bisect.insort_left(c,0)
print(c)

"""
数组，动态扩展，单一类型
"""

ss=array.array('b',[1,2,3])
ss.append(5)

