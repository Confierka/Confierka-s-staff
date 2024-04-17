from PIL import Image, ImageDraw
import telebot
import time
import threading
import requests
from random import randint


API = "6275842632:AAFmpv6pyKwt_vCezKcASCEq4CL3HZ8QDzE"

bot = telebot.TeleBot(API)

numbers=dict()
@bot.message_handler(commands=['begin'])
def begin(message):
    num = randint (1,100)
    id = message.chat.id

    numbers[id] = num

    bot.reply_to(message,"Угадай число от 1 до 100")

@bot.message_handler(regexp='^\d+$')
def serve(message):
    id = message.chat.id
    num = numbers[id]

    if num is None:
        bot.reply_to(message,"Начни игру /begin")
        return

    got = int(message.text)


    if got == num:
        bot.reply_to(message,"Win")
        return
    
    if got > num:
        bot.reply_to(message, "Ваше число слшиком большое")

    if got < num:
        bot.reply_to(message, "Ваше число слшиком маленькое")


threading.Thread(target= bot.polling).start()

