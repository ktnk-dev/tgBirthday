from models.bot import bot
from bot import *



if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)