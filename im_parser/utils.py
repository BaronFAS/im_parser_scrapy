import re


def title_split_string(product_title):
    match = re.search(r"(.*?)(\d+[.,]?\d*?\s*(?:мл|гр))(.*)", product_title)
    if match:
        title_name, volume_product = (
            match.group(1).strip() + " " + match.group(3).strip().rstrip(),
            match.group(2).strip(),
        )
        title_name = title_name.rstrip()
        volume_product = volume_product or ""
        return title_name, volume_product
    else:
        return product_title, None
