import scrapy
from Kenh14.items import Kenh14Item

class Kenh14dataSpider(scrapy.Spider):
    name = "Kenh14Data"
    allowed_domains = ["kenh14.vn"]
    start_urls = ["https://kenh14.vn"]
    
    def start_requests(self):
        yield scrapy.Request(url='https://kenh14.vn/', callback=self.parse)

    def parse(self, response):
        ArticleLists = response.xpath('///*[@id="admWrapsite"]/div[2]/div[3]/div[1]/div[1]/div/div[2]/div/div[4]/div/div[2]/div[2]/div[1]/a/@href').getall()
        for Articlek14items in ArticleLists:
            k14item = k14item()
            k14item['URL'] = response.urljoin(Articlek14items)
            request = scrapy.Request(url = response.urljoin(Articlek14items), callback=self.parseCourseDetailPage)
            request.meta['articledata'] = k14item
            yield request
    
    def parsearticlepage(self, response):
        k14item = response.meta['articledata']
        k14item['Title'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[1]/h1))').get()
        k14item['Consult'] = response.xpath('//*[@id="admWrapsite"]/div[2]/div[3]/div/div[3]/div[1]/div/ul/li[1]/a/@title').get()
        k14item['AuthorName'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[1]/div[2]/span[1]))').get()
        k14item['DateTime'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[1]/div[2]/span[3]]))').get()
        k14item['Intro'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[2]/h2))').get()
        k14item['Paragraph'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[2]/div[5]/p[1]))').get()
        k14item['Picture'] = response.xpath('normalize-space(string(//*[@id="k14-detail-content"]/div[2]/div/div/div[1]/div[2]/div[6]/div[2]/div/figure[1]/a/img/@src))').get()
        k14item['Sponsor'] = response.xpath('normalize-space(//*[@id="adx_sponor_11_3khv39j"]/text()))').get()
        k14item['Source'] = response.xpath('normalize-space(string(//*[@id="urlSourceKenh14"]/a/span[1]))').get()
        yield k14item    