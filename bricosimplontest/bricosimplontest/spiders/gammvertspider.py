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

                # sub_categories = response.css('a.ens-product-list-categories__item')
                # for sub_category in sub_categories:
                #     name_sub = sub_category.css('::text')
                #     url_sub = sub_category.css('::attr(href)')
                #     print('0000000000000000000')
                #     print(name_sub.get())
                #     print(url_sub.get())

                
                yield response.follow(self.start_urls[0] + lien.get(), self.parse_sub, meta = meta)
                # break



    def parse_sub(self,response:Response):
        print(response.meta)
        sub_categories = response.css('a.ens-product-list-categories__item')
        # if sub_categories: #si le bandeau menu existe
        for sub_category in sub_categories:
            name_sub = sub_category.css('::text')
            url_sub = sub_category.css('::attr(href)')
            print('0000000000000000000')
            print(name_sub.get())
            print(url_sub.get())

            meta = {
                'category_name' : name_sub.get(),
                'category_url' :url_sub.get(),

            }
            
            yield response.follow(self.start_urls[0] + url_sub.get(), self.parse_sub, meta = meta)
            # break

        yield {
            'category_name' : response.meta['category_name'],
            'category_url' :response.meta['category_url'], 
            'is_page_list' : True if not sub_categories else False
        }
            # if sub_category is not None:
            #     # yield{
            #     #         'subcategory_name' : name_sub.get(),
            #     #         'subcategory_url' :url_sub.get(),          
            #     #     }
            # else:
        #yield meta        
            # next = category.css('a ::attr(href)').get()
            

            


    # def parse_categories(self, response):
    #     sous_categorie_url = response.css('a ::attr(href)').get()
    #     sous_categorie_name = response.css('a .ens-product-list-categories__item ::text').get()

    #     yield{
    #         'sous_cat_name' : sous_categorie_name,
    #         'sous_cat_url' : sous_categorie_url

    #     }

        # next = category.css('a ::attr(href)').get()
        # print('**************************')
        # print(next)
        # if next:
        #     new_url = response.urljoint(next)
        #     print('++++++++++++++++++++++++++++')
        #     print(new_url)
        #     yield scrapy.Request(url = new_url, callback= self.parse)


