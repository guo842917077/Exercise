"""
单元测试
1。首先导入unittest库
2.让一个类进程unittest.TestCase
3.写一个方法以test开头
4.使用assert断言方法来验证
5。使用main方法来执行，该方法会自动执行所有以test开头的方法
"""
import unittest
from jsontest import getUserName
class UserName(unittest.TestCase):
    def testUserName(self):
        testUserName=getUserName('guo')
        self.assertEquals(testUserName,'guo')

unittest.main()