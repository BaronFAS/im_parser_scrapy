# Парсер интернет магазина

### Автор:
- [Михаил Приселков](https://github.com/BaronFAS)

### Технологии:
- Python 3.11.6
- Scrapy 2.11.0

### Описание проекта ###
Парсер проходит по заданным в константе страницам каталога переходит с них на карточку товара и собирает данные в установленном формате.
На выходе json фаил со списком словарей.

Формат выходных данных для одного товара:

```json
{
    "timestamp": int,
    "RPC": "str",
    "url": "str",
    "title": "str",
    "marketing_tags": ["str"],
    "brand": "str",
    "section": ["str"],
    "price_data": {
        "current": float,
        "original": float,
        "sale_tag": "str"
    },
    "stock": {
        "in_stock": bool,
        "count": int
    },
    "assets": {
        "main_image": "str",
        "set_images": ["str"],
        "view360": ["str"],
        "video": ["str"]
    },
    "metadata": {
        "__description": "str",
        "KEY": "str",
        "KEY": "str",
        "KEY": "str"
    }
    "variants": int,
}
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:BaronFAS/im_parser_scrapy.git
```

Cоздать и активировать виртуальное окружение:

```
python -m venv .venv
```

```
source venv/scripts/activate
```

Установить зависимости из файла requirements.txt

```
pip install -r requirements.txt
```

Обновить pip

```
python -m pip install --upgrade pip
```

Запустить парсер:

```
scrapy crawl maksavit
```

Скачать _json_ файл в папке _results_, каждый новый запуск создает новый файл с временной меткой.