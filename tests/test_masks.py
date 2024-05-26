import pytest
from src.masks import card_mask, account_mask


@pytest.mark.parametrize(
    "card_number, expected",
    [
        ("2223999900003245", "2223 99** **** 3245"),
        ("4852805736395734", "4852 80** **** 5734"),
        ("3842035735485027", "3842 03** **** 5027"),
    ],
)
def test_card_mask(card_number, expected):
    assert card_mask(card_number) == expected


@pytest.mark.parametrize(
    "acc_number, expected",
    [("57305837486958743860", "**3860"),("37586947586736458305", "**8305"), ("29487593759374659374", "**9374")],
)
def test_account_mask(acc_number, expected):
    assert account_mask(acc_number) == expected
