import requests
import json
from config import keys


class ConverterException(Exception):
    pass


class CurrencyConverter:
    @staticmethod
    def get_values():
        text = "Доступные валюты: \n"
        for key in keys.keys():
            text += f"{key}\n"
        return text

    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        try:
            quote = quote.lower()
        except AttributeError:
            pass

        try:
            base = base.lower()
        except AttributeError:
            pass

        if quote == base:
            raise ConverterException(f"Невозможно перевести одинаковые валюты: {base}")

        try:
            quote_ticker = keys[quote.lower()]
        except KeyError:
            raise ConverterException(f'Не удалось обработать валюту: {quote}')

        try:
            base_ticker = keys[base.lower()]
        except KeyError:
            raise ConverterException(f'Не удалось обработать валюту: {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f"Не удалось обработать количество: {amount}")

        r = requests.get(
            f'https://currate.ru/api/?get=rates&pairs={quote_ticker}{base_ticker}&key=be54ddc3c404c7ee2894e325f1cea893')
        currency = json.loads(r.content)['data'][f'{quote_ticker}{base_ticker}']
        final_amount = float(currency) * amount

        return final_amount
