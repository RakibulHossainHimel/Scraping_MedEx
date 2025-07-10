# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from w3lib.html import remove_tags
import html

class ScrapingMedexPipeline:
    def process_item(self, item, spider):
      item["Unit_Price_BDT"] = float(item["Unit_Price_BDT"].replace('৳', '').replace(',', '').strip()) 
      
      return item
