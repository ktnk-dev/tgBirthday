import json
import os
from telebot.types import Message
from datetime import datetime
from pydantic import BaseModel

class State(BaseModel):
    name: str = 'default'
    date: datetime = datetime.now()

class Birthday(BaseModel):
    name: str
    date: datetime = datetime.now()

class User(BaseModel):
    id: int
    text: str = ''
    state: State = State()
    bdays: list[Birthday] = []


def getUser(message: Message):
    path = f"./users/{message.from_user.id}.json" #type: ignore
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        out = User(**data)
        out.text = message.text #type: ignore

        return out
    
    except: return User(id=message.from_user.id, text=message.text) #type: ignore

def getAllUsers() -> list[User]: # type: ignore
    for filenames in os.listdir('./users'):
        if '.json' not in filenames: continue 
        with open('./users/'+filenames, 'r', encoding='utf-8') as file:
            data = json.load(file)
            yield User(**data) #type: ignore


def saveUser(user: User):
    path = f"./users/{user.id}.json"
    with open(path, 'w', encoding='utf-8') as file:
        file.write(user.model_dump_json())