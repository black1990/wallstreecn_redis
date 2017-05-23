# -*- coding: utf-8 -*-
import scrapy
import json
import re
from wallstreetcn.items import WallstreetNewsItem
from wallstreetcn.scrapy_redis.spiders import RedisSpider
import random,time
class WallstreetSpider(RedisSpider):
    name = "wallstreet"
    redis_key = 'wallstreet:start_urls'
    news_categorys = ['global','shares','bonds','commodities','forex','enterprise','economy','china','us','europe','japan']
    new_base_url = 'https://api-prod.wallstreetcn.com/apiv1/content/articles?category={category}&limit=20&platform=wscn-platform'
    next_base_url = 'https://api-prod.wallstreetcn.com/apiv1/content/articles?category={category}&limit=20&cursor={cursor}&platform=wscn-platform'
    live_categorys = ['global-channel','a-stock-channel','us-stock','weex-channel,gold-channel,gold-forex-channel','event-channel']
    def start_requests(self):
        for category in self.news_categorys:
            yield scrapy.Request(self.new_base_url.format(category=category), callback=self.parse)

    def parse(self, response):
        results = json.loads(response.text)
        category = re.findall(r'.*?category=(.*?)&.*?', response.url)[0]
        dic = {}
        if 'data' in results.keys():
            news_items = results.get('data').get('items')
            for each_news_item in news_items:
                dic['author'] = each_news_item['author']
                dic['content_short'] = each_news_item['content_short']
                dic['image_uri'] = each_news_item['image_uri']
                dic['title'] = each_news_item['title']
                dic['content_uri'] = each_news_item['uri']
                headers = {
                     'accept-encoding': 'gzip, deflate, sdch, br',
                     'accept-language': 'zh-CN,zh;q=0.8',
                     'accept': 'application/json, text/plain, */*',
                     'origin': 'https://wallstreetcn.com',
                     'referer': dic['content_uri'],
                     'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'
                }
                try:
                    result = re.search('https://wallstreetcn.com/articles/', dic['content_uri'])
                    if result is None:
                        print('文章：%s 不在匹配范围' % dic['content_uri'])
                    else:
                        #time.sleep(3)
                        yield scrapy.Request(url=dic['content_uri'], meta=dic,
                                            headers=headers, callback=self.parse_news_content, dont_filter=True)
                except(IndexError) as e:
                    print(e)
        if 'next_cursor' in results.get('data'):
            cursor = results.get('data').get('next_cursor')
            yield scrapy.Request(self.next_base_url.format(category=category, cursor=cursor),
                                 callback=self.parse, dont_filter=True)
    def parse_news_content(self, response):
        item = WallstreetNewsItem()
        item['author'] = response.meta['author']
        item['content_short'] = response.meta['content_short']
        item['image_uri'] = response.meta['image_uri']
        item['title'] = response.meta['title']
        item['content_uri'] = response.meta['content_uri']
        content = response.xpath('//div[@class="node-article-content"]').extract()[0]
        content_time = response.css('span.meta-item__text::text').extract()[0]
        pattern = re.compile(r'<[^>]+>', re.S)
        del_html_content = pattern.sub('', content)#文章内容
        item['content_time'] = content_time
        item['content'] = del_html_content
        yield item
