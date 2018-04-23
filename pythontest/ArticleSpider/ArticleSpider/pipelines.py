# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
"""
主要是做数据存储，在使用前需要在setting中将ITEM_PIPELINES注释放开，Item会自动被传入到此处
"""
from scrapy.pipelines.images import ImagesPipeline


class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item


####定制自己的Pipeline
class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for isOk, value in results:
            image_file_path = value['path']
        item['front_image_path']=image_file_path
        return item
