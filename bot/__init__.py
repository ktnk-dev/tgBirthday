from . import (
    start,
    default,
    adding_friend,
    remove_friend,
    # send_all_bd
)
from models.bot import bot

def start_bot():
    print("Бот запущен...")
    bot.polling(none_stop=True)