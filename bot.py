import telebot

# Вставьте сюда ваш токен API
TOKEN = '7242489594:AAHIWD5GcYEnjdyrAkegCM3bbP-eU9_4tUk'

bot = telebot.TeleBot(TOKEN)

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я ваш бот. Напишите 'Привет' и я отвечу вам!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text.lower() == "привет":
        bot.reply_to(message, "Привет! Как дела?")
    else:
        bot.reply_to(message, "Я могу ответить только на 'Привет' :)")

# Запуск бота
bot.polling()
