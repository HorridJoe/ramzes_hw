import json
import requests
from external_api import ruble_exchange_rate


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

def transaction_sum_in_rubles(transaction: dict):
    '''
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях
    :param transaction:
    :return:
    '''
    currency = transaction.get("code")
    amount = transaction.get("amount")

    if currency == "RUB":
        return float(amount)
    else:
        exchange_rate = ruble_exchange_rate(currency)
        return exchange_rate * float(amount)