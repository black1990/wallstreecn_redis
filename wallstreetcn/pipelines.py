# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


# class WallstreetcnPipeline(object):
#     def process_item(self, item, spider):
#         return item
import pymongo
from wallstreetcn import settings
from wallstreetcn.items import WallstreetNewsItem
class MongoPipeline(object):
    def __init__(self):
        port = settings.MONGODB_PORT
        host = settings.MONGODB_HOST
        db_name = settings.MONGODB_DBNAME
        client = pymongo.MongoClient(port=port, host=host)
        db = client[db_name]
        self.content = db[settings.MONGODB_COTENTNAME]

    def process_item(self, item, spider):
        if isinstance(item, WallstreetNewsItem):
            content_info = dict(item)
            self.content.insert(content_info)
        return item
