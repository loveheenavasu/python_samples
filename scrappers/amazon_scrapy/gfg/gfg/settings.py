BOT_NAME = 'gfg'

SPIDER_MODULES = ['gfg.spiders']
NEWSPIDER_MODULE = 'gfg.spiders'


ROBOTSTXT_OBEY = True

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
ITEM_PIPELINES = {
  'scrapy.pipelines.images.ImagesPipeline': 1
}
IMAGES_STORE = 'tmp/images/'


FEED_FORMAT = "csv"
FEED_URI = "reddit.csv"
# PROXY_POOL_ENABLED = True

# DOWNLOADER_MIDDLEWARES = {
#     # ...
#     'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
#     'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
#     # ...
# }

