"""Модуль для работы с API"""

import requests

def get_rate(code):
    try:
        url = "https://www.cbr-xml-daily.ru/daily_json.js"
        response = requests.get(url)
        data = response.json()
        rates = data["Valute"]

        if code in rates:
            return rates[code]["Value"]
        else:
            return None

    except requests.RequestException as e:
        print(f"Ошибка сети: {e}")
        return None
    except (KeyError, ValueError) as e:
        print(f"Ошибка в данных API: {e}")
        return None

if __name__ == "__main__":
    print("Это модуль курс валют.")