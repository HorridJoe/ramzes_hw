from src.masks import card_mask
from src.masks import account_mask
from datetime import datetime


def masking_func(str_to_mask: str) -> str:
    """
    Возвращает маску карты либо счёта
    :param str_to_mask:
    :return:
    """
    joined_string = str_to_mask.replace(" ", "")
    if joined_string.startswith("Счет"):
        return f'{str_to_mask[:-20]}{account_mask(joined_string[-20:])}'
    else:
        return f'{str_to_mask[:-16]}{card_mask(joined_string[-16:])}'


def return_date(datetime_input: str) -> str:
    """
    Преобразует переданную строку в обьект даты и времени,
    извлекает из него дату в привычном формате
    :param datetime_input:
    :return:
    """
    parsed_date = datetime.strptime(datetime_input, "%Y-%m-%dT%H:%M:%S.%f")
    return datetime.strftime(parsed_date, "%d.%m.%Y")
