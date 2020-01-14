import os

from flask import Flask, request
from bot import *

import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
app = Flask(__name__)

#  сделать wsgi

@app.route('/' + TOKEN, methods=['POST'])
def getMessage():
    print("Message has been got")
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@app.route("/")
def webhook():
    print("It is works")
    r = bot.remove_webhook()
    r2 = bot.set_webhook(url='https://shlyapikbot.herokuapp.com/' + TOKEN)
    print(f"{r},\n++++++++\n {r2}")
    return "!", 200



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))