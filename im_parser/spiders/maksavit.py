import scrapy
from typing import Dict
from datetime import datetime as dt
from im_parser.constants import (
    DOMAIN_NAME,
    START_URL,
    RU,
    XPATH_PAGE_URL,
    GET_PART_URL,
    XPATH_TITLE,
    SECTION_ONLY,
    XPATHS,
    EMPTY_STRING,
)
from im_parser.utils import (
    title_split_string,
    strip_space,
    discount_percentage_calc,
    get_number_from_string,
)


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
        product_id = get_number_from_string(response.url)
        product_title = response.xpath(XPATH_TITLE).extract()[0]
        title_name, volume_product = title_split_string(product_title)

        extracted_data = {
            key: strip_space(response.xpath(xpath).extract())
            for key, xpath in XPATHS.items()
        }

        brand = extracted_data['brand']
        if brand:
            brand = brand[0]

        original = extracted_data['original']
        current = extracted_data['current']
        if current:
            current = float(get_number_from_string(current[0]))
        if original:
            original = float(get_number_from_string(original[0]))
            sale_tag = discount_percentage_calc(current, original)
        data = {
            'timestamp': dt.now().timestamp(),
            'RPC': product_id,
            'url': response.url,
            'title': f'{title_name}, {volume_product}',
            'marketing_tags': extracted_data['marketing_tags'],
            'brand': brand,
            'section': extracted_data['section'][:SECTION_ONLY],
            'price_data': {
                'current': current,
                'original': original,
                'sale_tag': f'Скидка {sale_tag}%' if original else '',
            },
            'stock': {
                'in_stock': True if extracted_data['in_stock'] else False,
                'count': 0
            },
            'assets': {
                'main_image': extracted_data['main_image'],
                "set_images": [EMPTY_STRING],
                "view360": [EMPTY_STRING],
                "video": [EMPTY_STRING]
            },
        }
        yield data
