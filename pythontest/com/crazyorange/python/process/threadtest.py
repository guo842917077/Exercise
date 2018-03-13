"""
多线程学习
1。使用threading库，它封装了_thread库，是一个更高级的线程库，功能更完善
2.创建一个线程对象使用threading的Thread方法
3.锁对象 在多线程中使用同步锁  使用threading.RLock()
"""

import threading, time

lock = threading.RLock()

haha=0;


def test(name):
    lock.acquire()
    start=time.time();
    haha = name
    print("current thread is %s name is %s" % (threading.current_thread(),haha))
    lock.release()
    end=time.time()
    print("execute time is %s"%(end-start))

def test2(name):
    lock.acquire()
    haha = name
    print("current thread is %s name is %s" % (threading.current_thread(), haha))
    lock.release()


thread1 = threading.Thread(target=test, args=('guo',), name="test")
thread1.start()

thread2 = threading.Thread(target=test2, args=('shuai',), name="haha")
thread2.start()

"""
thread_lock 维护当前线程的某个对象的副本 
1.使用threading的local方法创建一个thread_local对象
"""
thread_local=threading.local()
def student():
    name=thread_local.name
    print("student name is %s"%(name))

def school(name):
    thread_local.name=name
    student()

t1=threading.Thread(target=school,args=('guo',))
t2=threading.Thread(target=school,args=('liu',))
t1.start()
t2.start()
t1.join()
t2.join()