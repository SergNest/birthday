import random
from datetime import datetime, timedelta, date

users = [
    {'name': 'Jhon', 'birthday': datetime(2015, 5, 26)}, 
    {'name': 'Stive', 'birthday': datetime(1949, 5, 21)},
    {'name': 'Chuck', 'birthday': datetime(2019, 5, 20)}, 
    {'name': 'David', 'birthday': datetime(1954, 5, 23)}, 
    {'name': 'Bob', 'birthday': datetime(1952, 1, 1)}, 
    {'name': 'Mike', 'birthday': datetime(1972, 12, 1)},  
    {'name': 'Chuck', 'birthday': datetime(2006, 9, 13)}, 
    {'name': 'Serg', 'birthday': datetime(1993, 3, 17)}, 
    ]

def get_random_birthdays(n):
    current_date = datetime.now()
    oldest_date = current_date - timedelta(days=365*80)
    birthdays_list = []
    for i in range(n):
        fake_year = random.randrange(oldest_date.year, current_date.year)
        fake_month = random.randint(1,12)
        fake_day = random.randint(1,31)
       
        try:
            fake_birthday = datetime(year=fake_year, month=fake_month, day=fake_day)
        except ValueError:
            continue

        if current_date >= fake_birthday:
            birthdays_list.append(fake_birthday.date())
        return birthdays_list
        
def get_name():
    return random.choice(['Serg', 'David', 'Nik', "Sasha", 'Mike', 'Bob', 'Jhon', 'Stive', 'Chuck'])

def get_list_users():
    users = []
    for i in range(10):
        users.append({'name': get_name(), 'birthday': get_random_birthdays(1)})

    return users

def get_birthdays_per_week(users):
    cur_date = datetime.now()
    cur_day = cur_date.weekday()
    
    days_ahead = (0 - cur_day) % 7
    next_monday = cur_date + timedelta(days=days_ahead)

    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    birthdays_per_week = {weekday: [] for weekday in weekdays}
    
    for us in users:
        name = us['name']
        birthday = us.get('birthday').replace(year=cur_date.year)

        if next_monday <= birthday < (next_monday + timedelta(days=7)):
            weekday_ind = (birthday - next_monday).days
            weekday = weekdays[weekday_ind]
            
            birthdays_per_week[weekday].append(name)

        elif (next_monday - timedelta(days=2)).date() <= birthday.date() < next_monday.date() :
            birthdays_per_week['Monday'].append(name)
            
    for weekday, names in birthdays_per_week.items():
        if names:
            print(f'{weekday}: {", ".join(names)}') 


get_birthdays_per_week(users)
# print(get_list_users())