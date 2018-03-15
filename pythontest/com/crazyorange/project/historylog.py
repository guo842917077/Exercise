####使用队列来保存输入记录
from collections import deque
####创建一个设定容量的队列
log=deque([],5)
"""
使用pickle将log存入到文件中
他可以存储一个python对象到文件中
"""
import pickle
pickle._dump(log,open('d:/log','w'))
history=pickle.load(open('d:/log'))



