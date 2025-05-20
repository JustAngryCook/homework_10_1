def get_mask_card_number(number: int) -> str:
    """функция принимает номер банковской карты и маскирует его"""
    numbers = str(number)
    return (f"{numbers[0:4]} {numbers[4:6]}** **** {numbers[12:]}")


def get_mask_account(number: int) -> str:
    """функция принимает номер счета и маскирует его"""
    numbers = str(number)
    return (f"**{numbers[-4:]}")
