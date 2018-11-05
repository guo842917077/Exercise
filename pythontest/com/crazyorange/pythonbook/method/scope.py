"""
作用域
1。global 声明调用全局变量
2。nonlocal 声明引用嵌套的变量
global 是默认调用的
内部方法inner使用了nonlocal关键词 表示引用的是inner方法内部声明的a
和外部的a是区分开的
"""

"""
output :
 test global
 inner a
 out a
"""
str='test global'
a='out a'
def test():
    #声明引用全局的str变量
    a='inner a'
    global str
    print(str)

    def inner():
        nonlocal a
        print(a)

    inner()




test()
print(a)