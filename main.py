import telebot
import json
import requests
import lxml
import lxml.html
from lxml import etree

TOKEN = '5647381385:AAFrww2_FfVzdzcuJR2Iu-nHhh56ZFh-QxE'

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубли': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'йена': 'JPY',
    'фунт': 'GBP',
    'франк': 'CHF',
    'тенге': 'KZT'
}


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<название валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nЧтобы получить список доступных валют введите: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values', ])
def get_values(message: telebot.types.Message):
    text = "Доступные валюты: \n"
    for key in keys.keys():
        text += f"{key} | {keys[key]}\n"
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    quote, base, amount = message.text.split(" ")
    quote = quote.lower()
    base = base.lower()
    r = requests.get(f'https://currate.ru/api/?get=rates&pairs={keys[quote]}{keys[base]}&key=be54ddc3c404c7ee2894e325f1cea893')
    currency = json.loads(r.content)['data'][f'{keys[quote]}{keys[base]}']
    final_amount = float(currency) * float(amount)
    text = f"Цена {amount} {quote} в {base} - {round(final_amount, 2)}"
    bot.reply_to(message, text)


bot.polling(none_stop=True)
