import pandas as pd
from typing import List, Dict, Any


def read_transactions(path: str) -> List[Dict[str, Any]]:
    """Чтение CSV с помощью pandas"""
    try:
        df = pd.read_csv(path, encoding='utf-8', delimiter=';', skip_blank_lines=True)

        df = df.dropna(how='all')

        # Конвертация в список словарей
        transactions = df.to_dict('records')
        return transactions

    except Exception as e:
        print(f"Ошибка: {e}")
        return []


def read_transactions_from_excel(path: str, sheet_name: str = 0) -> List[Dict[str, Any]]:
    """Чтение Excel файла (.xlsx) с помощью pandas"""
    try:
        # Чтение Excel файла
        df = pd.read_excel(path, sheet_name=sheet_name, engine='openpyxl')

        # Конвертация в список словарей
        transactions = df.to_dict('records')
        return transactions

    except FileNotFoundError:
        print(f"Файл не найден: {path}")
        return []
    except Exception as e:
        print(f"Ошибка при чтении Excel файла {path}: {e}")
        return []
