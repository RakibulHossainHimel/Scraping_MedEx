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
        #product['Marketed_by'] = response.xpath("//div[@title='Marketed by']/a/text()").get().strip()
        product['Unit_Price_BDT'] = response.xpath("//div[@class='package-container mt-5 mb-5']/span[2]/text()").get().strip()
        
        #Antibiotic
        product['IsAntibiotic'] = "Yes" if "Antibiotic" in " ".join(t.strip() for t in response.xpath("//div[@class='mb-2']//text()").getall() if t.strip()) else "No"


        #Indications
        if response.xpath("//div[@id='indications']/h3/text()").get()=="Indications":
            Indications_text_list = response.xpath("//div[@id='indications']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Indications_full_text = " ".join([text.strip() for text in Indications_text_list if text.strip()])
            product['Indications'] = Indications_full_text
        else:
            product['Indications'] = ""

        #Composition
        if response.xpath("//div[@id='composition']/h3/text()").get()=="Composition":
            Composition_text_list = response.xpath("//div[@id='composition']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Composition_full_text = " ".join([text.strip() for text in Composition_text_list if text.strip()])
            product['Composition'] = Composition_full_text
        else:
            product['Composition'] = ""
        
        #Pharmacology
        if response.xpath("//div[@id='mode_of_action']/h3/text()").get()=="Pharmacology":
            Pharmacology_text_list = response.xpath("//div[@id='mode_of_action']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Pharmacology_full_text = " ".join([text.strip() for text in Pharmacology_text_list if text.strip()])
            product['Pharmacology'] = Pharmacology_full_text
        else:
            product['Pharmacology'] = ""

        #Dosage & Administration
        if response.xpath("//div[@id='dosage']/h3/text()").get()=="Dosage & Administration":
            Dosage_and_Administration_text_list = response.xpath("//div[@id='dosage']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Dosage_and_Administration_full_text = " ".join([text.strip() for text in Dosage_and_Administration_text_list if text.strip()])
            product['Dosage_and_Administration'] = Dosage_and_Administration_full_text
        else:
            product['Dosage_and_Administration'] = ""

        #Interaction
        if response.xpath("//div[@id='interaction']/h3/text()").get()=="Interaction":
            Interaction_text_list = response.xpath("//div[@id='indications']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Interaction_full_text = " ".join([text.strip() for text in Interaction_text_list if text.strip()])
            product['Interaction'] = Interaction_full_text
        else:
            product['Interaction'] = ""

        #Contraindications
        if response.xpath("//div[@id='contraindications']/h3/text()").get()=="Contraindications":
            Contraindications_text_list = response.xpath("//div[@id='contraindications']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Contraindications_full_text = " ".join([text.strip() for text in Contraindications_text_list if text.strip()])
            product['Contraindications'] = Contraindications_full_text
        else:
            product['Contraindications'] = ""
        
        #Side Effects
        if response.xpath("//div[@id='side_effects']/h3/text()").get()=="Side Effects":
            Side_Effects_text_list = response.xpath("//div[@id='side_effects']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Side_Effects_full_text = " ".join([text.strip() for text in Side_Effects_text_list if text.strip()])
            product['Side_Effects'] = Side_Effects_full_text
        else:
            product['Side_Effects'] = ""

        #Pregnancy & Lactation
        if response.xpath("//div[@id='pregnancy_cat']/h3/text()").get()=="Pregnancy & Lactation":
            Pregnancy_and_Lactation_text_list = response.xpath("//div[@id='pregnancy_cat']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Pregnancy_and_Lactation_full_text = " ".join([text.strip() for text in Pregnancy_and_Lactation_text_list if text.strip()])
            product['Pregnancy_and_Lactation'] = Pregnancy_and_Lactation_full_text
        else:
            product['Pregnancy_and_Lactation'] = ""

        #Precautions & Warnings
        if response.xpath("//div[@id='precautions']/h3/text()").get()=="Precautions & Warnings":
            Precautions_and_Warnings_text_list = response.xpath("//div[@id='precautions']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Precautions_and_Warnings_full_text = " ".join([text.strip() for text in Precautions_and_Warnings_text_list if text.strip()])
            product['Precautions_and_Warnings'] = Precautions_and_Warnings_full_text
        else:
            product['Precautions_and_Warnings'] = ""

        #pediatric Uses
        if response.xpath("//div[@id='pediatric_uses']/h3/text()").get()=="Use in Special Populations":
            pediatric_Uses_text_list = response.xpath("//div[@id='pediatric_uses']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            pediatric_Uses_full_text = " ".join([text.strip() for text in pediatric_Uses_text_list if text.strip()])
            product['pediatric_Uses'] = pediatric_Uses_full_text
        else:
            product['pediatric_Uses'] = ""

        #Overdose Effects
        if response.xpath("//div[@id='overdose_effects']/h3/text()").get()=="Overdose Effects":
            Overdose_Effects_text_list = response.xpath("//div[@id='overdose_effects']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Overdose_Effects_full_text = " ".join([text.strip() for text in Overdose_Effects_text_list if text.strip()])
            product['Overdose_Effects'] = Overdose_Effects_full_text
        else:
            product['Overdose_Effects'] = ""
        
        #Therapeutic Class
        if response.xpath("//div[@id='drug_classes']/h3/text()").get()=="Therapeutic Class":
            Therapeutic_Class_text_list = response.xpath("//div[@id='drug_classes']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Therapeutic_Class_full_text = " ".join([text.strip() for text in Therapeutic_Class_text_list if text.strip()])
            product['Therapeutic_Class'] = Therapeutic_Class_full_text
        else:
            product['Therapeutic_Class'] = ""

        #Reconstitution
        if response.xpath("//div[@id='reconstitution']/h3/text()").get()=="Reconstitution":
            Reconstitution_text_list = response.xpath("//div[@id='reconstitution']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Reconstitution_full_text = " ".join([text.strip() for text in Reconstitution_text_list if text.strip()])
            product['Reconstitution'] = Reconstitution_full_text
        else:
            product['Reconstitution'] = ""
        
        #Storage Conditions
        if response.xpath("//div[@id='storage_conditions']/h3/text()").get()=="Storage Conditions":
            Storage_Conditions_text_list = response.xpath("//div[@id='storage_conditions']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Storage_Conditions_full_text = " ".join([text.strip() for text in Storage_Conditions_text_list if text.strip()])
            product['Storage_Conditions'] = Storage_Conditions_full_text
        else:
            product['Storage_Conditions'] = ""

        #Chemical Structure
        if response.xpath("//div[@id='compound_summary']/h3/text()").get()=="Chemical Structure":
            Chemical_Structure_text_list = response.xpath("//div[@id='compound_summary']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Chemical_Structure_full_text = " ".join([text.strip() for text in Chemical_Structure_text_list if text.strip()])
            product['Chemical_Structure'] = Chemical_Structure_full_text
        else:
            product['Chemical_Structure'] = ""

        #Common_Questions
        if response.xpath("//div[@id='commonly_asked_questions']/h3/text()").get() and 'Common Questions' in response.xpath("//div[@id='commonly_asked_questions']/h3/text()").get():
        
            Common_Questions_text_list = response.xpath("//div[@id='commonly_asked_questions']/following-sibling::div[@class='ac-body'][1]//text()").getall()
            Common_Questions_full_text = " ".join([text.strip() for text in Common_Questions_text_list if text.strip()])
            product['Common_Questions'] = Common_Questions_full_text
        else:
            product['Common_Questions'] = ""


        yield product
