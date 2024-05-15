from masks import card_mask
from masks import account_mask
from datetime import datetime

def masking_func(str_to_mask: str) -> str:

    joined_string = str_to_mask.replace(' ', '')

    if joined_string.startswith('Счет'):
        return account_mask(joined_string[-20:])
    else:
        return card_mask(joined_string[-16:])


def return_date(datetime_input: str) -> str:
     parsed_date = datetime.strptime('2018-07-11T02:26:18.671407',
                                    '%Y-%m-%dT%H:%M:%S.%f')
     return datetime.strftime(parsed_date, '%d.%m.%Y')
