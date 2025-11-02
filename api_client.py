import requests

def get_currency_rates(base: str) -> dict:
    URL = f"https://open.er-api.com/v6/latest/{base}"
    
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Ошибка: не удалось получить данные для {base}")
        return {}