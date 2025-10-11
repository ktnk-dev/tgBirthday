import json
from datetime import datetime


def create_date():
    date = {
        "month": datetime.now().month,
        "year": datetime.now().year
    }
    
    with open("date.json", 'w') as file:
        json.dump(date, file, indent=4)
    return 0


def get_info() -> dict:
    with open("date.json", 'r') as file:
        date = json.load(file)
    return date


def put_info(month = None, year = None):
    year = datetime.now().year if year == None else year
    date = {
        "month": month,
        "year": year
    }
        
    with open("date.json", 'w') as file:
        json.dump(date, file, indent=4)
    return 0

