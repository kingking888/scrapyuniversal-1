# -*- coding: utf-8 -*-

# Scrapy settings for scrapyuniversal project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'scrapyuniversal'

SPIDER_MODULES = ['scrapyuniversal.spiders']
NEWSPIDER_MODULE = 'scrapyuniversal.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'scrapyuniversal (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
# }
DEFAULT_REQUEST_HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/59.0.3071.115 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'scrapyuniversal.middlewares.ScrapyuniversalSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
# DOWNLOADER_MIDDLEWARES = {
#    'scrapyuniversal.middlewares.ScrapyuniversalDownloaderMiddleware': 543,
# }
# DOWNLOADER_MIDDLEWARES = {
#     'scrapyuniversal.middlewares.CookiesMiddleware': 554,
#     'scrapyuniversal.middlewares.ProxyMiddleware': 555,
#     'scrapyuniversal.middlewares.SeleniumMiddleware': 556
# }

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'scrapyuniversal.pipelines.ScrapyuniversalPipeline': 300,
# }
ITEM_PIPELINES = {
    'scrapyuniversal.pipelines.TimePipeline': 300,
    'scrapyuniversal.pipelines.MongoPipeline': 301,
    # 'scrapyuniversal.pipelines.MysqlPipeline': 302
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
RETRY_HTTP_CODES = [401, 403, 408, 414, 500, 502, 503, 504]

# Scrapy-Redis
# SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# scrapy_redis_bloomfilter
SCHEDULER = 'scrapy_redis_bloomfilter.scheduler.Scheduler'
DUPEFILTER_CLASS = "scrapy_redis_bloomfilter.dupefilter.RFPDupeFilter"
BLOOMFILTER_BIT = 30
BLOOMFILTER_HASH_NUMBER = 6
SCHEDULER_PERSIST = True
REDIS_HOST = '192.168.2.104'
REDIS_PORT = 6379
REDIS_PASSWORD = None
REDIS_DATABASE = 0

# COOKIES_URL = 'http://120.27.34.25:5556/weibo/random'
# PROXY_URL = 'http://120.27.34.25:5555/random'

# SELENIUM_TIMEOUT = 20
# PHANTOMJS_SERVICE_ARGS = ['--load-images=false', '--disk-cache=true']

# MySQL
MYSQL_HOST = '192.168.2.104'
MYSQL_DATABASE = 'spider'
MYSQL_USER = 'root'
MYSQL_PASSWORD = 'root'
MYSQL_PORT = 3306

# MONGO
MONGO_URI = '192.168.2.104'
MONGO_DB = 'spider'
