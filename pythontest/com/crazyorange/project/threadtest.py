from threading import Thread
from queue import Queue
import threading
"""
创建线程的方式 直接使用thread和继承thread
"""


def CallName():
    print("haha")


class MyThread(Thread):
    def __init__(self, method):
        Thread.__init__(self)
        self.method = method

    def run(self):
        self.method


t = MyThread(CallName())
t.start()

t2 = Thread(target=CallName, args=())
t2.start()
"""
使用Queue来进行线程间通信
"""


class Thread2(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        self.queue.put(1)
class Thread3(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
      data=  self.queue.get(1)
      print(data)

queue=Queue()
t2=Thread2(queue)
t2.start()
t3=Thread3(queue)
t3.start()


####tarfile函数进行压缩



"""
使用Event函数进行线程间事件通知
"""
from threading import Event

def waitMethod(e):
    print("haha")
    ###等待其他线程通知
    e.wait()
    print("wait finish")

def startMethod(e):
    print("start method")
    ###通知其他线程
    e.set()
event=Event()
t4=Thread(target=waitMethod,args=(event,))
t5=Thread(target=startMethod,args=(event,))
t4.start()
t5.start()
event.clear()

"""
线程本地对象
使用threadlocal存储的对象，会为每一个使用threadlocal中维护的那个变量的线程单独提供
该变量，其他线程访问不到或者不会对当前线程维护的那个变量造成影响
"""
t_local=threading.local
t.x=3

def test(arg):
    t.x=arg
    print("%s"%(threading.current_thread())+" %s"%(t.x))

t8=Thread(target=test,args=(6,))
t8.start()
t9=Thread(target=test,args=(9,))
t9.start()

"""
引入线程池
可以防止线程被无限的创建，避免资源浪费
"""
from concurrent.futures import ThreadPoolExecutor
executors=ThreadPoolExecutor(3)

def testA(a,b):
    print(a**b)
    return "a : %s"%(a)+" b : %s"%(b)
####使用submit来执行方法
result=executors.submit(testA,2,3)
####通过future的result方法拿到方法执行的结果
print(result.result())
###使用map函数来，根据传递的参数来指定 方法执行的次数
executors.map(testA,[1,2,3],[2,4,6])