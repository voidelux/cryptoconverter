import requests

url = "https://open.er-api.com/v6/latest/USD"

def get_uah():
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      rate = data.get("rates", {}).get("UAH")
      if rate:
          return rate  # возвращаем число курса
      else:
          return None
  else:
        print(f"Ошибка запроса: {response.status_code}")
        return None
