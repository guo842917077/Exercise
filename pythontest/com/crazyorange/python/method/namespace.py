"""
gloabls:表示是全局文件的引用关系
locals表示局域内对象的引用关系
所以可以通过使用globals来声明全局对象
"""

"""
globals : {'b': 20, 'a': 10}
local : {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x1056fd2e8>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': '/Users/apple/Desktop/Exercise/Exercise/pythontest/com/crazyorange/python/method/namespace.py',
 '__cached__': None, 'c': 100, 'see': <function see at 0x105686ea0>}
"""

c=100
def see():
    a=10
    b=20
    globals()['name']='guo'
    print("globals : "+str(globals()))
    print("local : "+str(locals()))

# print(locals())
# print(globals())

see()
##可以正常输出guo，但对象的声明是通过globals在方法区域内声明的，但编译器无法访问到
print(name)