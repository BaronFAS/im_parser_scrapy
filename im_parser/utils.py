import re
from typing import Optional, Tuple

from im_parser.constants import EMPTY_STRING, RE_FLOAT_OR_INT, RE_TITLE, SPICE


def title_split_string(product_title: str) -> Tuple[str, Optional[str]]:
    """Раскладывает строку title на части и записывает объем
    (в гр. или мл., если он есть) продукта в конец строки."""
    match = re.search(RE_TITLE, product_title)
    if match:
        title_name, volume_product = (
            match.group(1).strip() + SPICE + match.group(3).strip().rstrip(),
            match.group(2).strip(),
        )
        title_name = title_name.rstrip()
        volume_product = volume_product or EMPTY_STRING
        return title_name, volume_product
    else:
        return product_title, None


def strip_space(list_string: list[str]) -> list[str]:
    """Убирает лишние пробелы."""
    return [string.strip() for string in list_string]


def get_number_from_string(number: str) -> str:
    """Получает из строки число (int или float),
    без приведения к нужному типу данных т.е. строкой."""
    return (re.search(RE_FLOAT_OR_INT, number)).group()


def discount_percentage_calc(current: float, original: float) -> float:
    """Вычисляет процент скидки и округляет до одного знака после запятой."""
    return round(100 - 100 * current / original, 1)
