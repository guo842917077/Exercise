"""
python中  使用def定义一个方法
def 方法名（）：

1。方法可以使用默认参数 在必选参数一定要在最前面，使用param=value的形式设置默认值
2。默认参数一定要指向不变的对象  不能指向数组
3。可变参数在参数前加上*号 这些参数在函数中被组装成一个元组
4。关键词参数 在参数前加入两个**号：可以传入多个字典元素，这些字典在函数中组成一个字典
5. 命名关键词参数 由于不指定关键词的命名，有可能没有传入含有需要的key的字典 而造成在获取值时发生异常
可以指定 传入的字典必须含有的key来避免这个错误 ----命名关键词。通过（a，b，*，city，job）来分割，如果中间有可变参数
那么就不想要用*号分割了，并且在调用的时候需要带上参数名，针对例子，调用方式时（1，2，city="beijing"，job="hah"）
输出是1，2，{'city':'beijing'}
"""
# t1 = input("please input a number to t1")
# t2 = input("please input a number to t2")

def whichMax(a, b):
    if not isinstance(a, (int, float)):
        TypeError('bad params')
    if a < b:
        return b
    else:
        return a
# print("which one is max number %s" % (whichMax(t1, t2)))


def defaultParams(a, b=3):
    print("haha print b %s" % (b))


defaultParams(3)


def changeMethod(*numbers):
    sum = 2
    for x in numbers:
        print("n=%s" % (sum * x))

changeMethod(1, 2, 3, 4, 5)
#关键词参数方法
def defaultDicMethod(a,**city):
    if "city" in city:
        print(city)
'''
city会作为字典的key
'''
defaultDicMethod(1,city="guo")

#  a : 1 b:2 ('guo', 'wang', 'yang') guo android
def defaultMethodAllParams(a,b,*numbers,city,job):
    print("a : %s"%(a),"b:%s"%(b),numbers,city,job)

defaultMethodAllParams(1,2,"guo","wang","yang",city="guo",job="android")