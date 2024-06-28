import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("EXCHANGE_RATE_DATA_API_KEY")
headers = {"apikey": API_KEY}


def ruble_exchange_rate(currency: str) -> float:
    """Принимает название валюты и возвращает ее курс к рублю на текущий момент"""
    response = requests.get(
        f"https://api.apilayer.com/fixer/latest?base={currency.upper()}&symbols=RUB", headers=headers
    )
    return float(response.json()["rates"]["RUB"])