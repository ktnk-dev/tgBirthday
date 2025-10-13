from telebot.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from models.user import User
import calendar
from datetime import datetime


class Markup:
    @staticmethod
    def remove() -> ReplyKeyboardRemove:
        return ReplyKeyboardRemove()
    

    @staticmethod
    def main() -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("Добавить", "Удалить")
        markup.add("За месяц", "За весь год")

        return markup
    

    @staticmethod
    def calendar(month=None, year=None) -> ReplyKeyboardMarkup:
        markup = ReplyKeyboardMarkup(row_width=7, resize_keyboard=True)
        now = datetime.now()
        year = year if year else now.year
        month = month if month else now.month
        
        month_name = calendar.month_name[month]
        markup.add(KeyboardButton(month_name))
        
        days = ["Пн", "Вт", "Ср", "Чт", "Пт", "Сб", "Вс"]
        markup.add(*days)
        
        month_calendar = calendar.monthcalendar(year, month)
        for week in month_calendar:
            row = []
            for day in week:
                if day == 0:
                    row.append(" ")
                else:
                    row.append(str(day))
            markup.add(*row)

        prev_month = month - 1 if month > 1 else 12
        next_month = month + 1 if month < 12 else 1
        
        markup.add(
            f"⬅️ {calendar.month_name[prev_month]}",
            f"{calendar.month_name[next_month]} ➡️"
        )

        return markup
    

    @staticmethod
    def display_friends(user: User):
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        
        for bd in user.bdays:
            markup.add(bd.name)

        return markup


