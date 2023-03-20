import apikeys
import telebot
import openai

from telebot.types import ReplyKeyboardMarkup, KeyboardButton

TOKEN = apikeys.telegramkey

openai.api_key = apikeys.aikey

bot = telebot.TeleBot(TOKEN)
engine="text-davinci-003"


keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard.add(KeyboardButton('Об авторе'))
keyboard.add(KeyboardButton('О боте'))

@bot.message_handler(regexp=r'Об авторе\.*')
def about_author(message):
    bot.send_message(message.chat.id, "Меня зовут Юрий, мне 16 лет. Учусь писать код на Python")

@bot.message_handler(regexp=r'О боте\.*')
def about_bot(message):
    bot.send_message(message.chat.id, "Этот чат бот может ответить на любой твой вопрос с помощью ИИ!")

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    completion = openai.Completion.create(engine=engine, prompt=message.text, temperature=0.5, max_tokens=3500)

    bot.send_message(message.from_user.id, completion.choices[0]['text'])

    time.sleep(1)

bot.infinity_polling()
