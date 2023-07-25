import telebot

bot = telebot.Telebot('6312010807:AAFTKVrMkdYgsXic7TydMkLF90mr4mPO2qY')



@bot.message_handler(commands=['admin'])
def start_admin(message):
    global user_id
    user_id = message.from_user.id

    if user_id == 88444281:
        bot.send_message(user_id, 'Добро пожловать!')
        bot.send_message(user_id, 'Что хотите сделать?')

    else:
        bot.send_message(user_id, 'Вы не админ!')