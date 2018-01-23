"""
列表生成器：生成对象的模式  for 对象 in 范围
翻译成语言就是：生成一个列表 其中的x元素 从 范围R 中获得
"""
##生成a+b 类型的组合，a从xyz中获得 b从 abc中获得
listA = [a + b for a in "xyz" for b in "abc"]
print(listA)

##生成list
listB = [a * a for a in list(range(3))]
print(listB)

"""
不同于列表生成器，生成器保存的是算法，用（）将生成器的语句包含起来，而不是用[]
listC打印的结果是  <generator object <genexpr> at 0x104027938>
要想打印生成器，需要使用next方法 得出算法的结果 yudao 
遇到next方法的时候执行该执行器方法
"""
listC = (a * b for a in range(10) for b in range(10))
print(listC)
print(next(listC))

"""
第二种生成执行器方式是在一个程序中加入yield，一个函数中有yield，它就是一个执行器（保存一个算法）
执行程序时，入到yeild 返回，下次再执行时，执行上一次yield返回处后面的代码。
"""


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'



