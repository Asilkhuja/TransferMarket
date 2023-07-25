from telebot import types

# def chois_inbuttons_in():
#     ki = types.InlineKeyboardMarkup()
#
#     dollars_button = types.InlineKeyboardButton('dollars $')
#     pounds_button = types.InlineKeyboardButton('pounds £')
#     euros_button = types.InlineKeyboardButton('euros Э💶')
#
#     ki.add(dollars_button, pounds_button,euros_button)
#
#     return ki


def buttons_valute():
    bv = types.ReplyKeyboardMarkup(resize_keyboard=True)

    dollar = types.KeyboardButton('dollar $')
    pounds = types.KeyboardButton('pounds £')
    euros = types.KeyboardButton('euros Э💶')

    bv.add(dollar, pounds, euros)