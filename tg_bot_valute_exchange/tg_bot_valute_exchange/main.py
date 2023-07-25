import telebot, buttons, buttons_valute

bot = telebot.TeleBot('6116437158:AAEhdgh-htv-bETqQ7W5PZ97ePhyxbUYc7s')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.from_user.id, 'Hello, what can I help u', reply_markup=buttons.choice_buttons())

@bot.message_handler(content_types=['text'])
def text_message(message):
    if message.text.lower() == 'курс_валют':
        bot.send_message(message.from_user.id, 'Выберите валюту:'
                                               'dollar'
                                               'euro'
                                               'pound')

    elif message.text.lower() == 'stop':
        bot.send_message(message.from_user.id, 'Good bye 😥')



# @bot.message_handler(content_types=['text'])
# def text_message(valute):
#     bot.send_message(valute.from_user.id, reply_markup=buttons_valute.buttons_valute())
#     if valute.text.lower() == 'dollar $':
#         bot.send_message(valute.from_user.id, 'Введите сумму', reply_markup=telebot.types.ReplyKeyboardRemove())
#         bot.register_next_step_handler(valute, dollar)
#
def dollar(valute):
    if valute.text.lower() == 'dollar':
        d = int(input('Add dollars: '))
        c =1350
        bot.send_message(valute.from_user.id, d*c, 

#         a = valute.text * 1500
#         bot.send_message(valute.from_user.id, a)
#         bot.register_next_step_handler(valute, dollar)
#     # a*b
#     # return dollar(a,b)


bot.polling()