import scrapy

from im_parser.constants import META


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'

    def start_requests(self):
        '''Паук для проверки работы прокси.'''
        url = 'http://icanhazip.com'
        yield scrapy.Request(
            url, callback=self.parse,
            meta=META
        )

    def parse(self, response):
        '''Пишет в логи ip c которого был запрос.'''
        self.log('Ответ сервера: %s' % response.text)
