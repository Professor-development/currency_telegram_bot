import telebot
from config import TOKEN
from exctention import CurrencyConverter, ConverterException

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = "Чтобы начать работу введите команду боту в следующем формате:\n<название валюты>\
<в какую валюту перевести>\
<количество переводимой валюты>\nЧтобы получить список доступных валют введите: /values"
    bot.reply_to(message, text)


@bot.message_handler(commands=['values', ])
def get_values(message: telebot.types.Message):
    text = CurrencyConverter.get_values()
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(" ")
        if len(values) != 3:
            raise ConverterException("Слишком много параметров")
        quote, base, amount = values
        final_amount = CurrencyConverter.get_price(quote, base, amount)
    except ConverterException as e:
        bot.reply_to(message, f"Ошибка пользователя\n{e}")
    except Exception as e:
        bot.reply_to(message, f"Не удалось обработать команду\n{e}")
    else:
        text = f"Цена {amount} {quote} в {base} - {round(final_amount, 2)}"
        bot.reply_to(message, text)


bot.polling(none_stop=True)
