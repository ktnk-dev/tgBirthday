from datetime import datetime
import calendar
import json
from depr_create_json import *

print(calendar.month_name[datetime.now().month - 2])

with open("date.json", 'r') as file:
    a = json.load(file)

print(type(a))

put_info(10, 2024)
print(get_info())