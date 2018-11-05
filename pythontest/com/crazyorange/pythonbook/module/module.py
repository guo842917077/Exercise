def hello():
    print("demo test")

def privateF():
    print("private function")

#使用all声明模块中的那些功能是可以*号方式导入的
__all__=["hello"]