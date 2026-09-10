import telebot
from dotenv import load_dotenv
import os

load_dotenv()

bot = telebot.TeleBot(os.getenv("BOT_TOKEN"))

@bot.message_handler(commands=["start"])
def send_welcome(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn0 = telebot.types.KeyboardButton("Связаться с продавцом")
    btn1 = telebot.types.KeyboardButton("Посмотреть ассортимент")

    markup.add(btn0,btn1)

    bot.send_message(message.chat.id,"Добро пожаловать в бота оптовика! Здесь вы можете ознакомиться со всем ассортиментом нашего магазина\nПожалуйста,выберите опцию.",reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Связаться с продавцом")
def about_bot(message):
    bot.send_message(message.chat.id, "Продавец: @biznes_88")

@bot.message_handler(func=lambda message: message.text == "Посмотреть ассортимент")
def about_bot(message):
    bot.send_message(message.chat.id, "1.Лимитированные Кроссовки Nike air max DN\n2.Классные жилетки C.P. Company")

if __name__ == "__main__":
    print("Бот успешно запущен")
    bot.infinity_polling()