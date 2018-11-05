"""
回调练习
1.因为python可以将方法作为参数传递，利用这点直接建立一个callback方法
"""

def callBack(msg):
    print(msg)



def goto(msgCallBack):
    x=10
    msgCallBack(x)

goto(callBack)