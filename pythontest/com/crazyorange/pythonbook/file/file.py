"""
使用open操作文件，分为三种模式
'r':读取模式 读取文件的内容
'w'：写入模式 写入内容到文件，如果文件已经存在会清空远
'a'：追加模式

try--except--else  : 当try的代码正确执行时走else，不正确时走except
"""
path='/Users/apple/Desktop/Exercise/Exercise/pythontest/com/crazyorange/filterdir'
lines=[]
try:
   with open(path,'a') as open_file:
    open_file.write('\n美工')
except FileExistsError:
    print('File is exists')
      

try:
  with open(path) as open_file:
    lines=open_file.readlines()
except FileNotFoundError:
    print('File not found ')
else:
    for line in lines:
        print(line)
    




