from multiprocessing import Process, Pool
import os, time, random

"""
引入跨平台进程 multipleprocessing 库
引入操作系统 os库
"""

###打印当前进程号
print("current process name is : %s" % (os.getpid()))


####创建一个进程对象，以及指定进程要执行的方法
def test(name):
    print("execute test method in process " + name)


def test2(name):
    print("execte test2 method in process pool " + name)


"""
创建一个进程  使用Process 
@:param target  进程中要执行的方法
@:param args  方法中需要传递的参数
start方法 启动
join 等待子进程结束后 再继续运行
"""
process = Process(target=test, args=('guo',))
process.start()

"""
使用进程池Pool 创建进程和管理任务
"""
p = Pool()
p.apply_async(test2, args=('guo',))
###必须要先close再join
p.close()
p.join()
