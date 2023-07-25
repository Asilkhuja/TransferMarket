from telebot import types

def choice_buttons():
    #создаем пространства для кнопок
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True)

    #создаем сами кнопки
    usd_button = types.KeyboardButton('USD')
    eur_button = types.KeyboardButton('EUR')

    #добавляем кнопки в пространство
    kb.add(usd_button, eur_button)

    #вернуть пространство
    return kb