import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

API_KEY = os.getenv('EXCHANGE_RATE_DATA_API_KEY')

def ruble_exchange_rate(currency: str) -> float | None:
    '''
    Возвращает актуальный курс рубля к заданной валюте
    с помощью внешнего API
    :param currency:
    :return:
    '''

    # параметры запроса
    url = f"https://api.apilayer.com/exchangerates_data/latest?&base={currency}"
    headers = {"apikey": {API_KEY}}

    # запрос к API
    response = requests.get(url, headers=headers)

    # вывод статус-кода
    status_code = response.status_code
    print(f"Статус-код: {status_code}")

    # проверяем успешность запроса
    if status_code == 200:
        response_text = json.loads(response.text)
        return response_text["rates"]["RUB"]
    else:
        print(f"Запрос не был успешным. Возможная причина: {response.reason}")
        return None
