import pytest
from unittest.mock import patch, MagicMock
from src.external_api import convertation


# Тест 1: Успешная конвертация USD в RUB
@patch('src.external_api.requests.get')
@patch('src.external_api.os.getenv')
def test_convertation_usd_success(mock_getenv, mock_get):
    """тест на успешную конвертацию USD в RUB"""
    mock_getenv.return_value = 'fake-api-key'

    mock_response = MagicMock()
    mock_response.json.return_value = {
        "success": True,
        "rates": {"RUB": 75.50}
    }
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "100.0",
            "currency": {"code": "USD"}
        }
    }

    result = convertation(transaction)
    assert result == 7550.0
    