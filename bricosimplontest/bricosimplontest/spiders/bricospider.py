import scrapy


class BricospiderSpider(scrapy.Spider):
    name = "bricospider"
    allowed_domains = ["bricodiscount.fr"]
    start_urls = ["https://bricodiscount.fr"]

    def parse(self, response):
        pass
