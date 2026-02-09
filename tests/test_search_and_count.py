from src.search_and_count import search_operation, process_bank_operations


def test_search_operation():
    """Тест поиска транзакций"""
    transactions = [
        {'description': 'Перевод организации', 'amount': 100},
        {'description': 'Оплата услуг', 'amount': 200},
        {'description': 'Перевод клиенту', 'amount': 300}
    ]

    result = search_operation(transactions, 'Перевод')

    # Проверяем, что нашлось 2 транзакции с "Перевод"
    assert len(result) == 2
    # Проверяем, что в результатах действительно есть "Перевод" в описании
    assert 'Перевод' in result[0]['description']
    assert 'Перевод' in result[1]['description']


def test_process_bank_operations():
    """Тест подсчета операций по категориям"""
    transactions = [
        {'description': 'Перевод организации'},
        {'description': 'Оплата услуг'},
        {'description': 'Перевод клиенту'},
        {'description': 'Покупка товаров'},
        {'description': 'Перевод между счетами'}
    ]

    categories = ['Перевод', 'Оплата', 'Покупка']
    result = process_bank_operations(transactions, categories)

    # Проверяем, что функция возвращает словарь
    assert isinstance(result, dict)
    # Проверяем правильность подсчета
    assert result['Перевод'] == 3
    assert result['Оплата'] == 1
    assert result['Покупка'] == 1
