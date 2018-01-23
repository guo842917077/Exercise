"""
python 支持函数返回一个函数。当一个函数作为一个保存功能的 以及参数的的地方。
"""


def layzeMethod(*a):
    def sum():
        ax = 0
        for x in a:
            ax=ax+x
        return ax
    return sum
##1。调用保存参数和方法的执行结果
f1=layzeMethod(1,3,5,7,9,10)
##2.在需要的地方执行保存起来的方法f1
print(f1())