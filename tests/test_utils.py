import pytest
import json

from src.utils import transactions_readout
from src.utils import transaction_sum_in_rubles

from unittest.mock import Mock
from unittest.mock import patch



def test_transactions_readout_ok(transactions):
    input_file = 'test_operations.json'
    result = transactions_readout(input_file)
    expected = transactions
    assert result == expected

def test_transactions_readout_empty():
    input_file = 'test_empty.json'
    result = transactions_readout(input_file)
    expected = []
    assert result == expected

def test_transactions_readout_not_found():
    input_file = 'test_not_found.json'
    result = transactions_readout(input_file)
    assert result == []


def test_transaction_sum_in_rubles_if_usd(mock_ruble_exchange_rate):
    # Задаем возвращаемое значение для mock функции
    mock_ruble_exchange_rate.return_value = 75.0

    transaction = {
    "id": 518707726,
    "state": "EXECUTED",
    "date": "2018-11-29T07:18:23.941293",
    "operationAmount": {
      "amount": "3348.98",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 3152479541115065",
    "to": "Visa Gold 9447344650495960"
  }

    result = transaction_sum_in_rubles(transaction)
    assert result == 251173.5

def test_transaction_sum_in_rubles_if_rub():
    transaction = {
    "id": 407169720,
    "state": "EXECUTED",
    "date": "2018-02-03T14:52:08.093722",
    "operationAmount": {
      "amount": "67011.26",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод с карты на карту",
    "from": "MasterCard 4047671689373225",
    "to": "Maestro 3806652527413662"
    }

    result = transaction_sum_in_rubles(transaction)

    assert result == 67011.26

