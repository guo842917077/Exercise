"""
时间模块 datetime
"""
from datetime import datetime

now = datetime.now()
print(now)

"""
给元组的数据命名
"""
from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

"""
双向链表
"""
from collections import deque

deq = deque(['a', 'b', 'c'])
deq.append('d')
deq.remove('c')
print(deq)

"""
算法摘要 hashlib  包含了md5，sha1等算法
将某一段数据进行加密,注意需要指定字符串的编码方式
"""
import hashlib
m=hashlib.md5()
m.update('no body haha'.encode('utf-8'))
print(m.digest())

