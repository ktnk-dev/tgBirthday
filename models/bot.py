import telebot
from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
import config
from models.user import User
bot = telebot.TeleBot(config.TOKEN)

def send(user: User, text: str, markup: ReplyKeyboardMarkup | ReplyKeyboardRemove | None = None): 
    bot.send_message(
        user.id,
        text,
        reply_markup = markup,
        parse_mode = "html"
    )
