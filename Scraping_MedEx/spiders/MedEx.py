import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from Scraping_MedEx.items import MedicineItem

class MedexSpider(scrapy.Spider):
    name = "MedEx"
    allowed_domains = ["medex.com.bd"]
    start_urls = ["https://medex.com.bd/brands"]
    base_url = "https://medex.com.bd/brands"



    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url,callback=self.parse, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'})
        
    
    custom_settings={
        "AUTOTHROTTLE_ENABKED" : True,
        "DOWNLOAD_DELAY" : 3,
        "CONCURRENT_REQUESTS" : 16
    }

    def parse(self, response):
        for link in response.xpath("//a[@class='hoverable-block']/@href"):
            yield response.follow(link,self.medicine_details)


    def medicine_details(self,response):
        product = MedicineItem()
        product['Name'] = response.xpath("//h1[@class='page-heading-1-l brand']/text()").get().strip()
        product['Dosage_Form'] = response.xpath("//h1[@class='page-heading-1-l brand']/small/text()").get().strip()
        product['Generic_name'] = response.xpath("//div[@title='Generic Name']/a/text()").get().strip()
        product['Strength'] = response.xpath("//div[@title='Strength']/text()").get().strip()
        product['Manufactured_by'] = response.xpath("//div[@title='Manufactured by']/a/text()").get().strip()
        product['Unit_Price_BDT'] = response.xpath("//div[@class='package-container mt-5 mb-5']/span[2]/text()").get().strip()
        if response.xpath("//div[@id='indications']/h3/text()").get()=="Indications":
            product['Indications'] = response.xpath("//div[@class='ac-body']").get().strip()
        

        yield product
