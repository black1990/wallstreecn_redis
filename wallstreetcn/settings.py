# -*- coding: utf-8 -*-

# Scrapy settings for wallstreetcn project
BOT_NAME = 'wallstreetcn'
SPIDER_MODULES = ['wallstreetcn.spiders']
NEWSPIDER_MODULE = 'wallstreetcn.spiders'
#redis配置
REDIS_URL = None
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
SCHEDULER_PERSIST = True
SCHEDULER_FLUSH_ON_START = False
SCHEDULER_IDLE_BEFORE_CLOSE = 0
SCHEDULER_QUEUE_KEY = '%(spider)s:requests'
SCHEDULER_DUPEFILTER_KEY = '%(spider)s:dupefilter'
CONCURRENT_REQUESTS = 1
#Mongo配置
MONGODB_HOST = '127.0.0.1'
MONGODB_PORT =27017
MONGODB_DBNAME = 'wallstreet_news'
MONGODB_COTENTNAME='content_item'
# Obey robots.txt rules
ROBOTSTXT_OBEY =False
DOWNLOAD_DELAY = 1
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'wallstreetcn.pipelines.MongoPipeline': 300,
}
# #启用Redis调度存储请求队列
SCHEDULER = "wallstreetcn.scrapy_redis.scheduler.Scheduler"
#确保所有的爬虫通过Redis去重
DUPEFILTER_CLASS = "wallstreetcn.scrapy_redis.dupefilter.RFPDupeFilter"
#DUPEFILTER_CLASS = "wallstreetcn.BloomRedisDupefilter.BloomRedisDupeFilter"
#默认请求序列化使用的是pickle 但是我们可以更改为其他类似的。PS：这玩意儿2.X的可以用。3.X的不能用
#SCHEDULER_SERIALIZER = "scrapy_redis.picklecompat"
#不清除Redis队列、这样可以暂停/恢复 爬取
#SCHEDULER_PERSIST = True

#使用优先级调度请求队列 （默认使用）
#SCHEDULER_QUEUE_CLASS = 'wallstreetcn.scrapy_redis.queue.PriorityQueue'
#可选用的其它队列
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
#SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'

#最大空闲时间防止分布式爬虫因为等待而关闭
#SCHEDULER_IDLE_BEFORE_CLOSE = 10

# Store scraped item in redis for post-processing
#redis存储数据
# ITEM_PIPELINES = {
#     'scrapy_redis.pipelines.RedisPipeline': 300
# }

#序列化项目管道作为redis Key存储
#REDIS_ITEMS_KEY = '%(spider)s:items'

#默认使用ScrapyJSONEncoder进行项目序列化
#You can use any importable path to a callable object.
#REDIS_ITEMS_SERIALIZER = 'json.dumps'

#指定连接到redis时使用的端口和地址（可选）
# REDIS_HOST = 'localhost'
# REDIS_PORT = 6379

#指定用于连接redis的URL（可选）
#如果设置此项，则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
#REDIS_URL = 'redis://user:pass@hostname:9001'
#REDIS_URL='redis://sun:sa@127.0.0.1:6379'

#自定义的redis参数（连接超时之类的）
#REDIS_PARAMS  = {}

#自定义redis客户端类
#REDIS_PARAMS['redis_cls'] = 'myproject.RedisClient'

#如果为True，则使用redis的'spop'进行操作。
#如果需要避免起始网址列表出现重复，这个选项非常有用。开启此选项urls必须通过sadd添加，否则会出现类型错误。
#REDIS_START_URLS_AS_SET = False

#RedisSpider和RedisCrawlSpider默认 start_usls 键
#REDIS_START_URLS_KEY = '%(name)s:start_urls'

#设置redis使用utf-8之外的编码
#REDIS_ENCODING = 'latin1'
