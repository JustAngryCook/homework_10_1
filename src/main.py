import json
from typing import List, Dict, Any

# Импортируем функции чтения файлов
from reading_transactions_from_databases import read_transactions, read_transactions_from_excel
from search_and_count import search_operation
from generators import filter_by_currency
from processing import filter_by_state, sort_by_date


def load_json_file(filepath: str) -> List[Dict[str, Any]]:
    """Загружает данные из JSON файла"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Ошибка при чтении JSON: {e}")
        return []


def get_file_choice():
    """Выбор типа файла"""
    while True:
        print("\nВыберите тип файла:")
        print("1. JSON файл")
        print("2. CSV файл")
        print("3. XLSX файл")

        choice = input("Ваш выбор (1-3): ").strip()

        if choice in ['1', '2', '3']:
            return choice
        print("Неверный выбор. Введите 1, 2 или 3.")


def load_transactions(choice: str) -> List[Dict[str, Any]]:
    """Загружает транзакции в зависимости от выбора"""

    if choice == '1':  # JSON
        filepath = input("Введите путь к JSON файлу (или нажмите Enter для data/transactions.json): ").strip()
        if not filepath:
            filepath = r"D:\pyton_project\kot\Bank_Card_Project\data\operations.json"
        return load_json_file(filepath)

    elif choice == '2':  # CSV
        filepath = input("Введите путь к CSV файлу (или нажмите Enter для data/transactions.csv): ").strip()
        if not filepath:
            filepath = r"D:\pyton_project\kot\Bank_Card_Project\data\transactions.csv"
        return read_transactions(filepath)

    else:  # XLSX
        filepath = input("Введите путь к XLSX файлу (или нажмите Enter для data/transactions.xlsx): ").strip()
        if not filepath:
            filepath = r"D:\pyton_project\kot\Bank_Card_Project\data\transactions_excel.xlsx"
        return read_transactions_from_excel(filepath)


def get_status():
    """Получает статус транзакций"""
    while True:
        status = input("\nВведите статус (executed/canceled/pending): ").strip().lower()
        if status in ['executed', 'canceled', 'pending']:
            return status
        print("Неверный статус. Попробуйте снова.")


def ask_yes_no(question):
    """Простой вопрос Да/Нет"""
    answer = input(f"\n{question} (да/нет): ").strip().lower()
    return answer in ['да', 'д', 'yes', 'y']


def simple_format(transaction):
    """Простое форматирование транзакции"""
    date = transaction.get('date', '')[:10]  # Берем только дату
    desc = transaction.get('description', '')

    # Пробуем разные варианты ключей для суммы
    amount = transaction.get('amount')
    if amount is None:
        amount = transaction.get('Amount')
    if amount is None:
        # Попробуем найти вложенную структуру для JSON
        operation_amount = transaction.get('operationAmount', {})
        if isinstance(operation_amount, dict):
            amount = operation_amount.get('amount')

    # Если amount все еще None, ставим 0
    if amount is None:
        amount = 0

    # Форматируем сумму (убираем лишние знаки после запятой если это float)
    try:
        if isinstance(amount, float):
            amount_str = f"{amount:.2f}"
        else:
            amount_str = str(amount)
    except:
        amount_str = str(amount)

    return f"{date} {desc} - {amount_str}"


def main():
    """Основная функция программы"""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")

    # 1. Выбор и загрузка файла
    choice = get_file_choice()
    transactions = load_transactions(choice)

    if not transactions:
        print("Не удалось загрузить транзакции. Проверьте путь к файлу.")
        return

    print(f"Загружено {len(transactions)} транзакций.")

    # 2. Фильтрация по статусу
    status = get_status()
    transactions = filter_by_state(transactions, status)
    print(f"После фильтрации по статусу '{status}' осталось {len(transactions)} транзакций.")

    # 3. Сортировка
    if ask_yes_no("Отсортировать операции по дате?"):
        reverse = ask_yes_no("Отсортировать по убыванию?")
        transactions = sort_by_date(transactions, reverse)

    # 4. Фильтрация по валюте
    if ask_yes_no("Выводить только рублевые транзакции?"):
        transactions = list(filter_by_currency(transactions, 'RUB'))
        print(f"После фильтрации по валюте 'RUB' осталось {len(transactions)} транзакций.")

    # 5. Поиск по слову
    if ask_yes_no("Отфильтровать список транзакций по определенному слову в описании?"):
        word = input("Введите слово для поиска: ").strip()
        transactions = search_operation(transactions, word)

    # 6. Вывод результатов
    print("\nРаспечатываю итоговый список транзакций...")

    if transactions:
        print(f"\nВсего банковских операций в выборке: {len(transactions)}")
        for t in transactions:
            print(simple_format(t))
    else:
        print("\nНе найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
