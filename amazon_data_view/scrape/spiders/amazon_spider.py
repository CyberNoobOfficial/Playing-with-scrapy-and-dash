from scrapy import Spider


class AmazonSpider(Spider):
    name = 'amazon_spider'
    start_urls = [
        'https://www.amazon.com/Childrens-Books/b/?ie=UTF8&node=4&ref_=sv_b_4'
    ]
    custom_settings = {
        'LOG_ENABLED': 'False',
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'data.csv',
        'ITEM_PIPELINES': {'scrape.pipelines.AmazonPipeline': 300},
    }

    def parse(self, response):
        for book in response.css('.octopus-pc-item-v3'):
            yield {
                'title': book.css('.octopus-pc-asin-title .a-color-base::text').get().strip(),
                'rating': book.css('.octopus-pc-asin-review-star .a-color-tertiary::text').get().strip()
            }
