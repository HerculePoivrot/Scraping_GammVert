import scrapy
from scrapy.http.response import Response


class GammvertspiderSpider(scrapy.Spider):
    name = "gammvertspider"
    allowed_domains = ["gammvert.fr"]
    start_urls = ["https://www.gammvert.fr"]

    def parse(self, response):
        '''
        Extrait les liens des catégories de la main page et leur nom
        '''
        categories = response.css('.ens-main-navigation-items__item')
        for category in categories:
            lien = category.css('a ::attr(href)')
            name = category.css('span ::text')
            
            if name.get() not in ['Noël', 'Promotions','Conseils & idées']:
       
                meta = {
                    'category_name' : name.get(),
                    'category_url' :lien.get(),          
                }


                
                yield response.follow(self.start_urls[0] + lien.get(), self.parse_sub, meta = meta)



    def parse_sub(self,response:Response):

        sub_categories = response.css('a.ens-product-list-categories__item')
        
        for sub_category in sub_categories:
            name_sub = sub_category.css('::text')
            url_sub = sub_category.css('::attr(href)')


            meta = {
                'category_name' : name_sub.get(),
                'category_url' :url_sub.get(),

            }
            
            yield response.follow(self.start_urls[0] + url_sub.get(), self.parse_sub, meta = meta)
            

        yield {
            'category_name' : response.meta['category_name'],
            'category_url' :response.meta['category_url'], 
            'is_page_list' : True if not sub_categories else False
        }



