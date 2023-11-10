import re

from im_parser.constants import (
    RE_TITLE, SPICE, EMPTY_STRING, RE_FLOAT_OR_INT
)


def title_split_string(product_title):
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


def strip_space(list_string):
    return [string.strip() for string in list_string]


def get_number_from_string(number):
    return (re.search(RE_FLOAT_OR_INT, number)).group()


def discount_percentage_calc(current, original):
    """Вычислить процент скидки."""
    return round(100 - 100 * current / original, 1)
