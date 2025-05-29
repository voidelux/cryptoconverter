from textual.app import App, ComposeResult
from textual.containers import Container
from textual.widgets import Header, Footer, Button, Static, Input, Select

from backend.calc.api.crypto import toncoin, bitcoin, notcoin
from backend.calc.api.currency import USDtoEUR, USDtoRUB, USDtoUAH


class CryptoConverter(App):

    def compose(self) -> ComposeResult:
        yield Header()
        yield Container(
            Static("Выберите криптовалюту:"),
            Select(options=[
                ("Toncoin", "toncoin"),
                ("Bitcoin", "bitcoin"),
                ("Notcoin", "notcoin"),
            ], id="crypto_choice"),

            Static("Введите количество монет:"),
            Input(placeholder="Например, 3.5", id="amount"),

            Static("Выберите валюту:"),
            Select(options=[
                ("USD", "USD"),
                ("EUR", "EUR"),
                ("RUB", "RUB"),
                ("UAH", "UAH"),
            ], id="currency_choice"),

            Button("Конвертировать", id="convert_btn"),
            Static(id="result", classes="result")
        )
        yield Footer()

    async def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "convert_btn":
            crypto = self.query_one("#crypto_choice", Select).value
            currency = self.query_one("#currency_choice", Select).value
            amount_input = self.query_one("#amount", Input).value
            result_display = self.query_one("#result", Static)

            try:
                amount = float(amount_input)
            except ValueError:
                result_display.update("Некорректное число.")
                return

            crypto_price = None
            if crypto == "toncoin":
                crypto_price = toncoin.get_info()
            elif crypto == "bitcoin":
                crypto_price = bitcoin.get_info()
            elif crypto == "notcoin":
                crypto_price = notcoin.get_info()

            if crypto_price is None:
                result_display.update("Не удалось получить цену криптовалюты.")
                return

            total_usd = crypto_price * amount
            eur = USDtoEUR.get_eur()
            rub = USDtoRUB.get_rub()
            uah = USDtoUAH.get_uah()

            if currency == "USD":
                result = f"{amount} монет = {total_usd:.2f} USD"
            elif currency == "EUR":
                result = f"{amount} монет = {total_usd * eur:.2f} EUR"
            elif currency == "RUB":
                result = f"{amount} монет = {total_usd * rub:.2f} RUB"
            elif currency == "UAH":
                result = f"{amount} монет = {total_usd * uah:.2f} UAH"
            else:
                result = "Неверный выбор валюты."

            result_display.update(result)


if __name__ == "__main__":
    app = CryptoConverter()
    app.run()
