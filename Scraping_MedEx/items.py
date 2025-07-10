# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MedicineItem(scrapy.Item):
    Name = scrapy.Field()
    Dosage_Form = scrapy.Field()
    Generic_name = scrapy.Field()
    Strength = scrapy.Field()
    Manufactured_by = scrapy.Field()
    Unit_Price_BDT = scrapy.Field()
    Indications =  scrapy.Field()
