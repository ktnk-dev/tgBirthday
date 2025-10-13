from models.bot import bot
from bot import *
from event_loop import loop
# from multiprocessing import Process
from threading import Thread
import locale


try:
    locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'ru_RU')
    except locale.Error:
        try:
            locale.setlocale(locale.LC_ALL, 'Russian_Russia.1251')
        except locale.Error:
            print("Русская локаль не доступна")



if __name__ == "__main__":
    p1 = Thread(target=start_bot)
    p2 = Thread(target=loop)
    p1.start()
    p2.start()
    p1.join()
    p2.join()