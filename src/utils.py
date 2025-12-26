import json
import os


def load_transaction(json_file: str) -> list:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        # Проверяем существование файла
        if not os.path.exists(json_file):
            print(f"Файл {json_file} не найден")
            return []
        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data

    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
        return []

    except PermissionError as e:
        print(f"Ошибка доступа к файлу: {e}")
        return []

    except UnicodeDecodeError as e:
        print(f"Ошибка кодировки файла: {e}")
        print("Попробуйте сохранить файл в кодировке UTF-8")
        return []

    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return []


print(load_transaction("D:/pyton_project/kot/Bank_Card_Project/data/operations.json"))