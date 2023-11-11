import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


DOMAIN_NAME = os.getenv('DOMAIN_NAME')
BASE_DIR = Path(__file__).parent

BOT_NAME = "im_parser"
SPIDER_MODULES = ["im_parser.spiders"]
NEWSPIDER_MODULE = "im_parser.spiders"

ROBOTSTXT_OBEY = True

DEFAULT_REQUEST_HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36", # noqa
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", # noqa
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
}

DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 543,
}
PROXY_HOST = os.getenv('212.115.48.49')
PROXY_PORT = os.getenv('5174')
PROXY_USER = os.getenv('user143352')
PROXY_PASS = os.getenv('3h0psg')

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"

FEEDS = {
    (BASE_DIR / 'results/maksavit_%(time)s.json').as_posix(): {
        'format': 'json',
        'fields': (
            'timestamp', 'RPC', 'url', 'title', 'marketing_tags', 'brand',
            'section', 'price_data', 'stock', 'assets', 'metadata', 'variants'
        ),
        'overwrite': True,
    }
}
