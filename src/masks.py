import os


def card_mask(card_number: str) -> str:
    """
    Возвращает маску карты
    :param card_number:
    :return:
    """
    return f"{card_number[:4]} {card_number[5:7]}** **** {card_number[12:]}"


def account_mask(account_number: str) -> str:
    """
    Возвращает маску счета
    :param account_number:
    :return:
    """
    return f"**{account_number[-4:]}"
