# SkilltestmainBot
# t.me/SkilltestmainBot
# Token - 5505670952:AAEAU19T53OQ50BMj6AfxXhluSSmUH_HmEk

import telebot
from config import keys, TOKEN
from extensions import ConvertionException, ConverterValut

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
     bot.send_message(message.chat.id, f'Приветствую {message.chat.username}.\n '
    f'Бот возвращает цену на определённое количество валюты (доллар, евро или рубль). Вы должны отправить '
    f'сообщение боту в виде <имя валюты> - цену которой хотите узнать, <имя валюты> - в которой надо узнать цену '
    f'первой валюты <количество первой валюты>.\n Например:\n доллар рубль 100\n доллар рубль 5.5\n Увидеть список всех доступных валют /values ')

@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text ='\n'.join((text, key, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) > 3:
            raise ConvertionException('Слишком много параметров')

        quote, base, amount = values
        total_quote, total_base = ConverterValut.get_price(quote, base, amount)

    except ConvertionException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {keys[quote]} в {keys[base]} - {round(float(amount) * total_base / total_quote,6)} {keys[base]}'
        bot.send_message(message.chat.id, text)



bot.polling(none_stop=True)

