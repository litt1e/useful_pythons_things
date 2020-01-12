import os

from flask import Flask, request

import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
server = Flask(__name__)


@server.route('/' + TOKEN, methods=['POST'])
def getMessage():
    print("Message has been got")
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    print("It is works")
    r = bot.remove_webhook()
    r2 = bot.set_webhook(url='https://shlyapikbot.herokuapp.com' + TOKEN)
    print(f"{r},\n++++++++\n {r2}")
    return "!", 200


@bot.message_handler(commands=['start'])
def start(message):
    print("Started new user")
    r3 = bot.reply_to(message, 'Hello, ' + message.from_user.first_name)
    print(f"\n+++++====\n{r3}\n+++++====\n")


@bot.message_handler(func=lambda message: True, content_types=['text'])
def echo_message(message):
    print("Message has been got")
    bot.reply_to(message, message.text)


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))