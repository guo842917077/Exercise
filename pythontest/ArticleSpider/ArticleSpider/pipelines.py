# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
它可以拦截到Item
主要是做数据存储，在使用前需要在setting中将ITEM_PIPELINES注释放开，Item会自动被传入到此处
1.codecs可以更好的操作file，避免许多编码问题
2.json库 将数据转化为json
3.process_item 这个方法会将接收到的item返回出来，给客户端做处理
4.scrapy自身也提供了导出为各种数据类型的exporter
5.使用MySqlDb 需要导入mysqlclient库 以及mysql的python环境python_devel mysql_devel
6.也可以使用pymysql
7.当爬取的速度超过插入数据库的操作时，可以使用异步插入法，使用twist提供的连接池
8。scrapy提供了可以将数据倒出为各种类型的exporter
"""
from scrapy.pipelines.images import ImagesPipeline
###使用scrapy提供的exporter
from scrapy.exporters import JsonItemExporter
import codecs
import json
import pymysql as MySql
# 将mysql的操作 编程异步的操作
from twisted.enterprise import adbapi
import pymysql.cursors

class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


"""
自定义json导出方式
"""


class JobJsonPipeline(object):
    def __init__(self):
        self.file = codecs.open(filename='article.json', mode='w', encoding='utf-8')

    def process_item(self, item, spider):
        # ensure-ascii必须要设置，关闭ascii编码
        lines = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(lines)
        return item

    def spider_closed(self, spider):
        self.file.close()


"""
使用scrapy的exporter的方式导出数据成json
scrapy自带了json倒出方式 ---exporter
"""


class JobJsonExporter(object):
    def __init__(self):
        self.file = codecs.open('job_exporter.json', 'wb')
        self.exporter = JsonItemExporter(file=self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()

    def process_item(self, item, spider):
        # 传递数据给exporter
        self.exporter.export_item(item)
        return item

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


####定制自己的ImagePipeline
class ArticleImagePipeline(ImagesPipeline):
    # 可以获取到图片的实际下载地址
    # 使用debug方式查看result 是存放元组的数组，并且元组中的value 是一个dict
    def item_completed(self, results, item, info):
        for isOk, value in results:
            image_file_path = value['path']
        item['front_image_path'] = image_file_path
        return item


"""
读取settings的配置信息
需要在settings的pipline中配置
"""


class JobSettings(object):
    ##
    @classmethod
    def from_settings(self, settings):
        pass


"""
使用Pipline将数据保存到数据库
使用异步保存的方式
"""


class JobMySqlPipline(object):
    def __init__(self,dbPool):
        self.dbPool=dbPool

    ##这个方法会在pipline初始化的时候调用
    @classmethod
    def from_settings(cls, settings):
        host = settings["MY_HOST"]
        port = settings["MY_PORT"]
        account = settings["MY_ACCOUNT"]
        password = settings["MY_PASSWORD"]
        database = settings["MY_DATABASE"]
        # 要跟使用的mysql框架对应
        dbParams = dict(host=host, db=database, user=account, password=password, port=port,
                        charset='utf8', use_unicode=True)
        print("from settings : " + host + " password : " + password)
        #将数据库操作编程异步操作，这里pymysql代表使用的数据库
        dbPool = adbapi.ConnectionPool("pymysql", **dbParams)
        return cls(dbPool)

    def process_item(self, item, spider):
        # 传递数据给exporter
        # 使用twisted和mysql将数据库插入编程异步操作
        query= self.dbPool.runInteraction(self.do_insert,item)
        #添加异步错误处理操作
        query.addErrback(self.handleError,item,spider)
        return item

    def do_insert(self,cursor,item):
        sql = """
                    insert into article_spider(title,url,front_img_path,praise_nums)
                  VALUES (%s,%s,%s,%s)
                   """
        cursor.execute(sql, (item['title'], item['url'], item['front_img_url'], item['praise_nums'],))
        #不再需要commit操作，这个操作自动完成
        #self.conn.commit()
    def handleError(self,failuer,item,spider):
        print(failuer)
# class JobMySqlPipline(object):
#     def __init__(self):
#         host = "localhost"
#         port = 3306
#         account = "root"
#         password = "123456"
#         database = 'tpython'
#         self.conn = MySql.connect(host=host, port=port, user=account, password=password, database=database,
#                                   charset='utf8', use_unicode=True)
#         self.cursor = self.conn.cursor()
#
#     def process_item(self, item, spider):
#         # 传递数据给exporter
#         sql = """
#             insert into article_spider(title,url,front_img_path,praise_nums)
#           VALUES (%s,%s,%s,%s)
#         """
#         self.cursor.execute(sql, (item['title'], item['url'], item['front_img_url'], item['praise_nums'],
#                                   ))
#         self.conn.commit()
#         return item
