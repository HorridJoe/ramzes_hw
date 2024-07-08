import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(filename)s - %(levelname)s: %(message)s",
    filename="logs/masks.log",
    filemode="w",
)
masks_logger = logging.getLogger(__name__)

def card_mask(card_number: str) -> str:
    """
    Возвращает маску карты
    :param card_number:
    :return:
    """
    masks_logger.info('Возвращена маска введенного номера карты')
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


def account_mask(account_number: str) -> str:
    """
    Возвращает маску счета
    :param account_number:
    :return:
    """
    masks_logger.info('Возвращена маска введенного номера банковского счёта')
    return f"**{account_number[-4:]}"
