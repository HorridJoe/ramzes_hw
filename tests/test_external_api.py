import os
from unittest.mock import patch
from dotenv import load_dotenv
from src.external_api import ruble_exchange_rate

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_DATA_API_KEY")
headers = {"apikey": API_KEY}


@patch("requests.get")
def test_currency_exchange_rate(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1717678144,
        "base": "USD",
        "date": "2024-06-25",
        "rates": {"RUB": 89.749374},
    }
    assert ruble_exchange_rate("USD") == 89.749374
    mock_get.assert_called_once_with("https://api.apilayer.com/fixer/latest?base=USD&symbols=RUB", headers=headers)
