import os
from unittest.mock import patch
from dotenv import load_dotenv
from src.external_api import ruble_exchange_rate

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_DATA_API_KEY")
headers = {"apikey": API_KEY}


@patch("requests.get")
def test_ruble_exchange_rate(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1717678144,
        "base": "USD",
        "date": "2024-06-25",
        "rates": {"RUB": 89.749374},
    }
    transaction = {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    }
    assert ruble_exchange_rate(transaction) == 89.749374
    mock_get.assert_called_once_with("https://api.apilayer.com/fixer/latest?base=USD&symbols=RUB", headers=headers)
