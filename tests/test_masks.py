from src.masks import get_mask_card_number, get_mask_account
import pytest


def test_get_mask_card_number_masked(card_number: str) -> None:
    """Тестирование правильности маскировки номера карты"""
    assert get_mask_card_number(card_number) == "1234 56** **** 5678"


@pytest.mark.parametrize("number, masked_number", [
    (1234567891234, "1234 56** **** 4"),
    (123456789123456, "1234 56** **** 456"),
    (123456789123456789, "1234 56** **** 456789"),
    (1234567891234567890, "1234 56** **** 4567890")
])
def test_get_mask_card_number_length(number: str, masked_number: str) -> None:
    """Тестирование для нестандартной длины номера карты"""
    assert get_mask_card_number(number) == masked_number


def test_get_mask_account_masked(account_number: str) -> None:
    """Тестирование правильности маскировки номера счета"""
    assert get_mask_account(account_number) == "**4305"
