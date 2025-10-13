from telebot.types import Message
from models.user import getUser, saveUser, Birthday
from models.markup import Markup

from models.bot import bot, send

@bot.message_handler(
    func=lambda message: 
        getUser(message).state.name == 'delete_friend'
)
def _(message: Message):
    user = getUser(message)
    user.state.name = "default"
    
    # Удаление из списка дня рождений человека. Путем фильтрации списка друзей
    user.bdays = list(filter(lambda bd: user.text != bd.name, user.bdays))
    
    send(
        user,
        "<b>Удален(а)</b> 💔",
        Markup.main()
    )
    
    saveUser(user)