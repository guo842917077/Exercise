"""
集合
存储的是非重复对象，只存储键
存在可修改和不可修改两种集合
存储的元素必须支持hash方法
"""
#集合的包含关系不能用in not来判断 只能通过 > <等符号来判断
set1={1,2}
set2={3}
print(set1>set2)

#如何保证自定义类型在集合中不重复
#重写hash方法,和 eq方法
class User(object):
    def __init__(self,id):
        self.id=id

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        return self.id==other.id
users={User(1),User(1)}
#output 1  因为这两个对象一样，所以只保留了一个
print(len(users))
