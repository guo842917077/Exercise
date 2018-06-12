import impmodule as second
"""
learn method
1。指定参数赋值，可以忽略参数的顺序
2。参数默认值，
"""
def descirbe(arg,arg2="default"):
    print("arg : "+str(arg)+" arg2 : "+str(arg2))

def prt(args):
    if isinstance(args,(list)):
        for t in args:
            print(t)

#使用参数列表时，参数列表一定要放到最后
def pizz(name,*size):
    print("pizz name is : "+name)
    print("size is : "+size[0]+" y : "+size[1])

#直接调用方法传入参数
descirbe(1,2)
#指定参数赋值
descirbe(arg2=3,arg=4)
#指定参数默认值,如果参数指定了默认值，那么可以在调用的时候不必传入
descirbe(3)
names=['guo','li','zhao']
#为了避免直接操作集合 可以传入集合的副本,使用切片创建一个副本
prt(names[:])
pizz('bige','50','60')


second.importmodule()