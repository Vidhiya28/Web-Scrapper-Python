# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# Importing Scrapy's signal system for handling events like when a spider is opened or closed
from scrapy import signals

# Importing utilities to help handle different item types
from itemadapter import is_item, ItemAdapter

# Define the middleware for the spider (logic before/after a response is processed by the spider)
class BookscraperSpiderMiddleware:
    
    # Scrapy uses this method to create spider instances
    @classmethod
    def from_crawler(cls, crawler):
        # Create an instance of this middleware
        s = cls()
        # Connect the spider_opened method to the spider_opened signal
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # Process incoming response before reaching spider logic
    def process_spider_input(self, response, spider):
        # Return None so that the spider continues processing
        return None

    # Process the result after the spider has processed the response
    def process_spider_output(self, response, result, spider):
        # Yield each item from the spider’s result
        for i in result:
            yield i

    # Handle exceptions raised in process_spider_input or during spider processing
    def process_spider_exception(self, response, exception, spider):
        # Handle the exception and return None or a list of items/requests
        pass

    # Process requests when the spider starts crawling
    def process_start_requests(self, start_requests, spider):
        # Yield each request to start the crawling
        for r in start_requests:
            yield r

    # Called when the spider is opened
    def spider_opened(self, spider):
        # Log spider opening message
        spider.logger.info("Spider opened: %s" % spider.name)


# Define the middleware for the downloader (logic before/after a request is processed by the downloader)
class BookscraperDownloaderMiddleware:

    # Scrapy uses this method to create downloader middleware instances
    @classmethod
    def from_crawler(cls, crawler):
        # Create an instance of this middleware
        s = cls()
        # Connect the spider_opened method to the spider_opened signal
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # Process request before the downloader handles it
    def process_request(self, request, spider):
        # Return None to continue processing the request
        return None

    # Process the response after it has been downloaded
    def process_response(self, request, response, spider):
        # Return the response object so that the spider can process it
        return response

    # Handle exceptions raised in process_request
    def process_exception(self, request, exception, spider):
        # Handle the exception and return None, Response, or Request object
        pass

    # Called when the spider is opened
    def spider_opened(self, spider):
        # Log spider opening message
        spider.logger.info("Spider opened: %s" % spider.name)
