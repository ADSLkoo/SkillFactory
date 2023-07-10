import requests

class APIException(Exception):
    pass

class CurrencyConverter:
    @staticmethod
    def get_price(base, quote, amount):
        url = f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}"
        response = requests.get(url)

        if response.status_code != 200:
            raise APIException("Ошибка при получении курса валют")

        data = response.json()

        if quote not in data:
            raise APIException("Неправильно указана валюта или количество первой валюты")

        rate = data[quote]
        converted_amount = amount * rate

        return converted_amount