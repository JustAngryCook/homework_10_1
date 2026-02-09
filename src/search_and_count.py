import re
from typing import List, Dict, Any


def search_operation(data: List[Dict[str, Any]], search: str) -> List[Dict[str, Any]]:
    """Фильтрует операции по заданному слову"""
    if not data or not search:
        return []

    result = []
    pattern = re.compile(re.escape(search), re.IGNORECASE)

    for transaction in data:
        description = transaction.get('description', '')
        if pattern.search(description):
            result.append(transaction)

    return result


def process_bank_operations(data: List[Dict[str, Any]], categories: List[str]) -> Dict[str, int]:
    """Подсчитывает количество операций по заданным категориям"""
    if not data or not categories:
        return {}

    # Создаем словарь для подсчета
    category_count = {category: 0 for category in categories}

    for transaction in data:
        description = transaction.get('description', '').lower()
        for category in categories:
            if category.lower() in description:
                category_count[category] += 1

    return category_count
