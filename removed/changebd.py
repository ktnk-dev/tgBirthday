import json


def load(user_id):
    path = f"./users/{user_id}.json"
    with open(path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    return data


def save(user_id, data):
    path = f"./users/{user_id}.json"
    with open(path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)