import scrapy


class IkeaspiderSpider(scrapy.Spider):
    name = "ikeaspider"
    allowed_domains = ["www.ikea.com"]
    start_urls = ["https://www.ikea.com/fr/fr/"]

    def parse(self, response):
        categories = response.css('div .hnf-tabs-navigation__container div.hnf-tabs-navigation__carousel-wrapper')
        # cat = categories[0]
        # categories.css('div .hnf-carousel-slide span ::text').getall()

        for cat in categories:

            print('000000000000000000000000000000000')
            print(cat.css('div .hnf-carousel-slide span ::text').getall())
            yield {
                "titre" : cat.css('div .hnf-carousel-slide span ::text').get(),

                # "url" : cat.css('')
            }
            next  = response.xpath('/html/body/div/div/div/div/div/div/nav/ul/li/div/a/@href').get()
            print('COUCOU0000000000000000000000000000')
            print(next)

                #break
        #tab-products > div:nth-child(1)
            # }
            # button = hnf-btn__inner
            #title = cat.css('div .hnf-carousel-slide span ::text').get()
            






    #         yield {
    #             'nom_lit': response.css('span.notranslate.plp-price-moduleproduct-name::text').getall(),
    #             'prix': response.css('span.plp-priceinteger::text').getall(),


    #         }
        # categories = response.xpath('//body/div')
        # yield {
        #     "categories" : categories
        # }

