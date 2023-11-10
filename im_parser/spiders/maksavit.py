import scrapy
import re
from typing import Dict
from datetime import datetime as dt
from im_parser.constants import (
    DOMAIN_NAME, START_URL, RU, XPATH_PAGE_URL, GET_PART_URL, RE_GET_NUMBER,
    XPATH_TITLE, XPATH_MARKETING_TAG, XPATH_BRAND, XPATH_SECTION,
    SECTION_ONLY,
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
        marketing_tags = response.xpath(XPATH_MARKETING_TAG).extract()
        marketing_tags = [tag.strip() for tag in marketing_tags]
        brand = response.xpath(XPATH_BRAND).extract_first()
        if brand:
            brand = brand.strip()
        section = response.xpath(XPATH_SECTION).extract()
        section = [tag.strip() for tag in section]
        price_data = ''
        data = {
            'timestamp': dt.now().timestamp(),
            'RPC': product_id.group(),
            'url': response.url,
            'title': f'{title_name}, {volume_product}',
            'marketing_tags': marketing_tags,
            'brand': brand,
            'section': section[:SECTION_ONLY],
            'price_data': price_data,
        }
        yield data
