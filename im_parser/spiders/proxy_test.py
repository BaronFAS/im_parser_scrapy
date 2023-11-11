from typing import Generator

import scrapy
from scrapy.http import Request, Response

from im_parser.constants import META


class ProxyTestSpider(scrapy.Spider):
    name = 'proxy_test'

    def start_requests(self) -> Generator[Request, None, None]:
        """Паук для проверки работы прокси."""
        url = 'http://icanhazip.com'
        yield scrapy.Request(
            url, callback=self.parse,
            meta=META
        )

    def parse(self, response: Response) -> None:
        """Пишет в логи ip c которого был запрос."""
        self.log('Ответ сервера: %s' % response.text)
