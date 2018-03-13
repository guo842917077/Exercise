"""
python中的异常捕获try-except--finally 类似java的try-catch-finally
使用raise抛出日志
assert : 断言功能  和java一致
logging:日志记录对象，可以保存日志到文件
"""
import logging

logging.basicConfig(level=logging.INFO)


def test():
    s = 2
    try:
        assert (s != 0)
        a = -2 / 0
    except Exception as e:
        logging.info("exception %s" % (e))
    finally:
        print("模拟一个错误")

test()
