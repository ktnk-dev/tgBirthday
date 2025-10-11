from datetime import datetime, timedelta 

from telebot.types import Message
from models.user import getUser, saveUser
from models.markup import Markup

from models.bot import bot

TEMP_NAMES: dict[int, str] = {}

@bot.message_handler(
    func=lambda message: 
        getUser(message.from_user.id).state.name == 'choose_name'
)
def _(message: Message):
    user = getUser(message.from_user.id)
    TEMP_NAMES[user.id] = message.text
    
    now = datetime.now()
    user.state.date = datetime(now.year, now.month, 15)
    user.state.name = 'choose_date'
    
    bot.send_message(
        user.id,
        "Выберете дату рождения человека",
        reply_markup=Markup.calendar()
    )
    
    saveUser(user)
    
    
@bot.message_handler(
    func=lambda message: 
        getUser(message.from_user.id).state.name == 'choose_date'
)
def _(message: Message):
    user = getUser(message.from_user.id)

    if '⬅️' in message.text or '➡️' in message.text:
        delta = timedelta(days=(30 if '➡️' in message.text else -30))
        user.state.date += delta

        bot.send_message(
            message.chat.id,
            "Обновляю календарь...",
            reply_markup = Markup.calendar(user.state.date.month, user.state.date.year)
        )
    
    if ...:
        ...
    saveUser(user)