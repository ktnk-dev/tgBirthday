import telebot
from config import TOKEN
from datetime import datetime
import calendar
import json

from model import CDate
from markup import Markup
from changebd import save, load


bot = telebot.TeleBot(TOKEN)
markup = Markup()
chat_state = "default"
name = ""
default_mydate = CDate(month=datetime.now().month, year=datetime.now().year)
mydate = CDate(month=1, year=1000)


@bot.message_handler(commands=['start'])
def welcome_info(message):
    """
    Выводит приветственное сообщение и сбрасывает класс календаря в default
    """

    global mydate
    mydate = default_mydate.model_copy()

    data = {"objects": {}}
    save(message.chat.id, data)

    bot.send_message(
        message.chat.id,
        "Привет. Я бот для отслеживания дней рождений",
        reply_markup = markup.main()
    )


# @bot.message_handler(commands=['start'])
# def send_welcome(message):
#     """
#     Обработчик команды /start - показывает приветствие и календарь
#     """
#     welcome_text = """
# 👋 Привет! Я бот с календарем.

# Выберите дату из календаря ниже
#     """
#     global mydate
#     mydate = default_mydate.model_copy()


#     # Отправляем приветственное сообщение с календарем

#     bot.send_message(
#         message.chat.id,
#         welcome_text,
#         reply_markup=create_calendar()[0]
#     )




@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    """
    Обработчик всех сообщений для работы с календарем
    """
    global chat_state
    global name
    selected_month = mydate.month
    selected_year = mydate.year
    text = message.text

    if chat_state == "choose_name":
        name = text
        data = load(message.chat.id)

        tmp = {f"{name.lower()}": 0}
        data["objects"].update(tmp)
        
        save(message.chat.id, data)
        
        chat_state = "choose_date"

        bot.send_message(
            message.chat.id,
            "Выберете дату рождения человека",
            reply_markup=markup.calendar()
        )


    elif text == "Добавить":
        chat_state = "choose_name"
        bot.send_message(
            message.chat.id,
            "Как зовут человека?",
            reply_markup = markup.remove()
        )


    # Проверяем, является ли сообщение числом (выбранным днем)
    elif text.isdigit() and 1 <= int(text) <= 31 and chat_state == "choose_date":
        day = int(text)
        selected_date = datetime(selected_year, selected_month, day)
        
        chat_state = "default"

        data = load(message.chat.id)
        tmp = {name.lower(): selected_date.strftime('%d.%m.%Y')}
        data["objects"].update(tmp)
        save(message.chat.id, data)

        bot.send_message(
            message.chat.id,
            f"✅ Вы выбрали дату: {selected_date.strftime('%d.%m.%Y')}",
            reply_markup = markup.main()
        )
    

    elif text == "selected month":
        today = datetime.now()
        bot.send_message(
            message.chat.id,
            f"✅ Вы выбрали месяц: {selected_month}",
            reply_markup = markup.remove()
        )
    
    # Обработка навигации по месяцам
    elif "⬅️" in text:
        selected_year = selected_year if selected_month - 1 > 1 else selected_year - 1
        selected_month = selected_month - 1 if selected_month > 1 else 12

        mydate.month = selected_month
        mydate.year = selected_year

        bot.send_message(
            message.chat.id,
            "Обновляю календарь...",
            reply_markup=markup.calendar(selected_year, selected_year)
        )
    elif "➡️" in text:
        selected_year = selected_year if selected_month + 1 < 13 else selected_year + 1
        selected_month = selected_month + 1 if selected_month < 12 else 1

        mydate.month = selected_month
        mydate.year = selected_year

        bot.send_message(
            message.chat.id,
            "Обновляю календарь...",
            reply_markup=markup.calendar(selected_year, selected_year)
        )
    
    else:
        bot.send_message(
            message.chat.id,
            "Я тебя не понял"
        )



if __name__ == "__main__":
    print("Бот запущен...")
    bot.polling(none_stop=True)