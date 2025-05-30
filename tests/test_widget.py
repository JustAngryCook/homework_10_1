from src.widget import mask_account_card, get_date
import pytest


@pytest.mark.parametrize("number, masked_number", [
    ("Карта 1234567891234", "Карта 1234 56** **** 4"),
    ("Карта 123456789123456", "Карта 1234 56** **** 456"),
    ("Карта 123456789123456789", "Карта 1234 56** **** 456789"),
    ("Карта 1234567891234567890", "Карта 1234 56** **** 4567890"),
    ("Счет 64686473678894779589", "Счет **9589")
])
def test_mask_account_card_lenght(number: str, masked_number: str) -> None:
    """Тестирование для нестандартной длины номера карты"""
    assert mask_account_card(number) == masked_number


def test_get_date_correctly(date_time: str) -> None:
    """Тестируем корректность преобразования формата даты"""
    assert get_date(date_time) == "11.03.2024"
