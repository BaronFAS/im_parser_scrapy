from datetime import datetime as dt
from typing import Dict, Generator

import scrapy
from scrapy.http import Request, Response

from im_parser.constants import (ASSETS, BRAND, COUNT, CURRENT,
                                 DECSRIPTION_KEY, DECSRIPTION_VALUE,
                                 DOMAIN_NAME, DOMAIN_URL, EMPTY_STRING,
                                 GET_PART_URL, IN_STOCK, MAIN_IMAGE,
                                 MARKETING_TAGS, META, METADATA, ORIGINAL,
                                 PARSE_ERROR, PATH_LIST, PRICE_DATA, REGION,
                                 RPC, SALE_TAG, SECTION, SECTION_ONLY,
                                 SET_IMAGE, START_PAGE_INDEX, STOCK, TIMESTAMP,
                                 TITLE, URL, VARIANTS, VIDEO, VIEW360,
                                 XPATH_METADATA, XPATH_METADATA_H3,
                                 XPATH_PAGE_URL, XPATH_SIB_TEXT, XPATH_TEXT,
                                 XPATH_TITLE, XPATHS, XPATHS_LIST, ZERO,
                                 DOMAIN)
from im_parser.items import ScrapyItem
from im_parser.utils import (discount_percentage_calc, get_number_from_string,
                             strip_space, title_split_string)


class MaksavitSpider(scrapy.Spider):
    name = DOMAIN_NAME
    page_index = START_PAGE_INDEX
    allowed_domains = [DOMAIN_URL]

    def start_requests(self) -> Generator[Request, None, None]:
        """Запускает пасинг со страницы каталога."""
        for path in PATH_LIST:
            yield scrapy.Request(
                url=DOMAIN + REGION + path,
                callback=self.parse,
                meta=META,
            )

    def parse(self, response: Response) -> Generator[Request, None, None]:
        """Собирает со страниц катлога ссылки на страницы товара."""
        if response.status != 200:
            self.log(PARSE_ERROR.format(
                status=response.status,
                url=response.url),
            )
        product_page_urls = response.xpath(XPATH_PAGE_URL).extract()
        for link in product_page_urls:
            yield response.follow(link, self.parse_product)
        url = response.url.split('?')[ZERO]
        next_page = f'{url}{GET_PART_URL}{self.page_index}'
        self.page_index += 1
        yield response.follow(next_page, callback=self.parse, meta=META,)

    def parse_product(self, response: Response) -> Dict[str, str]:
        """Собирает информацию о товарах."""
        if response.status != 200:
            self.log(PARSE_ERROR.format(
                status=response.status,
                url=response.url)
            )
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
                COUNT: ZERO,
            },
            ASSETS: {
                MAIN_IMAGE: DOMAIN_URL + extracted_data[MAIN_IMAGE],
                SET_IMAGE: [EMPTY_STRING],
                VIEW360: [EMPTY_STRING],
                VIDEO: [EMPTY_STRING],
            },
            METADATA: metadata,
            VARIANTS: ZERO,
        }
        yield ScrapyItem(data)
