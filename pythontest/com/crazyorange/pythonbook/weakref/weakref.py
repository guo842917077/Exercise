"""
弱引用练习，弱引用不会增加引用的技术
"""
import weakref
import sys

def a():
    pass
fount=a()
b=a
count=sys.getrefcount(fount)
weakA=weakref.ref(a)
count=sys.getrefcount(a)

print("strong ref of a : "+str(count))
print("ref of a : "+str(count))
