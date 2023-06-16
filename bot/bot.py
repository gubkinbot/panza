import telebot
import os

bot = telebot.TeleBot(os.getenv("PANZA_TG_TOKEN"))

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я расскажу тебе, что умею...')

@bot.message_handler(commands=['coffee'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Кофе?')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    bot.send_message(message.chat.id, message.text)

bot.polling()