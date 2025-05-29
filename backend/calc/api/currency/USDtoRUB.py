import requests

def get_rub():
    url = "https://api.exchangerate-api.com/v4/latest/USD"  # пример URL, подставь свой
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        rate = data.get("rates", {}).get("RUB")
        if rate:
            return rate  # возвращаем число курса
        else:
            print("Не удалось получить курс из ответа.")
            return None
    else:
        print(f"Ошибка запроса: {response.status_code}")
        return None
