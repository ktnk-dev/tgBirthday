from models.user import User, getAllUsers
from models.bot import send
from datetime import datetime
from time import sleep


def loop():
    while datetime.now().hour != 7:
        sleep(1)

    while True:
        now = datetime.now()
        for user in getAllUsers():
            for bd in user.bdays:
                if [bd.date.day, bd.date.month] == [now.day, now.month]:
                    send(
                        user,
                        f"Сегодня день рождения у {bd.name}"
                    )
        sleep(86_400)