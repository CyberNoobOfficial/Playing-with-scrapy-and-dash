from scrapy.crawler import CrawlerProcess

from scrape.spiders.amazon_spider import AmazonSpider

process = CrawlerProcess({'LOG_ENABLED': 'False'})


def run_spiders():
    process.crawl(AmazonSpider)
    process.start()  # the script will block here until the crawling is finished
