import json
import os
import logging


log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'utils.log')

utils_logger = logging.getLogger('utils')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)
utils_logger.setLevel(logging.DEBUG)


def load_transaction(json_file: str) -> list:
    """функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        utils_logger.debug(f"Начинаю загрузку файла: {json_file}")

        # Проверяем существование файла
        if not os.path.exists(json_file):
            utils_logger.error(f"Файл {json_file} не найден")
            return []

        # Проверяем, что файл не пустой
        if os.path.getsize(json_file) == 0:
            utils_logger.error(f"Файл {json_file} пустой")
            return []

        with open(json_file, "r", encoding="utf-8") as f:
            data = json.load(f)

            # Проверяем, что данные - это список
            if not isinstance(data, list):
                utils_logger.error(f"Файл {json_file} содержит не список, а {type(data).__name__}")
                return []

            utils_logger.info(f"Успешно загружено {len(data)} транзакций из {json_file}")
            return data

    except json.JSONDecodeError as e:
        utils_logger.error(f"Ошибка декодирования JSON: {e}")
        return []

    except PermissionError as e:
        utils_logger.error(f"Ошибка доступа к файлу: {e}")
        return []

    except UnicodeDecodeError as e:
        utils_logger.error(f"Ошибка кодировки файла: {e}")
        utils_logger.info("Попробуйте сохранить файл в кодировке UTF-8")
        return []

    except Exception as e:
        utils_logger.error(f"Неизвестная ошибка: {e}")
        return []
