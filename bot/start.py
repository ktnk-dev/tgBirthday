from telebot.types import Message
from models.user import getUser, saveUser
from models.markup import Markup

from models.bot import bot


@bot.message_handler(commands=['start'])
def welcome_info(message: Message):
    """
    Выводит приветственное сообщение и сбрасывает класс календаря в default
    """

    
    user = getUser(message.from_user.id)
    saveUser(user)
    
    # Если надо отчистить все данные после /start
    # saveUser(User(id=message.from_user.id))

    bot.send_message(
        message.chat.id,
        "Привет. Я бот для отслеживания дней рождений",
        reply_markup = Markup.main()
    )