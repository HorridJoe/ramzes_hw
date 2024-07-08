import json
import logging
from src.external_api import ruble_exchange_rate

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="logs/utils.log",  # Запись логов в файл
    filemode="w",
)
utils_logger = logging.getLogger(__name__)


def transactions_readout(transactions_input: str) -> list:
    """
    принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях.
    Если файл пустой, содержит не список или не найден, функция возвращает пустой список.
    :param transactions_input:
    :return:
    """
    try:
        with open(transactions_input, "r", encoding="utf-8") as file:
            utils_logger.info("Список транзакций успешно извлечен")
            return json.load(file)
    except FileNotFoundError:
        utils_logger.error("Файл по указанному пути не найден")
        return []
    except ValueError:
        utils_logger.error("Файл по указанному пути не содержит списка транзакций")
        return []


def transaction_sum_in_rubles(transaction: dict):
    """
    Принимает на вход транзакцию и возвращает сумму транзакции в рублях
    :param transaction:
    :return:
    """
    currency = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]

    if currency == "RUB":
        utils_logger.info("Валюта транзакции - рубль; получать курс не нужно")
        return float(amount)
    else:
        utils_logger.info(f"Валюта транзакции - {currency}; возвращена сумма в рублях по актуальному курсу")
        exchange_rate = ruble_exchange_rate(currency)
        return exchange_rate * float(amount)
