from backend.api.crypto import toncoin, bitcoin, notcoin

def quiz():
    print("Выберите криптовалюту для получения информации:")
    print("1. Toncoin")
    print("2. Bitcoin")
    print("3. Notcoin")

    choice = input("Введите номер вашего выбора: ")

    if choice == '1':
        toncoin.get_info()
    elif choice == '2':
        bitcoin.get_info()
    elif choice == '3':
        notcoin.get_info()
        
    else:
        print("Неверный выбор. Пожалуйста, попробуйте снова.")

quiz()
