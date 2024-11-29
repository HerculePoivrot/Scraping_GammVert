# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookscraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nom_produit =  scrapy.Field()
    note =  scrapy.Field()
    prix =  scrapy.Field()
    id_produit =  scrapy.Field()
    url =  scrapy.Field()

