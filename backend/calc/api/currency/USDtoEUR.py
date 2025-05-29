import requests

url = "https://open.er-api.com/v6/latest/USD"

def get_eur():
  response = requests.get(url)
  if response.status_code == 200:
      data = response.json()
      rate = data.get("rates", {}).get("EUR")
      if rate:
          return rate
      else:
          return None
  else:
        print(f"Ошибка запроса: {response.status_code}")
        return None
