from com.crazyorange.python.classtest.Student import Student
"""
使用type创建类型，类似于java的反射
1.类名
"""

def test():
    print("这里是替换的方法")


Student=type('Student',(object,),dict(run=test))
s=Student()



