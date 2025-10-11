import datetime
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from datetime import datetime
import calendar

def create_calendar(year=None, month=None):
    """
    Создает календарь для выбора даты
    """
    now = datetime.now()
    if year is None:
        year = now.year
    if month is None:
        month = now.month
    
    markup = ReplyKeyboardMarkup(row_width=7, resize_keyboard=True)

    # Заголовок с месяцем и годом
    month_name = calendar.month_name[month]
    markup.add(KeyboardButton(month_name))
    # markup.add(KeyboardButton("Start", web_app=WebAppInfo("http://127.0.0.1:5500/webapp/")))
    
    # Дни недели
    days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
    markup.add(*days)
    
    # Ячейки календаря
    month_calendar = calendar.monthcalendar(year, month)
    for week in month_calendar:
        row = []
        for day in week:
            if day == 0:
                row.append(" ")
            else:
                row.append(str(day))
        markup.add(*row)
    
    # Кнопки навигации
    prev_month = month - 1 if month > 1 else 12
    prev_year = year if month > 1 else year - 1
    next_month = month + 1 if month < 12 else 1
    next_year = year if month < 12 else year + 1
    
    

    markup.add(
        f"⬅️ {calendar.month_name[prev_month]}",
        "selected month" ,
        f"{calendar.month_name[next_month]} ➡️"
    )
    
    return (markup, year, month)
