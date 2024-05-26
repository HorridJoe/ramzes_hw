def filter_by_currency(transactions, currency):
    '''
    Принимает список транзакций; возвращает итератор,
    который выдает по очереди операции в заданной валюте.
    :param transactions:
    :param currency:
    :yield:
    '''
    for transaction in transactions:
        if transaction['operationAmount']['currency']['name'] == currency:
            yield transaction['id']

def descriptions(transactions):
    pass

def card_number_generator(start, stop):
    pass



