from extensions import APIException, CurrencyConverter
import telebot
import requests
from TOKEN_TG import TG_TOKEN

TOKEN = TG_TOKEN

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    instructions = """
    Привет! Я бот для конвертации валют.
    Для получения цены на валюту используй следующий формат сообщения:
    <имя валюты цену которой ты хочешь узнать> <имя валюты в которой хочешь узнать цену первой валюты> <количество первой валюты>

    Например: USD RUB 100
    Это вернет цену 100 долларов в рублях.

    Доступные команды:
    /start - начать использование бота
    /help - получить инструкции
    /values - информация о доступных валютах
    """
    bot.reply_to(message, instructions)


@bot.message_handler(commands=['values'])
def handle_values(message):
    available_currencies = """
    Доступные валюты:
    - USD: Доллар США
    - EUR: Евро
    - RUB: Российский рубль
    - GBP: Фунт стерлингов
    - JPY: Японская иена
    - AUD: Австралийский доллар
    - CAD: Канадский доллар
    - CHF: Швейцарский франк
    - CNY: Китайский юань
    """
    bot.reply_to(message, available_currencies)


@bot.message_handler(func=lambda message: True)
def handle_conversion(message):
    try:
        input_data = message.text.split()

        if len(input_data) != 3:
            raise APIException(
                "Неправильный формат запроса. Пожалуйста, введите запрос в таком формате: <Запрашиваемая валюта> <В какую валюту конвертировать> <Сумма>")

        base_currency = input_data[0].upper()
        quote_currency = input_data[1].upper()
        amount = float(input_data[2])

        converted_amount = CurrencyConverter.get_price(base_currency, quote_currency, amount)
        converted_amount = round(converted_amount, 3)  # Округление до 3 знаков после запятой

        result_message = f"{amount} {base_currency} = {converted_amount} {quote_currency}"
        bot.reply_to(message, result_message)

    except ValueError:
        error_message = "Неправильный формат запроса. Пожалуйста, введите запрос втаком формате: <Запрашиваемая валюта> <В какую валюту конвертировать> <Сумма>"
        bot.reply_to(message, error_message)

    except APIException as e:
        error_message = str(e)
        bot.reply_to(message, error_message)

    except Exception as e:
        error_message = "Произошла ошибка при обработке запроса"
        bot.reply_to(message, error_message)

bot.polling()