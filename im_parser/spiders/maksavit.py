import scrapy

from scrapy.http import Request, Response
from typing import Dict, Generator
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
    XPATHS_LIST,
    EMPTY_STRING,
    XPATH_METADATA,
    XPATH_METADATA_H3,
    XPATH_TEXT,
    XPATH_SIB_TEXT,
    BRAND,
    ORIGINAL,
    CURRENT,
    DECSRIPTION_KEY,
    DECSRIPTION_VALUE,
    MARKETING_TAGS,
    SECTION,
    TIMESTAMP,
    RPC,
    URL,
    TITLE,
    PRICE_DATA,
    SALE_TAG,
    STOCK,
    IN_STOCK,
    COUNT,
    ASSETS,
    MAIN_IMAGE,
    SET_IMAGE,
    VIEW360,
    VIDEO,
    METADATA,
    VARIANTS,
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

    def parse(self, response: Response) -> Generator[Request, None, None]:
        product_page_urls = response.xpath(XPATH_PAGE_URL).extract()
        for link in product_page_urls:
            yield response.follow(link, self.parse_product)

        next_page = f'{START_URL}{GET_PART_URL}{self.page_index}'
        self.page_index += 1
        yield response.follow(next_page, callback=self.parse)

    def parse_product(self, response: Response) -> Dict[str, str]:
        product_id = get_number_from_string(response.url)
        product_title = response.xpath(XPATH_TITLE).extract_first()
        title_name, volume_product = title_split_string(product_title)

        extracted_data_list = {
            key: strip_space(response.xpath(value).extract())
            for key, value in XPATHS_LIST.items()
        }
        extracted_data = {
            key: response.xpath(value).extract_first()
            for key, value in XPATHS.items()
        }

        brand = extracted_data[BRAND]

        original = extracted_data[ORIGINAL]
        current = extracted_data[CURRENT]
        if current:
            current = float(get_number_from_string(current))
        if current and original:
            original = float(get_number_from_string(original))
            sale_tag = discount_percentage_calc(current, original)

        metadata = {}
        description_key = extracted_data[DECSRIPTION_KEY]
        description_value = extracted_data[DECSRIPTION_VALUE]
        if description_key and description_value:
            metadata[description_key] = description_value

            metadata_body = {}
            for div in response.xpath(XPATH_METADATA):
                for h3 in div.xpath(XPATH_METADATA_H3):
                    key = h3.xpath(XPATH_TEXT).extract_first()
                    value = (
                        h3.xpath(XPATH_SIB_TEXT).extract_first()
                        or EMPTY_STRING
                    ).strip()
                    metadata_body[key] = value
            metadata.update(metadata_body)
        sale_tag = (f'Скидка {sale_tag}%' if original else EMPTY_STRING,)
        data = {
            TIMESTAMP: dt.now().timestamp(),
            RPC: product_id,
            URL: response.url,
            TITLE: f'{title_name}, {volume_product}',
            MARKETING_TAGS: extracted_data_list[MARKETING_TAGS],
            BRAND: brand.strip() if brand else EMPTY_STRING,
            SECTION: extracted_data_list[SECTION][:SECTION_ONLY],
            PRICE_DATA: {
                CURRENT: original if current == original else current,
                ORIGINAL: original if original else current,
                SALE_TAG: sale_tag,
            },
            STOCK: {
                IN_STOCK: True if extracted_data_list[IN_STOCK] else False,
                COUNT: 0,
            },
            ASSETS: {
                MAIN_IMAGE: extracted_data[MAIN_IMAGE],
                SET_IMAGE: [EMPTY_STRING],
                VIEW360: [EMPTY_STRING],
                VIDEO: [EMPTY_STRING],
            },
            METADATA: metadata,
            VARIANTS: 0,
        }
        yield data
