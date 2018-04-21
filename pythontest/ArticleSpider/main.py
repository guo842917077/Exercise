"""
调试scrapy
1.引入scrapy的命令行类
2.使用sys将获取项目工程的路径
3.根据os的path参数 获取到main文件的父目录
_file_参数表示当前文件 即main.py
4.在settings.py中 一定要把ROBOTSTXT_OBEY 设置成false，否则会查询每一个网站是否符合robots协议
不符合的就过滤
"""
import sys
import os
from scrapy.cmdline import execute
##output:/Users/apple/Desktop/workspace/pythonwork/ArticleSpider
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
execute(['scrapy',"crawl","jobbole"])