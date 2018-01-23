"""
高级函数方法
1。因为python是一种动态语音，可以给对象动态的绑定参数和方法，可以使用——slots——指定对象可以
绑定的方法
2。python可以使用@Property 声明一个属性的get，set方法。在操作属性的时候 会直接调用它的get，set方法
注意提供的方法名要和属性名一致
3.注意一点的是 @property方法内部的参数不能和方法名一样，否则出现递归无限调用。
  要先调用set方法才能再调用 get方法，否则self 并没有和你声明的对象进行绑定。
"""


class SlotsObj(object):
    ##声明属性score的get方法
    @property
    def width(self):#width的set方法
        print("start set width")
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def resolution(self):
        return self._width




def test():
    slotsObj = SlotsObj()
    slotsObj.name = "guo"
    slotsObj.age = 33
    ##由于没有在slots 中声明可以绑定gradle对象  所以这里绑定不会成功，并且会失败
    # slotsObj.gradle = 33
    print(type(slotsObj))
    ##实际上调用的是setWidth方法，调用了self._width给 对象生成了一个 _width对象
    slotsObj.width=200
    print(slotsObj.width)


test()
