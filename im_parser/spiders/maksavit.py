import scrapy


class MaksavitSpider(scrapy.Spider):
    name = "maksavit"
    allowed_domains = ["maksavit.ru"]
    start_urls = ["https://maksavit.ru/"]

    def parse(self, response):
        pass
