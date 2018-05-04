"""
在同一个进程内，多个线程的执行 需要获得GIL锁的同意，哪个线程获得了锁，哪个线程可以执行
"""
from multiprocessing import Process,Pipe
import queue
def p1(c):
    print("receive a num ")
    result=c.recv()
    print(result)
    c.send(result*2)
###Pipe 创建一个双向的管道 c1 send的  c2可以receive到
c1,c2=Pipe()

Process(target=p1,args=(c2,)).start()
c1.send(10)
print(c1.recv())
