# Scrapy settings for xueshu project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'xueshu'

SPIDER_MODULES = ['xueshu.spiders']
NEWSPIDER_MODULE = 'xueshu.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en',
    # 'referer': 'https://scholar.google.com.hk/scholar?start=20&hl=zh-TW&as_sdt=2005&sciodt=0,5&cites=8493427109448629428&scipsc=',
    'cookie': '__51uvsct__JIOiBUQQkX0bqCxs=1; __51vcke__JIOiBUQQkX0bqCxs=977ac609-6950-5a34-984a-873c51cffa0a; __51vuft__JIOiBUQQkX0bqCxs=1629553621378; __gads=ID=accd6ea3474a2bc4-22beb1ca0ccb0064:T=1629553621:RT=1629553621:S=ALNI_MYZMK6mbyPP1p-5gJeimPjCcMijAw; session=.eJw9z1tPwkAQBeD_0mdJZtvZy_BWJSAkKI2QyFMz253lotTai4YY_7s1Jp4fcM53vpIyttIdk2nfDnKTlKeQTBPn2FQZ2UyhBw-cYqrJko8hooAgZJUnB5kAZsEFVhHZSZVWCKmHoINjstGhjhlWwXmxAXxKziAFw4zRjgUGQSkvyqmUowCx9yIqesNVMkIaaS9cS93_04ZO2j_fIf_N7XFZcGN8MykeF_k-9_vt0jS793PTP9_b2akuJ0_r9WXVXbJNujj3oIfXw2p_7Rh195lnsp15U4Kbt1i0d9E84Jw3u-vpYzgWo6Dq2lj2by9Sj4uMbIkCcrCgg7LjKXJEkTQggUKHjlTUKvn-ATYHZjA.YSEG2Q.3LHq_jw7aB8zw_PhEuWLKz_DYMI; __vtins__JIOiBUQQkX0bqCxs=%7B%22sid%22%3A%20%227c4d97d5-87d2-5883-ab3f-70cf4043f2f1%22%2C%20%22vd%22%3A%2025%2C%20%22stt%22%3A%20774739%2C%20%22dr%22%3A%206893%2C%20%22expires%22%3A%201629556196111%2C%20%22ct%22%3A%201629554396111%7D',

}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
SPIDER_MIDDLEWARES = {
    'xueshu.middlewares.XueshuSpiderMiddleware': 543,
}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'xueshu.middlewares.ProxyMiddleware': 100,
    'xueshu.middlewares.XueshuDownloaderMiddleware': 543,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    'xueshu.pipelines.XueshuPipeline': 300,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
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
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
