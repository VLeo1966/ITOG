# bot/bot.py
import telebot

API_TOKEN = '7843222297:AAGIsnQ6v247JoCJUcUOfiNl_aCAf30fFho'
bot = telebot.TeleBot(API_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to FlowerDelivery! You will receive updates on your orders here.")


# Функция отправки сообщения с заказом
def notify_order(order_info):
    bot.send_message(chat_id='your-chat-id', text=order_info)


bot.polling()
