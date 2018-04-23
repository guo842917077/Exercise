# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class JoBBoleArticleItem(scrapy.Item):
    """
    标题
    """
    title = scrapy.Field()
    create_date = scrapy.Field()
    """
    文章地址
    """
    url = scrapy.Field()
    # 使用md5对url进行转换
    url_md5_id = scrapy.Field()
    """
    首页图片
    """
    front_img_url = scrapy.Field()
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
