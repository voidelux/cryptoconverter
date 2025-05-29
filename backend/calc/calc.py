def get_toncoin_usd():
    from backend.calc.api.crypto import toncoin
    toncoin_usd = toncoin.get_usd_price()  # Adjust this based on your actual implementation
    return toncoin_usd

if __name__ == "__main__":
    toncoin_usd_value = get_toncoin_usd()
    print(f"Current Toncoin to USD rate: {toncoin_usd_value}")
