from src.generators import transactions_by_currency, descriptions, card_number_generator

def test_transactions_usd(transactions, currency='USD'):
    expected = [939719570, 142264268, 895315941]
    result = list(transactions_by_currency(transactions, currency))
    assert result == expected

def test_transactions_rub(transactions, currency='RUB'):
    expected = [873106923, 594226727]
    result = list(transactions_by_currency(transactions, currency))
    assert result == expected

def test_descriptions(transactions):
    expected = [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]
    result = list(descriptions(transactions))
    assert result == expected

def test_card_number_generator():
    expected = [
        '0000 0000 0000 0001',
        '0000 0000 0000 0002',
        '0000 0000 0000 0003',
        '0000 0000 0000 0004',
        '0000 0000 0000 0005',
    ]
    result = list(card_number_generator(1, 5))
    assert result == expected
