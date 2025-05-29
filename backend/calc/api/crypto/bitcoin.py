import requests
import json

url = "https://api.coinpaprika.com/v1/tickers/btc-bitcoin"

response = requests.get(url)

def get_info():
  if response.status_code == 200:
      data = response.json()
      print(" ")
      btcprice = round(data['quotes']['USD']['price'], 2)
      return btcprice
  else:
      print(f"Ошибка: {response.status_code}")
      return None
