def filter_by_currency(transactions, currency):
    '''
    Принимает список транзакций; возвращает итератор,
    который выдает по очереди операции в заданной валюте.
    :param transactions:
    :param currency:
    :yield:
    '''
    for transaction in transactions:
        if transaction['operationAmount']['currency']['code'] == currency:
            yield transaction['id']

def transaction_descriptions(transactions):
    '''
    Принимает список словарей;
    возвращает описание каждой операции по очереди.
    :param transactions:
    :yield:
    '''
    for transaction in transactions:
        yield transaction['description']

def card_number_generator(start, stop):
    pass

