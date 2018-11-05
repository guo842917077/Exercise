"""
在python中使用装饰器注释@包装方法名 可以对一个方法进行包装
@+装饰方法名 用在另一个方法上：表示另一个方法将被装饰方法包裹。

同样可以使类作为装饰器，只要类实现了call方法，并且传入原方法，并且在call方法中调用了原方法
就可以实现装饰，因为实现call方法可以让类像方法一样调用

2。装饰器注解同样可以传参数，相当于在装饰器外层加入一层接收参数
"""
def log(fun):
    def wrapper(*args,**kwargs):
        print("print logs")
        return fun(*args,**kwargs)
    return wrapper

@log
def test(str):
    print(str)


# test("gggg")


class TT:
    def __init__(self,fn):
        self.fn=fn
    #实现call方法可以让类像方法一样调用
    def __call__(self, *args, **kwargs):
       print("class callable")
       return self.fn(*args,**kwargs)
@TT
def tt():
    print("decorate in TT")

# tt()

##在decorator外层嵌套了ccc方法用来接收注解参数
def ccc(name='default'):
    print("args : "+name)
    def decorator(fn):
        def wrapper(*args,**kwargs):
            print("ccc decorator")
            return fn(*args,**kwargs)
        return wrapper
    return decorator
@ccc("ccTest")
def ccTest():
    print("cc callacble")

ccTest()