def filter_by_state(list_of_dictionaries: list[dict], state: str = "EXECUTED") -> list[dict]:
    """функция принимает список словарей и возвращает словари в соответствии со значением state"""
    new_dict = []
    for d in list_of_dictionaries:
        if d.get("state") == state:
            new_dict.append(d)
    return new_dict
