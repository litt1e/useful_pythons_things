#from wsgi import bot
import telebot
import os

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    print("Started new user")
    r3 = bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    print(f"\n+++++====\n{r3}\n+++++====\n")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print("Message has been got")
    bot.reply_to(message, message.text)


