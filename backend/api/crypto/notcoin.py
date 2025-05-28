import requests
import json

url = "https://api.coinpaprika.com/v1/tickers/not-notcoin"

response = requests.get(url)

def get_info():
  if response.status_code == 200:
      data = response.json()
      print(" ")
      notprice = round(data['quotes']['USD']['price'], 2)
      print(notprice)
  else:
      print(f"Ошибка: {response.status_code}")
