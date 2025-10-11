import json
from datetime import datetime
from pydantic import BaseModel

class State(BaseModel):
    name: str = 'default'
    date: datetime = datetime.now()

class Birthday(BaseModel):
    name: str
    date: str

class User(BaseModel):
    id: int
    state: State = State()
    bdays: list[Birthday] = []


def getUser(userid: int):
    path = f"./users/{userid}.json"
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        
        return User(**data)
    
    except: return User(id=userid)
    
def saveUser(user: User):
    path = f"./users/{user.id}.json"
    with open(path, 'w', encoding='utf-8') as file:
        file.write(user.model_dump_json())