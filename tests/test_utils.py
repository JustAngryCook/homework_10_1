from src.utils import load_transaction
from unittest.mock import patch


def test_file_not_found():
    """Тест случая, когда файл не существует"""
    with patch('os.path.exists', return_value=False) as mock_exists:
        result = load_transaction("non_existent.json")

        mock_exists.assert_called_once_with("non_existent.json")
        assert result == []  # Должен вернуть пустой список
