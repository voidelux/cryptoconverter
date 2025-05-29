import requests

url = "https://api.coinpaprika.com/v1/tickers/ton-toncoin"

def get_info():
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        tonprice = round(data['quotes']['USD']['price'], 2)
        return tonprice
    else:
        return None
