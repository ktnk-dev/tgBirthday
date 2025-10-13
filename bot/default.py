from telebot.types import Message
from models.user import getUser, saveUser
from models.markup import Markup

from models.bot import bot


@bot.message_handler(
    func=lambda message: 
        getUser(message.from_user.id).state.name == 'default'
)
def handle_default_state(message: Message):
    user = getUser(message.from_user.id)

    match (message.text):
        case 'Добавить':
            user.state.name = 'choose_name'
            
            bot.send_message(
                user.id,
                "Как зовут человека?",
                reply_markup = Markup.remove()
            )
        
        case 'Удалить':
            ...
        
        case 'За месяц':
            ...
            
        case 'За весь год':
            ...
        
            
    saveUser(user)