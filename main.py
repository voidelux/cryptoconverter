from backend.calc.api.crypto import toncoin, bitcoin, notcoin
from backend.calc.api.currency import USDtoEUR, USDtoRUB, USDtoUAH

def quiz():
    eur = USDtoEUR.get_eur()
    rub = USDtoRUB.get_rub()
    uah = USDtoUAH.get_uah()
    usd = 1.0

    print("Выберите криптовалюту для получения информации:")
    print("1. Toncoin")
    print("2. Bitcoin")
    print("3. Notcoin")
    choice = input("Введите номер вашего выбора: ")

    if choice == '1':
        crypto_price_usd = toncoin.get_info()
    elif choice == '2':
        crypto_price_usd = bitcoin.get_info()
    elif choice == '3':
        crypto_price_usd = notcoin.get_info()
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")
        return

    if crypto_price_usd is None:
        print("Не удалось получить цену криптовалюты.")
        return

    try:
        amount = float(input("Сколько монет вы хотите конвертировать? "))
    except ValueError:
        print("Некорректное число.")
        return

    print("В какой валюте вы хотите получить результат?")
    print("Доступные варианты: USD, EUR, RUB, UAH")
    currency = input("Введите валюту: ").upper()

    total_usd = crypto_price_usd * amount

    if currency == 'EUR':
        print(f"{amount} монет = {total_usd * eur:.2f} EUR")
    elif currency == 'RUB':
        print(f"{amount} монет = {total_usd * rub:.2f} RUB")
    elif currency == 'UAH':
        print(f"{amount} монет = {total_usd * uah:.2f} UAH")
    elif currency == 'USD':
        print(f"{amount} монет = {total_usd:.2f} USD")
    else:
        print("Неверный выбор валюты.")

quiz()
