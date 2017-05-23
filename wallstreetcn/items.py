# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# class WallstreetcnItem(scrapy.Item):
#     # define the fields for your item here like:
#     pass
class WallstreetNewsItem(scrapy.Item):
    author=scrapy.Field()#作者
    content_short=scrapy.Field()#文章概要
    image_uri=scrapy.Field() #文章图片
    title=scrapy.Field()#文章标题
    content_id=scrapy.Field()#文章id
    content_uri=scrapy.Field()#文章链接地址
    content=scrapy.Field()#文章内容
    content_time=scrapy.Field()#发布时间
class WallstreetLiveItem(scrapy.Item):
    pass

