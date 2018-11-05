"""
python io流测
1.open()读取文件内容，path：路径   r 只读   w写   a 追加
2.close()使用close 关闭流
3.如果使用with .. as  语法  可以避免主动调用close方法
4。要读取2进制文件，open的第二个参数 必须是rb
5.使用encoding方法指定字符编码
6。
"""
path = '/Users/apple/Desktop/Exercise/Exercise/pythontest/com/crazyorange/python/exception/ExceptionTest.py'
with open(path, 'r', encoding='utf-8') as f:
    for line in f.readlines():
        print(line)

"""
内存读写  使用stringIO和BytesIO
1.stringIO 只能操作str
2.byteIO 可以操作二进制数组
"""
from io import StringIO

f = StringIO()
f.write("haha,my name is guo")
print(f.getvalue())

from io import BytesIO

a = BytesIO()
a.write("中文".encode('utf-8'))
print(a.getvalue())

import os

# 操作系统
print(os.name)
# 所有环境变量
print(os.environ)
# 指定环境变量
print(os.environ.get('PATH'))


class Tt:
  def __init__(self):
      self.a=10
      self.guo='guo'


import json

t = Tt()
print(json.dumps(t, default=lambda obj: obj.__dict__))
