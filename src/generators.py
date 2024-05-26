def filter_by_currency(transactions, currency):
    """
    Принимает список транзакций; возвращает итератор,
    который выдает по очереди операции в заданной валюте.
    :param transactions:
    :param currency:
    :yield:
    """
    for transaction in transactions:
        if transaction["operationAmount"]["currency"]["code"] == currency:
            yield transaction["id"]


def transaction_descriptions(transactions):
    """
    Принимает список словарей;
    возвращает описание каждой операции по очереди.
    :param transactions:
    :yield:
    """
    for transaction in transactions:
        yield transaction["description"]


def card_number_generator(start, stop):
    """
    Генератор номеров банковских карт
    в формате XXXX XXXX XXXX XXXX
    :param start:
    :param stop:
    :yield:
    """
    for num in range(start, stop + 1):
        num_to_str = str(num)
        full_number = num_to_str.zfill(16 - len(num_to_str))
        yield f"{full_number[:4]} {full_number[4:8]} {full_number[8:12]} {full_number[-4:]}"
