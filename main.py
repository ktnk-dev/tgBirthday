from models.bot import bot
from bot import *
from event_loop import loop
from multiprocessing import Process


if __name__ == "__main__":
    p1 = Process(target=start_bot)
    p2 = Process(target=loop)
    p1.start()
    p2.start()
    p1.join()
    p2.join()