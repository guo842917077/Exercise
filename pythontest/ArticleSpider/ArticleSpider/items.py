# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html
import datetime
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst
"""
定义爬出数据的item，类似javabean
当使用ItemLoader时，返回到item类中的每一个参数将是数组
在Field中可以添加预处理函数,通过input_processor参数
1.processor在loader。processors中，当字段传入到item的field中时，会预先调用mapcompose指定的方法
2.TakeFirst 定义了选取返回数据中的第几个元素
"""

"""
自定义ItemLoader，解决每次itemloader返回的都是数组的问题，变为取第一个
"""
class FirstItemLoader(ItemLoader):
    default_output_processor = TakeFirst()


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def returnValue(value):
    return value

"""
定义数据类型，将数据组成结构，并返回数据给scrapy
当scrapy发现数据是一个item时，会自动将数据路由到pipelines中
"""
def addTtitle(value):
    return value+'-guo'
"""
解析时间
"""
def parseData(data):
  try:
      create_date = datetime.datetime.strptime(data, "%Y/%m/%d").date()
  except Exception as e:
      create_date = datetime.datetime.now().date()
  return create_date

class JoBBoleArticleItem(scrapy.Item):
    """
    标题
    """
    title = scrapy.Field(
        #MapCompose需要传入一个回调函数，可以对取到的值做预处理
        #可以接收多个方法
        input_processor=MapCompose(lambda x:x+"-spider",addTtitle)
    )
    create_date = scrapy.Field(input_processor=MapCompose(parseData))
    """
    文章地址
    """
    url = scrapy.Field()
    # 使用md5对url进行转换
    url_md5_id = scrapy.Field()
    """
    首页图片
    """
    ##使用自定义的item后，返回的将是单个字符串而不是数组，所以使用自定义个processor覆盖掉
    ##原来的outputProcessor
    front_img_url = scrapy.Field(output_processor=MapCompose(returnValue))
    front_img_path = scrapy.Field()
    """
    点赞数
    """
    praise_nums = scrapy.Field()
    """
    评论数
    """
    commment_nums = scrapy.Field()
    """
    内容
    """
    content = scrapy.Field()

