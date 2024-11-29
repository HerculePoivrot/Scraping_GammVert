import scrapy

class BookspiderSpider(scrapy.Spider):
    name = 'bookspider'
    allowed_domains = ['manomano.fr']
    start_urls = ['https://www.manomano.fr/luminaire-solaire-5283']

    def parse(self, response):
        articles = response.css('li.b9bdc658')
        # for article in articles:
        #     yield{
        #         'name' : article.css().get()
        #         'price'
        #         'url'

        #     }