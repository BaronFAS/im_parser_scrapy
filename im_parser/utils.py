import re

from im_parser.constants import RE_TITLE, SPICE, EMPTY_STRING


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
