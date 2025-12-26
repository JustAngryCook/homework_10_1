import requests
import os
from dotenv import load_dotenv
load_dotenv()

def convertation(transaction: dict) -> float:
    """Извлекает сумму из транзакции и возвращает как float, конвертирую в рубли"""
    try:
        # 1. Извлекаем данные
        amount = float(transaction["operationAmount"]["amount"])
        currency = transaction["operationAmount"]["currency"]["code"]

        # 2. Если рубли - возвращаем как есть
        if currency == "RUB":
            return amount

        # 3. Если USD или EUR - конвертируем
        elif currency in ("USD", "EUR"):
            url = f"https://api.apilayer.com/exchangerates_data/latest?base={currency}&symbols=RUB"
            API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
            headers = {
                "apikey": API_KEY
            }
            response = requests.get(url, headers=headers)
            data = response.json()
            rate = data["rates"]["RUB"]
            result = amount * rate
            return result

        # 4. Другая валюта - ошибка
        else:
            raise ValueError(f"Неподдерживаемая валюта: {currency}")

    except KeyError:
        raise KeyError("В транзакции нет нужных полей")
    except ValueError as e:
        raise ValueError(f"Некорректные данные: {e}")


print(convertation({
  "id": 441945886,
  "state": "EXECUTED",
  "date": "2019-08-26T10:50:58.294041",
  "operationAmount": {
    "amount": "700",
    "currency": {
      "name": "руб.",
      "code": "USD"
    }
  },
  "description": "Перевод организации",
  "from": "Maestro 1596837868705199",
  "to": "Счет 64686473678894779589"
}))