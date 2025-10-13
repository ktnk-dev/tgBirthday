import calendar
from datetime import datetime
from telebot.types import Message
from models.user import getUser, saveUser
from models.markup import Markup

from models.bot import bot, send


@bot.message_handler(func=lambda message: message.text == "Haзад")
def return_back(message: Message):
    user = getUser(message)
    user.state.name = "default"

    send(
        user,
        "🏠 Возвращаюсь на главную...",
        Markup.main()
    )

    saveUser(user)


@bot.message_handler(
    func=lambda message: 
        getUser(message).state.name == 'default'
)
def handle_default_state(message: Message):
    user = getUser(message)

    match (user.text):
        case 'Добавить':
            user.state.name = 'choose_name'
            
            send(
                user,
                "<b>Как зовут человека?</b>",
                Markup.remove()
            )
        
        case 'Удалить':
            if len(user.bdays) < 1:
                
                return send(
                    user,
                    "<b>У вас нету друзей. плаки-плаки :sad_emote:</b>"
                )
                
            user.state.name = "delete_friend"

            send(
                user, 
                "<b>Выберите друга, которого нужно удалить</b> 😨",
                Markup.display_friends(user)
            )            
        
        case 'За месяц':
            empty_flag = True
            user.bdays.sort(key=lambda bd: bd.date.month)
            target_month = datetime.now().month
            text_to_send = f'\n<b>{calendar.month_name[target_month]}</b> 🗓\n'
            for bd in user.bdays:
                if bd.date.month == target_month:
                    text_to_send += f'<blockquote>{bd.name}: {bd.date.day} число</blockquote>' + '\n'
                    empty_flag = False


            if empty_flag:
                text_to_send += "Пусто...\n"
            
            return send(
                user,
                text_to_send
            )

            
        case 'За весь год':
            user.bdays.sort(key=lambda bd: bd.date.month)
            text_to_send = ''
            last_saved_month = -1

            for bd in user.bdays:
                if bd.date.month != last_saved_month:
                    text_to_send += f'\n<b>{calendar.month_name[bd.date.month]} 🗓</b>\n'
                    last_saved_month = bd.date.month
                text_to_send += f'<blockquote>{bd.name}: {bd.date.day} число</blockquote>' + '\n'

            if len(user.bdays) < 1:
                
                text_to_send += "Пусто...\n"

            return send(
                user, 
                text_to_send
            )  
        
            
    saveUser(user)