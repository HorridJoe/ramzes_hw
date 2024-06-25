import json

import requests


def transactions_readout(transactions_input: str) -> list:
    '''
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param transactions_input:
    :return:
    '''
    try:
        with open(transactions_input) as file:
            return json.load(file)
    except LookupError:
        return []
    except ValueError:
        return []