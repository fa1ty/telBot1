import telebot

bot = telebot.TeleBot('5151693175:AAGacM5Sv9XLJDrlgpaFoKDLBff5UUq6KMs')

@bot.message_handler(commands=["start"])
def start(message, res=False):
    chat_id = message.chat.id

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Главное меню")
    btn2 = types.KeyboardButton("❓ Помощь")
    markup.add(btn1, btn2)

    bot.send_message(chat_id,
                     text="Привет, {0.first_name}! Я тестовый бот для курса программирования на языке ПаЙтон".format(
                         message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    chat_id = message.chat.id
    ms_text = message.text
    bot.send_message(chat_id, text="Я тебя слышу!!! Ваше сообщение: " + ms_text)

bot.polling(none_stop=True, interval=0)