import telebot
from telebot import types
import config
import dbworker

# Создание бота
bot = telebot.TeleBot(config.TOKEN)


# Начало диалога
@bot.message_handler(commands=['start'])
def cmd_start(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id, 'Приветствую тебя, '+ name)
    bot.send_message(message.chat.id, 'Я бот-калькулятор!')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    bot.send_message(message.chat.id, 'Введите первое число')


# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога
@bot.message_handler(commands=['reset'])
def cmd_reset(message):
    bot.send_message(message.chat.id, 'Сбрасываем результаты предыдущего ввода.')
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
    bot.send_message(message.chat.id, 'Введите первое число')


# Обработка первого числа
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_FIRST_NUM.value)
def first_num(message):
    text = message.text
    if not text.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы ввели первое число {text}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value), text)
        bot.send_message(message.chat.id, 'Введите второе число')


# Обработка второго числа
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_SECOND_NUM.value)
def second_num(message):
    text = message.text
    if not text.isdigit():
        # Состояние не изменяется, выводится сообщение об ошибке
        bot.send_message(message.chat.id, 'Пожалуйста введите число!')
        return
    else:
        bot.send_message(message.chat.id, f'Вы ввели второе число {text}')
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_OPERATION.value)
        # Сохраняем первое число
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value), text)
        markup = types.ReplyKeyboardMarkup(row_width=2)
        itembtn1 = types.KeyboardButton('+')
        itembtn2 = types.KeyboardButton('*')
        itembtn3 = types.KeyboardButton('/')
        itembtn4 = types.KeyboardButton('-')
        markup.add(itembtn1, itembtn2, itembtn3, itembtn4)
        bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)


# Выбор действия
@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_OPERATION.value)
def operation(message):
    # Текущее действие
    op = message.text
    # Читаем операнды из базы данных
    v1 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_FIRST_NUM.value))
    v2 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_SECOND_NUM.value))
    # Выполняем действие
    fv1 = float(v1)
    fv2 = float(v2)
    global res

    if op == '/' and fv2 == 0:
        bot.send_message(message.chat.id, 'На ноль делить нельзя!')
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_SECOND_NUM.value)
        bot.send_message(message.chat.id, 'Введите второе число')
        return
    res = final(op, fv1, fv2)
    # Выводим результат
    markup = types.ReplyKeyboardRemove(selective=False)
    bot.send_message(message.chat.id, f'Результат: {v1}{op}{v2}={str(res)}', reply_markup=markup)
    markup = types.ReplyKeyboardMarkup(row_width=2)
    itembtn1 = types.KeyboardButton('MR')
    itembtn2 = types.KeyboardButton('MC')
    itembtn3 = types.KeyboardButton('M+')
    itembtn4 = types.KeyboardButton('M-')
    itembtn5 = types.KeyboardButton('MS')
    itembtn6 = types.KeyboardButton('Продолжить вычисления')
    markup.add(itembtn1, itembtn2, itembtn3, itembtn4, itembtn5, itembtn6)
    bot.send_message(message.chat.id, 'Выберите пожалуйста действие', reply_markup=markup)
    dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_EXTRA.value)

def final(op, fv1, fv2):
    if op == '+':
        ans = fv1 + fv2
    elif op == '*':
        ans = fv1 * fv2
    elif op == '/' and fv2 != 0:
        ans = fv1 / fv2
    elif op == '-':
        ans = fv1 - fv2
    return ans

@bot.message_handler(func=lambda message: dbworker.get(
    dbworker.make_key(message.chat.id, config.CURRENT_STATE)) == config.States.STATE_EXTRA.value)
def extra(message):
    result = res
    extra_op = message.text
    if extra_op == 'MS':
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_EXTRA.value), str(result))
        bot.send_message(message.chat.id, 'Число успешно сохранено')
    elif extra_op == 'MR':
        v3 = dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_EXTRA.value))
        bot.send_message(message.chat.id, 'Число, сохраненное в памяти:' + v3)
    elif extra_op == 'MC':
        result = 0
        dbworker.set(dbworker.make_key(message.chat.id, config.States.STATE_EXTRA.value), result)
        bot.send_message(message.chat.id, 'Число удалено из памяти')
    elif extra_op == 'Продолжить вычисления':
        # Меняем текущее состояние
        dbworker.set(dbworker.make_key(message.chat.id, config.CURRENT_STATE), config.States.STATE_FIRST_NUM.value)
        # Выводим сообщение
        bot.send_message(message.chat.id, 'Введите первое число')
    elif extra_op == 'M-':
        k1 = float(dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_EXTRA.value)))
        result = k1 - res
        bot.send_message(message.chat.id, f'Результат: {k1}-{res}={str(result)}')
    elif extra_op == 'M+':
        k1 = float(dbworker.get(dbworker.make_key(message.chat.id, config.States.STATE_EXTRA.value)))
        result = k1 + res
        bot.send_message(message.chat.id, f'Результат: {k1}+{res}={str(result)}')

if __name__ == '__main__':
    bot.infinity_polling()