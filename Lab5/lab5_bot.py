import os
import telebot
from telebot import types

# Токент бота
TOKEN = '2124745848:AAE8WuDOuQfzMY8Fdwf-WAARjjc29sB5P94'

# Сообщения
mes_smartphone = 'Хочу новый смартфон. Что можете предложить?'
mes_console = 'Время играть! Покажи-ка игровые консоли'

# Путь к текущему каталогу
cur_path = os.path.dirname(os.path.abspath(__file__))

# Создание бота
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Идентификатор диалога
    chat_id = message.chat.id

    # Текст, введенный пользователем, то есть текст с кнопки
    text = message.text

    # Проверка сообщения и вывод данных
    if text == mes_smartphone:
        bot.send_message(chat_id, 'У нас большой ассортимент смартфонов. Только сейчас скидки до 50%!!!')
        bot.send_message(chat_id, 'Iphone 13 - 73487 руб:')
        img = open(os.path.join(cur_path, 'img\Iphone.jpg'), 'rb')
        bot.send_photo(chat_id, img)
        bot.send_message(chat_id, 'Samsung galaxy S21 - 64490 руб:')
        img = open(os.path.join(cur_path, 'img\Samsung.jpg'), 'rb')
        bot.send_photo(chat_id, img)
    elif text == mes_console:
        bot.send_message(chat_id, 'Да, конечно. Игровые консоли на любой вкус и цвет:')
        bot.send_message(chat_id, 'XBOX ONE Series X - 67390 руб:')
        img = open(os.path.join(cur_path, 'img\XBOX.jpeg'), 'rb')
        bot.send_photo(chat_id, img)
        bot.send_message(chat_id, 'Sony Playstation 5 - 89457 руб:')
        img = open(os.path.join(cur_path, 'img\PS5.jpg'), 'rb')
        bot.send_photo(chat_id, img)
    else:
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton(mes_smartphone)
        itembtn2 = types.KeyboardButton(mes_console)
        markup.add(itembtn1, itembtn2)
        bot.send_message(chat_id, 'Зравствуйте!Я DANiCH_helper. Чем я могу вам помочь?', reply_markup=markup)


bot.infinity_polling()