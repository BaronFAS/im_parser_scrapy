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
RE_GET_NUMBER = r'\d+'
# Регулярное выражение для выбора числа из строки
XPATH_TITLE = '//h1[@class="product-top__title"]/text()'
XPATH_MARKETING_TAG = '//div[contains(@class, "product-picture")]//div[contains(@class, "badge-discount")]/text()' # noqa
XPATH_BRAND = '//a[contains(@class, "product-info__brand-value")]/text()'
XPATH_SECTION = '//ul[contains(@class, "breadcrumbs")]//span[@itemprop="name"]/text()' # noqa
SECTION_ONLY = -1

# utils.py
RE_TITLE = r"(.*?)(\d+[.,]?\d*?\s*(?:мл|гр))(.*)"
# Регулярное выражение для поиска обьема продукта в строке title
SPICE = ' '
EMPTY_STRING = ''
