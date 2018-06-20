"""
当我们不想要一个方法的参数操作原对象时，可以使用拷贝
1.浅拷贝：只拷贝出一份原对象的引用，拷贝对象不拷贝原对象内部的元素，对拷贝对象内部元素进行修改仍然会印象原对象
2.深拷贝：拷贝出一份一模一样的对象，对象的引用和内部数据的引用全部拷贝
"""
import copy
class A:
    def __init__(self):
        self.data=[]

a=A()
##浅拷贝

copy_a=copy.copy(a)
copy_a.data.append('copy')
print("copy result : "+str(a.data))

##深拷贝
deep_a=copy.deepcopy(a)
deep_a.data.append('deep')
print("deep copy : "+str(a.data))



"""
output result: 
copy result : ['copy']
deep copy : ['copy']
"""