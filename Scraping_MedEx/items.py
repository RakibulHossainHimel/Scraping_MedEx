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
    #Marketed_by = scrapy.Field()
    Unit_Price_BDT = scrapy.Field()
    IsAntibiotic = scrapy.Field()
    Indications =  scrapy.Field()
    Composition = scrapy.Field()
    Pharmacology = scrapy.Field()
    Dosage_and_Administration = scrapy.Field()
    Interaction = scrapy.Field()
    Contraindications = scrapy.Field()
    Side_Effects = scrapy.Field()
    Pregnancy_and_Lactation = scrapy.Field()
    Precautions_and_Warnings = scrapy.Field()
    pediatric_Uses = scrapy.Field()
    Overdose_Effects = scrapy.Field()
    Therapeutic_Class = scrapy.Field()
    Reconstitution = scrapy.Field()
    Storage_Conditions = scrapy.Field()
    Chemical_Structure = scrapy.Field()
    Common_Questions = scrapy.Field()

