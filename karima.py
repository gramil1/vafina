import telebot, os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv('TOKEN'))



# Обработчик команды /start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я эхо-бот. Напиши мне что-нибудь!")

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    bot.send_message(message.chat.id, f"Ты сказал: {message.text}")

if __name__ == '__main__':
    bot.polling(none_stop=True)