from im_parser import settings


# spider общие настройки
DOMAIN_NAME = 'maksavit'
RU = '.ru'
DOMAIN_URL = ('https://' + DOMAIN_NAME + RU)
PATH_LIST = (
    '/novosibirsk/catalog/materinstvo_i_detstvo/detskaya_gigiena/',
    # '/catalog/materinstvo_i_detstvo/detskie_aksessuary/',
    # '/catalog/materinstvo_i_detstvo/detskie_podguzniki_i_pelenki/',
)
PARSE_ERROR = 'Ошибка в парсинге {response.status} на {response.url}'
META = {
    'proxy': 'http://%(user)s:%(pass)s@%(host)s:%(port)s' % {
        'user': settings.PROXY_USER,
        'pass': settings.PROXY_PASS,
        'host': settings.PROXY_HOST,
        'port': settings.PROXY_PORT,
    }
}
# не забыть добавить
START_PAGE_INDEX = 1
SPICE = ' '
EMPTY_STRING = ''
ZERO = 0

# Парсинг страницы каталога
XPATH_PAGE_URL = '//a[@class="product-card-block__title"]/@href'
GET_PART_URL = '?page='


# Парсинг страницы продукта
XPATH_TITLE = '//h1[@class="product-top__title"]/text()'
XPATH_MARKETING_TAG = '//div[contains(@class, "product-picture")]//div[contains(@class, "badge-discount")]/text()'  # noqa
XPATH_BRAND = '//a[contains(@class, "product-info__brand-value")]/text()'
XPATH_SECTION = (
    '//ul[contains(@class, "breadcrumbs")]//span[@itemprop="name"]/text()'
)
XPATH_PRICE_CURRENT = (
    '//div[@class="price-box"]//span[@class="price-value"]/text()'
)
XPATH_PRICE_ORIGINAL = (
    '//div[@class="price-box"]//div[@class="price-box__old-price"]/text()'
)
XPATH_IN_STOCK = '//div[@class="available-count"]'
XPATH_MAIN_IMAGE = '//div[@class="product-picture"]//img/@src'
XPATH_METADATA = '//div[contains(@class, "product-instruction__guide")]'
XPATH_METADATA_H3 = './/h3[@class="desc"]'
XPATH_TEXT = './text()'
XPATH_SIB_TEXT = "following-sibling::text()[1]"
XPATH_DEC_KEY = '//div[contains(@class, "product-instruction")]//h2/text()'
XPATH_DEC_VALUE = '//div[contains(@class, "product-instruction")]//div/text()'

# Ключи для словаря data
BRAND = 'brand'
ORIGINAL = 'original'
CURRENT = 'current'
DECSRIPTION_KEY = 'description_key'
DECSRIPTION_VALUE = 'description_value'
MARKETING_TAGS = 'marketing_tags'
SECTION = 'section'
TIMESTAMP = 'timestamp'
RPC = 'RPC'
URL = 'url'
TITLE = 'title'
PRICE_DATA = 'price_data'
SALE_TAG = 'sale_tag'
STOCK = 'stock'
IN_STOCK = 'in_stock'
COUNT = 'count'
ASSETS = 'assets'
MAIN_IMAGE = 'main_image'
SET_IMAGE = 'set_images'
VIEW360 = 'view360'
VIDEO = 'video'
METADATA = 'metadata'
VARIANTS = 'variants'

XPATHS_LIST = {
    MARKETING_TAGS: XPATH_MARKETING_TAG,
    SECTION: XPATH_SECTION,
    IN_STOCK: XPATH_IN_STOCK,
}

XPATHS = {
    BRAND: XPATH_BRAND,
    CURRENT: XPATH_PRICE_CURRENT,
    ORIGINAL: XPATH_PRICE_ORIGINAL,
    MAIN_IMAGE: XPATH_MAIN_IMAGE,
    DECSRIPTION_KEY: XPATH_DEC_KEY,
    DECSRIPTION_VALUE: XPATH_DEC_VALUE,
}

SECTION_ONLY = -1
# Убирает страницу парсинга "из хлебных крпошек"


# utils.py
RE_TITLE = r"(.*?)(\d+[.,]?\d*?\s*(?:мл|гр))(.*)"
# Регулярное выражение для поиска обьема продукта в строке title
RE_FLOAT_OR_INT = r"(\d*[.,]\d+)|\d+"
# Регулярное выражение для поиска дробного или целого числа
