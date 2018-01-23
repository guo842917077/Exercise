import functools

"""
1。定义一个装饰器，类似于java的方法的切面
2。使用便函数：将方法的某些参数固定 ，生成一个新的函数
"""

# 1。定义一个装饰方法
def addLog(text):
    # 2.定义一个装饰方法表示要装饰的方法，并且将该方法签名成要被装饰的方法
    def decorate(fun):
        print("decorate ")
        @functools.wraps(fun)
        ##3。定义实际要追加内容方法
        def wrapper(*args, **kwargs):
            #这里表示在追加代码前执行
            fun(*args,**kwargs)
            # 5.追加代码
            print("add something %s"%(text))
            ###4。执行原方法：原方是传递进来的 这里表示在追加代码之后执行
            #return fun(*args,**kwargs)
        return wrapper
    return decorate

@addLog("ttt")
def test():
    print("test execute ")
test()

int2 = functools.partial(int, base=10)
print(int2('10000'))
