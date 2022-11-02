import telebot
import json
import requests
import lxml
from lxml import etree

TOKEN = '5647381385:AAFrww2_FfVzdzcuJR2Iu-nHhh56ZFh-QxE'

bot = telebot.TeleBot(TOKEN)

keys = {
    'рубль': 'RUB',
    'доллар': 'USD',
    'евро': 'EUR',
    'японская йена': 'JPY',
    'британский фунт': 'GBP',
    'швейцарский франк': 'CHF'
}


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<название валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nЧтобы получить список доступных валют введите: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values', ])
def get_values(massage: telebot.types.Message):
    text = "Доступные валюты: \n"
    for key in keys.keys():
        text += f"{key} | {keys[key]}\n"
    bot.reply_to(massage, text)


bot.polling(none_stop=True)
