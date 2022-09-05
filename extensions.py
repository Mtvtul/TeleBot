import requests
import json
from config import keys

class ConvertionException(Exception):
    pass

class ConverterValut:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'Не удалось обработать количество {amount}')

        r = requests.get(f'https://cdn.cur.su/api/cbr.json')
        total_quote, total_base = json.loads(r.content)['rates'][quote_ticker], json.loads(r.content)['rates'][base_ticker]

        return total_quote, total_base