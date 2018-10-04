import telebot
import constants
import constant

bot = telebot.TeleBot(constants.token)

#bot.send_message(336708361, "test")

upd = bot.get_updates()
#print(upd)

#last_upd = upd[-1]
#message_from_user = last_upd.message
#print(message_from_user)

@bot.message_handler(commands = ['start'])
def handle_start(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
    user_markup.row(u"\U0001F4A1"'Натисни тут'u"\U0001F4A1", u"\U0001F195"'Тут щось новеньке?'u"\U0001F195", 'Може тут?'u"\U0001F914")
    user_markup.row('Тут точно'u'\U0001f604', 'Тепер вгадалa)'u"\U0001F605")
    user_markup.row('Цього тут не було'u"\U0001F914", 'Це точно останнє!'u"\U0001F925"u"\U0001F925"u"\U0001F925", 'Не дістало ще?'u"\U0001F926\u200D\u2642\uFE0F")
    bot.send_message(message.from_user.id, 'Хороший бот, правда?', reply_markup = user_markup)

@bot.message_handler(commands = ['stop'])
def handle_start(message):
    hide_markup = telebot.types.ReplyKeyboardRemove(True)
    bot.send_message(message.from_user.id, 'Ти закрила клавіатуру!', reply_markup = hide_markup)

@bot.message_handler(content_types=['text'])
def handle_command(message):
    if message.text == u"\U0001F4A1"'Натисни тут'u"\U0001F4A1":
        bot.send_message(message.chat.id, 'poem1')
    elif message.text == u"\U0001F195"'Тут щось новеньке?'u"\U0001F195":
        bot.send_message(message.chat.id, 'poem2')
    elif message.text == 'Може тут?'u"\U0001F914":
        bot.send_message(message.chat.id, 'poem3')
    elif message.text == 'Тут точно'u'\U0001f604':
        bot.send_message(message.chat.id, 'poem4')
    elif message.text == 'Тепер вгадалa)'u"\U0001F605":
        bot.send_message(message.chat.id, 'poem5')
    elif message.text == 'Цього тут не було'u"\U0001F914":
        bot.send_message(message.chat.id,'poem6')
    elif message.text == 'Це точно останнє!'u"\U0001F925"u"\U0001F925"u"\U0001F925":
        bot.send_message(message.chat.id,'poem7')
    elif message.text == 'Не дістало ще?'u"\U0001F926\u200D\u2642\uFE0F":
        bot.send_message(message.chat.id,'poem8')
    else:
        bot.send_message(message.chat.id, 'Обери кнопку!')


bot.polling(none_stop = True, interval = 0)
