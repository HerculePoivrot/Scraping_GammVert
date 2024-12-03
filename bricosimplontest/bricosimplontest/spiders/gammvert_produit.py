from collections.abc import Iterable
import scrapy
import re
import json
import math
from bricosimplontest.items import BookscraperItem


class GammvertSpider(scrapy.Spider):

    name = "gammvert"
    allowed_domains = ["www.gammvert.fr"]
    start_urls= ['https://www.gammvert.fr/']
    url_actuel = ''
    page_index = 1
    



    def start_requests(self):

        chemin = 'data.json'

        with open(chemin, 'r') as fichier:
            data = json.load(fichier)

        for d in data:
        
            if d['is_page_list']:
                self.page_index = 1
                self.calculer_nb_pages = False
                self.url_actuel = self.start_urls[0] + d['category_url'][1:]
                yield scrapy.Request(
                    url = self.url_actuel,
                    callback=self.parse)

    calculer_nb_pages = False

    page_index = 1
    def parse(self, response):

        articles = response.css('.ens-product-list__item')
        
        if not self.calculer_nb_pages : 

            recup_nb_article_brut = response.css('.ens-product-list-template__products-counter span::text').get()

            nb_produit_brut = recup_nb_article_brut.split(' ')
            nb_produit = int(nb_produit_brut[6])

            self.nb_pages = math.ceil((nb_produit // 50))
            self.calculer_nb_pages = True




        
        

        for article in articles:
            list_categorie = response.css('.idf-breadcrumb__entry-label::text').getall()
            note_brut = article.css('.ds-ens-product-card__rating span.idf-rating::attr(style)').get()
            note= float(re.sub(r'[^0-9.]', '', note_brut)) if note_brut is not None else 'PAS DE NOTE'
            title = article.css('.ds-ens-product-card__name::text').get()
            url_incomplete = article.css('a.ens-product-list__link::attr(href)').get()
            url_split = url_incomplete.split('-')
            id_produit = url_split[-1]
            url = response.urljoin(url_incomplete)
            prix = article.css('.ds-ens-pricing__price-amount--xxl.ds-ens-pricing__price-amount--l.ds-ens-pricing__price-amount--bold::text').get()
            categorie_principale = list_categorie[0]
            sous_categorie_principale = list_categorie[-2]
            

            yield BookscraperItem(
                nom_produit = title,
                note = note,
                prix  = prix,
                id_produit=id_produit,
                categorie = categorie_principale,
                sous_categorie = sous_categorie_principale,
                url = url)
        
        if self.page_index <= self.nb_pages or self.page_index == 20:
            self.page_index += 1

            yield response.follow(self.url_actuel+ '?p='+str(self.page_index), callback = self.parse)
