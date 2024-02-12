# Scrapy settings for linkedinJobsScraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "linkedinJobsScraper"

SPIDER_MODULES = ["linkedinJobsScraper.spiders"]
NEWSPIDER_MODULE = "linkedinJobsScraper.spiders"

FEEDS = {
    'job_listings.json' : {'format': 'json'}
}

# Database settings
DATABASE = {
    'host': 'localhost',          
    'port': '5432',               
    'user': 'postgres',
    'password': '1234',
    'database': 'postgres'
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "linkedinJobsScraper (+http://www.yourdomain.com)"

# Fake User Agents
SCRAPEOPS_API_KEY = '4be9b634-d055-407e-9895-61aebc448b49'
SCRAPEOPS_FAKE_USER_AGENT_ENDPOINT = 'http://headers.scrapeops.io/v1/user-agents'
SCRAPEOPS_FAKE_USER_AGENT_ENABLED = True 
SCRAPEOPS_NUM_RESULTS = 50

## https://geonode.com/free-proxy-list
ROTATING_PROXY_LIST = [
    '183.89.116.141:4145',
    '147.182.203.142:12345',
    '159.89.173.98:14061'
]

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

SCRAPEOPS_PROXY_ENABLED = True

## custom middleware to use with a premium proxy endpoint provider    
# PROXY_USER = 'username'
# PROXY_PASSWORD = 'password'
# PROXY_ENDPOINT = 'proxy.proxyprovider.com'
# PROXY_PORT = '8000'

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
#DEFAULT_REQUEST_HEADERS = {
#    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#    "Accept-Language": "en",
#}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "linkedinJobsScraper.middlewares.LinkedinjobsscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    ## custom middleware for the premium proxy endopoint provider
    # "linkedinJobsScraper.middlewares.MyProxyMiddleware": 350, 
    # "scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware": 400, 
    
    ## default one
    # "linkedinJobsScraper.middlewares.LinkedinjobsscraperDownloaderMiddleware": 543,
    
    ## Fake User Agent and header
    # "linkedinJobsScraper.middlewares.ScrapeOpsFakeUAMiddleware": 544,
    # "linkedinJobsScraper.middlewares.ScrapeOpsBrowserHeaderMiddleware": 544,
    
    ## Rotating proxy, must be disabled to not interfere with other proxy stuff
    # "rotating_proxies.middlewares.RotatingProxyMiddleware": 610,
    # "rotating_proxies.middlewares.BanDetectionMiddleware": 620,
    
    ## scrapeops proxy sdk
    'scrapeops_scrapy_proxy_sdk.scrapeops_scrapy_proxy_sdk.ScrapeOpsScrapyProxySdk': 725,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   "linkedinJobsScraper.pipelines.LinkedinjobsscraperPipeline": 300,
   "linkedinJobsScraper.pipelines.SaveDataPipeline": 400,
   
}

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
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"
