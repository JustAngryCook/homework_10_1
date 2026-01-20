import pytest
from unittest.mock import patch, MagicMock


def test_minimal_csv():
    """Тест для CSV reader"""
    with patch('src.reading_transactions_from_databases.pd.read_csv') as mock_read:
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"test": "data"}]
        mock_read.return_value = mock_df

        from src.reading_transactions_from_databases import read_transactions
        result = read_transactions("any.csv")

        assert result == [{"test": "data"}]


def test_minimal_excel():
    """Тест для Excel reader"""
    with patch('src.reading_transactions_from_databases.pd.read_excel') as mock_read:
        mock_df = MagicMock()
        mock_df.to_dict.return_value = [{"excel": "data"}]
        mock_read.return_value = mock_df

        from src.reading_transactions_from_databases import read_transactions_from_excel
        result = read_transactions_from_excel("any.xlsx")

        assert result == [{"excel": "data"}]
