"""
python中的异常处理：
try：检测代码段
except ：捕获异常后如何处理
else ：没有发生异常走的代码
finally：不管如何都会走的代码
"""
def test():
    try:
        raise Exception('test exception')
    except:
        print("i get a exception")
    else :
        print("have no exception")
    finally:
        print("always get there")

test()
