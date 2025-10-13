from telebot.types import Message
from models.user import getUser, saveUser
from models.markup import Markup

from models.bot import bot, send


@bot.message_handler(
    func=lambda message: 
        getUser(message).state.name == 'default'
)
def handle_default_state(message: Message):
    user = getUser(message)

    match (message.text):
        case 'Добавить':
            user.state.name = 'choose_name'
            
            send(
                user,
                "Как зовут человека?",
                Markup.remove()
            )
        
        case 'Удалить':
            if len(user.bdays) < 1:
                
                return send(
                    user,
                    "У вас нету друзей. плаки-плаки :sad_emote:"
                )
                
            user.state.name = "delete_friend"

            send(
                user, 
                "Выберите друга, которого нужно удалить",
                Markup.display_friends(user)
            )            
        
        case 'За месяц':
            ...
            
        case 'За весь год':
            ...
        
            
    saveUser(user)