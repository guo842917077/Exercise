###给元组的值命名
AGE,NAME,WORK=range(3)
student=(24,"java","guojinlong")
print(student[NAME])
####使用collections内置的nametuple来创建元组
from collections import namedtuple
Student=namedtuple("student",['name','age','work'])
s=Student('guo',25,'java')
print(s)


