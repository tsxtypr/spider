# -*- coding: utf-8 -*-

# Scrapy settings for wangyiyun project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'wangyiyun'

SPIDER_MODULES = ['wangyiyun.spiders']
NEWSPIDER_MODULE = 'wangyiyun.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'wangyiyun (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36',
    'referer': 'https://www.baidu.com/link?url=3IiGyyNc8mAay2LGTw_1BtfEnrCfXVXdvN4-B3W5a0e&wd=&eqid=c0f073d7000498a1000000035dc565c8',
    # 'referer':'https://music.163.com/discover/artist',
    # 'cookie':'_iuqxldmzr_=32; _ntes_nnid=dd7a1324751aefc09f5d2aa1764e3e29,1572500358113; _ntes_nuid=dd7a1324751aefc09f5d2aa1764e3e29; WM_TID=yqHqpUue3LlEAEFAFEc86Q0AN0gOnwoC; JSESSIONID-WYYY=n65vp7VTnQO%2Fwjk%2BqMJPXZQijP%2BySE7O%2BJXWozem%2F1H%5Can7OkMEgDNJkpoIrMahuhrkFrxeTjgYV9dAtgBtFzSWHvGPFMMTq0Zi%2FEG7uJlrcGxwwpKS2ox3j6lbhv%2Bq%2BpgngGogfPoc3cHT%2B7lbo1ViCk%2BVEirwA%2B33D1o5nuTEyOwwn%3A1573220158806; WM_NI=AjMkvvBlghsw6Eh30%2BPIY1nYKTuAgcuG%2Bup55tuB0%2FfJf3CK%2BSa94Q7%2F5IiJ150S%2FbaJDfG%2BcxClS0MRoqJTunyxAuZuvl9317DaVxJY1AoLEtWoPjevOVLjk3cDrtfqTFY%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed8bc7b8aac96a2f75eaa9a8aa3d54e868f9b84f7218588aaa6ae48b7a988d6dc2af0fea7c3b92a83b6838cf57e82b4a989f27df69ba8d4b321949797d2ed53898cbba2e669b799e596f33ff7acbba3b325a696aad4c241e98dafdab75bf5f1fbaaec42f3eb00b4ae6aa3968c87c621a1a88d8dd23c8f8ea192c960b7b2b799c47f9aabba8dbc39f3e98c82d5748a87ffa2ee4887ac9990d362a7aa81b7cf62a9edada5f180a6af9ca7dc37e2a',
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'wangyiyun.middlewares.WangyiyunSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'wangyiyun.middlewares.WangyiyunDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'wangyiyun.pipelines.WangyiyunPipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
