from telebot import types

def choice_buttons():
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

    course_button = types.KeyboardButton('курс_валют')
    stop_button = types.KeyboardButton('stop')

    kb.add(course_button, stop_button)

    return kb


def buttons_valute():
    bv = types.ReplyKeyboardMarkup(resize_keyboard=True)

    dollar = types.KeyboardButton('dollar $')
    pounds = types.KeyboardButton('pounds £')
    euros = types.KeyboardButton('euros Э💶')

    bv.add(dollar, pounds, euros)





