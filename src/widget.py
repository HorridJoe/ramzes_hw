from masks import card_mask
from masks import account_mask

def masking_func(str_to_mask: str) -> str:

    joined_string = str_to_mask.replace(' ', '')

    if joined_string.startswith('Счет'):
        return account_mask(joined_string[-20:])
    else:
        return card_mask(joined_string[-16:])
