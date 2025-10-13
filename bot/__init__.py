from models.bot import bot
from telebot.handler_backends import ContinueHandling

@bot.message_handler(func=lambda _: True)
def middleware(message): 
    print(message.from_user.id, message.text)
    return ContinueHandling()

from . import (
    start,
    default,
    adding_friend,
    remove_friend,
    # send_all_bd
)


def start_bot():
    print("Бот запущен...")
    bot.polling(none_stop=True)