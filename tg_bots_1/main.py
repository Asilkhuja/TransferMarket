#

import telebot, buttons

bot = telebot.TeleBot('5984470952:AAH7okxEFWp6rkvXIErvAhdJxJj8VkKCmow')
USD = 11520
EUR = 12300

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Привет!', reply_markup=buttons.choice_buttons())

# @bot.message_handler(content_types=['text'])
# def text_message(message):
#     if message.text.lower() == 'hello':
#         bot.send_message(message.from_user.id, 'How are you?')
#
#     elif message.text.lower() == 'Bye':
#         bot.send_message(message.from_user.id, 'Ok, bye😒')

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.from_user.id, 'Nice to meet u')

    elif message.text.lower() == 'Bye':
        bot.send_message(message.from_user.id, 'Ok, bye😒')

    elif message.text.lower() == 'usd':
        bot.send_message(message.from_user.id, 'Введите сумму', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, usd_con)

    elif message.text.lower() == 'eur':
        bot.send_message(message.from_user.id, 'Введите сумму', reply_markup=telebot.types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, eur_con)



def usd_con(message):
   try:
       a = int(message.text)
       if a >= 0:
           bot.send_message(message.from_user.id, f'{int(a)/USD}', reply_markup=buttons.choice_buttons())
           bot.register_next_step_handler(message, text_message)
       else:
           bot.send_message(message.from_user.id, 'Пиши больше 0!')

   except telebot.apihelper.ApiTelegramException:
       bot.send_message(message.from_user.id, 'Пишите цифры!')


def eur_con(message):
    try:
        bot.send_message(message.from_user.id, f'{int(message.text) / EUR}', reply_markup=buttons.choice_buttons())
        bot.register_next_step_handler(message, text_message)

    except telebot.apihelper.ApiTelegramException:
        bot.send_message(message.from_user.id, 'Пишите цифры!')

bot.polling()