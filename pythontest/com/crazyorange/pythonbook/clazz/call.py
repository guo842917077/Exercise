"""
python中的类 重写call方法后，该类的实例可以像方法一样调用
"""
class CallTest:
    def __init__(self):
        pass
    def __call__(self, s):
        print(s)

#创建CallTest的实例cal
cal=CallTest()
#像函数一样调用cal，实际触发的是call方法
cal('abc')