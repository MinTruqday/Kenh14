import scrapy


class Kenh14dataSpider(scrapy.Spider):
    name = "Kenh14Data"
    allowed_domains = ["kenh14.vn"]
    start_urls = ["https://kenh14.vn"]

    def parse(self, response):
        pass
