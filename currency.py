import requests
import json

FAVORITE_CURRENCIES = ["USD", "EUR", "GBP", "RUB"]

def get_currency_rate(currency_code: str):
    URL = f"https://open.er-api.com/v6/latest/{currency_code}"

    try:
        response = requests.get(URL, timeout=10)
    except requests.RequestException as e:
        print(f"Ошибка запроса: {e}")
        return None
    if response.status_code != 200: 
        print(f"Ошибка: {response.status_code}")
        return None
    
    try:
        data = response.json()
        return data
    except json.JSONDecodeError:
        print("Ошибка: некорректный JSON")
        return None
    
def save_to_file(data: dict):
    try:
        with open("currency_rate.json", "w") as file:
            json.dump(data, file)
    except (OSError, PermissionError, json.JSONEncodeError) as e:
        print(f"Ошибка сохранения: {e}")

def update_currency_rates():
    all_data = {}
    for currency in FAVORITE_CURRENCIES:
        rate = get_currency_rate(currency)
        if rate is not None:
            all_data[currency] = rate

    save_to_file(all_data)
    print(f"Данные обновлены в currency_rate.json")

def read_from_file():
    try:
        with open("currency_rate.json", "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError, PermissionError) as e:
        print(f"Ошибка чтения: {e}")
        return None

if __name__ == "__main__":
    update_currency_rates()
