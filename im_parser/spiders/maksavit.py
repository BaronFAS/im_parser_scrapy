import scrapy
import re
from typing import Dict
from datetime import datetime as dt
from im_parser.constants import (
    DOMAIN_NAME, START_URL, RU, XPATH_PAGE_URL, GET_PART_URL, RE_GET_NUMBER,
    XPATH_TITLE,
)
from im_parser.utils import title_split_string


class MaksavitSpider(scrapy.Spider):
    name = DOMAIN_NAME
    page_index = 700
    allowed_domains = [DOMAIN_NAME + RU]
    start_urls = [START_URL]

    def parse(self, response):
        product_page_urls = response.xpath(XPATH_PAGE_URL).extract()
        for link in product_page_urls:
            yield response.follow(link, self.parse_product)

        next_page = f'{START_URL}{GET_PART_URL}{self.page_index}'
        self.page_index += 1
        yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response) -> Dict[str, str]:
        product_id = re.search(RE_GET_NUMBER, response.url)
        product_title = response.xpath(XPATH_TITLE).extract()[0]
        title_name, volume_product = title_split_string(product_title)
        data = {
            'timestamp': dt.now().timestamp(),
            'RPC': product_id.group(),
            'url': response.url,
            'title': f'{title_name}, {volume_product}'
        }
        yield data
