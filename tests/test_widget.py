import pytest
from src.widget import masking_func, return_date


@pytest.mark.parametrize(
    "input_mask, expected",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
        ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
        ("Счет 73654108430135874305", "Счет **4305"),
    ],
)
def test_masking_func(input_mask, expected):
    assert masking_func(input_mask) == expected


@pytest.mark.parametrize(
    "date_str, expected",
    [
        ("2018-07-11T23:26:46.645807", "11.07.2018"),
        ("2019-05-05T02:19:18.671407", "05.05.2019"),
        ("2018-10-03T14:55:11.948575", "03.10.2018"),
    ],
)
def test_return_date(date_str, expected):
    assert return_date((date_str)) == expected
