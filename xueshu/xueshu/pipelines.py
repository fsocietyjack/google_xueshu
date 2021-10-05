# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv


class XueshuPipeline:
    def process_item(self, item, spider):
        print('----', list(item.values())[0])
        with open('./data2.csv', 'a', encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerows(list(item.values())[0])
        # return item
