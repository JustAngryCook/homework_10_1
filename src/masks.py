import logging
import os

log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'masks.log')

masks_logger = logging.getLogger('masks')
file_handler = logging.FileHandler(log_file, mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(name)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
masks_logger.addHandler(file_handler)
masks_logger.setLevel(logging.DEBUG)


def get_mask_card_number(number: str) -> str:
    """функция принимает номер банковской карты и маскирует его"""
    try:

        masks_logger.debug(f"Начало маскирования номера карты: {number}")
        numbers = str(number)
        if len(numbers) != 16:
            error_msg = f"Некорректная длина номера карты: ожидается 16, получено {len(numbers)}"
            masks_logger.error(error_msg)
            raise ValueError(error_msg)

        if not numbers.isdigit():
            error_msg = f"Номер карты содержит нецифровые символы: {number}"
            masks_logger.error(error_msg)
            raise ValueError(error_msg)

        masks_logger.info("Номер карты успешно замаскирован")
        return (f"{numbers[0:4]} {numbers[4:6]}** **** {numbers[12:]}")

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировании карты {number}: {str(e)}")
        raise


def get_mask_account(number: str) -> str:
    """функция принимает номер счета и маскирует его"""
    try:
        masks_logger.debug(f"Начало маскирования номера счета: {number}")
        numbers = str(number)
        if len(numbers) < 4:
            error_msg = f"Номер счета слишком короткий: минимально 4 символа, получено {len(numbers)}"
            masks_logger.error(error_msg)
            raise ValueError(error_msg)

        if not numbers.isdigit():
            error_msg = f"Номер счета содержит нецифровые символы: {number}"
            masks_logger.error(error_msg)
            raise ValueError(error_msg)
        masks_logger.info("Номер счета успешно замаскирован")
        return (f"**{numbers[-4:]}")

    except Exception as e:
        masks_logger.error(f"Ошибка при маскировании счета {number}: {str(e)}")
        raise
