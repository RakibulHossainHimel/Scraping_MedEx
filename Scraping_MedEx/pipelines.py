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
      raw_html= item["Indications"]
      
    # Step 1: Replace <br> tags with newline
      raw_html = raw_html.replace("<br>", "\n").replace("<br/>", "\n")

        # Step 2: Remove HTML tags
      text = remove_tags(raw_html)

    # Step 3: Unescape HTML entities and strip extra spaces
      clean_text = html.unescape(text).strip()
      item["Indications"] = clean_text
      return item
