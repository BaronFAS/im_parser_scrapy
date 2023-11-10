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
