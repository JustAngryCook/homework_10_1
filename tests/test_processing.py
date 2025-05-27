from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_status(list_dict: list, list_dict_result: list) -> None:
    """Тест фильтрации по статусу 'EXECUTED'"""
    assert filter_by_state(list_dict) == list_dict_result


def test_sort_by_date(list_dict: list, list_dict_date_sort_result: list) -> None:
    """Тест фильтрации по дате в порядке убывания"""
    assert sort_by_date(list_dict) == list_dict_date_sort_result
