# Scrapy settings for bookscraper project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Scrapy settings for bookscraper project
BOT_NAME = "bookscraper"  # Name of the bot (project)

SPIDER_MODULES = ["bookscraper.spiders"]  # List of modules where spiders are located
NEWSPIDER_MODULE = "bookscraper.spiders"  # Default module for new spiders

# Identify the bot to websites using a custom User-Agent string
USER_AGENT = "bookscraper (+http://www.yourdomain.com)"

# Whether to respect robots.txt rules (default: False)
ROBOTSTXT_OBEY = True

# Maximum concurrent requests Scrapy will perform (default: 16)
#CONCURRENT_REQUESTS = 32

# Delay between requests to the same website to avoid getting banned
#DOWNLOAD_DELAY = 3

# Limit concurrent requests per domain and IP
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Default request headers sent with each request
#DEFAULT_REQUEST_HEADERS = {
#   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
#   "Accept-Language": "en",
#}

# Enable or disable spider middlewares
#SPIDER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
#DOWNLOADER_MIDDLEWARES = {
#    "bookscraper.middlewares.BookscraperDownloaderMiddleware": 543,
#}

# Enable or disable extensions (e.g., for logging, stats)
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines (processing scraped items before saving)
#ITEM_PIPELINES = {
#    "bookscraper.pipelines.BookscraperPipeline": 300,
#}

# AutoThrottle settings to avoid server overloads
#AUTOTHROTTLE_ENABLED = True
#AUTOTHROTTLE_START_DELAY = 5
#AUTOTHROTTLE_MAX_DELAY = 60
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
#AUTOTHROTTLE_DEBUG = False

# HTTP caching to avoid re-downloading pages
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"
