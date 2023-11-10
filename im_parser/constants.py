# spider общие настройки
DOMAIN_NAME = 'maksavit'
RU = '.ru'
START_URL = 'https://' + DOMAIN_NAME + RU + '/novosibirsk/catalog/materinstvo_i_detstvo/detskaya_gigiena/' # noqa
# не забыть добавить
START_PAGE_INDEX = 1


# Парсинг страницы каталога
XPATH_PAGE_URL = '//a[@class="product-card-block__title"]/@href'
GET_PART_URL = '?page='


# Парсинг страницы продукта
XPATH_TITLE = '//h1[@class="product-top__title"]/text()'
XPATH_MARKETING_TAG = '//div[contains(@class, "product-picture")]//div[contains(@class, "badge-discount")]/text()' # noqa
XPATH_BRAND = '//a[contains(@class, "product-info__brand-value")]/text()'
XPATH_SECTION = '//ul[contains(@class, "breadcrumbs")]//span[@itemprop="name"]/text()' # noqa
XPATH_PRICE_CURRENT = '//div[@class="price-box"]//span[@class="price-value"]/text()' # noqa
XPATH_PRICE_ORIGINAL = '//div[@class="price-box"]//div[@class="price-box__old-price"]/text()' # noqa
XPATH_IN_STOCK = '//div[@class="available-count"]'
XPATH_MAIN_IMAGE = '//div[@class="product-picture"]//img/@src'
XPATH_METADATA = '//div[contains(@class, "product-instruction__guide")]'
XPATH_METADATA_H3 = './/h3[@class="desc"]'
XPATH_TEXT = './text()'
XPATH_SIBLING_TEXT = 'following-sibling::text()[1]'
XPATH_DEC_KEY = '//div[contains(@class, "product-instruction")]//h2/text()'
XPATH_DEC_VALUE = '//div[contains(@class, "product-instruction")]//div/text()'

XPATHS = {
    'marketing_tags': XPATH_MARKETING_TAG,
    'brand': XPATH_BRAND,
    'section': XPATH_SECTION,
    'current': XPATH_PRICE_CURRENT,
    'original': XPATH_PRICE_ORIGINAL,
    'in_stock': XPATH_IN_STOCK,
    'main_image': XPATH_MAIN_IMAGE,
    'description_key': XPATH_DEC_KEY,
    'description_value': XPATH_DEC_VALUE,
}

SECTION_ONLY = -1


# utils.py
RE_TITLE = r'(.*?)(\d+[.,]?\d*?\s*(?:мл|гр))(.*)'
# Регулярное выражение для поиска обьема продукта в строке title
SPICE = ' '
EMPTY_STRING = ''
RE_FLOAT_OR_INT = r'(\d*[.,]\d+)|\d+'
# Регулярное выражение для поиска дробного или целого числа
