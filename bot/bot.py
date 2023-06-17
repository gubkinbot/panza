import telebot
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")
bot = telebot.TeleBot(os.getenv("PANZA_TG_TOKEN"))

@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Внутренний сервис для ЛУОК. CV и NLP в помощь.')

@bot.message_handler(commands=['coffee'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Модуль анализа загрузки буфета. Баллы пробок, как в Яндекс.Картах.')

@bot.message_handler(commands=['learn'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Познавательный модуль. Три курса обучения: искусственный интеллект, кофе и нефтегаз. Подписка на AI-анализ статей SPE.')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    response = openai.ChatCompletion.create(model='gpt-3.5-turbo-16k-0613', messages=[{'role': 'system', 'content': 'Ты помощник ЛУОК'}, {'role': "user", "content": str(message.text)}])
    bot.send_message(message.chat.id, response['choices'][0]['message']['content'])

bot.polling()