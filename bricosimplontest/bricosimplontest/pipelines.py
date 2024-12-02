# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class BricosimplontestPipeline:
    def process_item(self, item, spider):
        if 'prix' in item:

            item['prix'] = item['prix'].replace('\u202f€',' ').strip()

        return item