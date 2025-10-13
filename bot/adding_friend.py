from datetime import datetime, timedelta 

from telebot.types import Message
from models.user import getUser, saveUser, Birthday
from models.markup import Markup

from models.bot import bot, send

TEMP_NAMES: dict[int, str] = {}

@bot.message_handler(
    func=lambda message: 
        getUser(message).state.name == 'choose_name'
)
def save_name(message: Message):
    user = getUser(message)
    TEMP_NAMES[user.id] = user.text
    
    for bd in user.bdays:
        if user.text == bd.name:
            return send(
                user,
                "<b>У вас ошибочка ❌ Друг уже добавлен Введите другое имя</b> "
            )


    now = datetime.now()
    user.state.date = datetime(now.year, now.month, 15)
    user.state.name = 'choose_date'
    
    
    send(
        user,
        "<b>Выберете дату рождения человека</b> 🎁",
        Markup.calendar()
    )
    
    saveUser(user)
    
    
@bot.message_handler(
    func=lambda message: 
        getUser(message).state.name == 'choose_date'
)
def calendar_manager(message: Message):
    user = getUser(message)

    if '⬅️' in user.text or '➡️' in user.text: 
        delta = timedelta(days=(30 if '➡️' in user.text else - 30))
        user.state.date += delta

        send(
            user,
            "<b>Обновляю календарь...</b> 🔄",
            Markup.calendar(user.state.date.month, user.state.date.year)
        )
    
    if user.text.isdigit():
        user.bdays.append(Birthday(
            name=TEMP_NAMES[user.id],
            date=datetime(
                user.state.date.year,
                user.state.date.month,
                int(user.text)
            )
        ))

        user.state.name = "default"
        
        send(
            user,
            "<b>День рождения добавлен</b> 💾",
            Markup.main()
        )
    saveUser(user)