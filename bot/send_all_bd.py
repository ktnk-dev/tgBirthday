from datetime import datetime, timedelta 

from telebot.types import Message
from models.user import getUser, saveUser, Birthday
from models.markup import Markup

from models.bot import bot, send


@bot.message_handler(func=lambda message: message.text == "За весь год")
def _(message):
    user = getUser(message)

    