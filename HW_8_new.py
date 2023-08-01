import datetime
from datetime import datetime, timedelta
from collections import defaultdict

users = [
    {"name": "Mik", "birthday": "1984-08-02"},
    {"name": "Anna", "birthday": "1984-08-02"},
    {"name": "Simon", "birthday": "1984-07-30"},
    {"name": "Alex", "birthday": "2003-08-07"},
    {"name": "Pet", "birthday": "1984-08-15"},
    {"name": "Ivet", "birthday": "1984-08-05"},
    {"name": "Rosa", "birthday": "1984-08-06"},
    {"name": "Wim", "birthday": "1986-07-30"},
    {"name": "Serg", "birthday": "2021-08-04"},
    {"name": "Alvaro", "birthday": "1986-08-01"},
]

def get_birthdays_per_week(users):
    
    current_date = datetime.now()
    
    if current_date.isoweekday() == 1:
        current_date = current_date - timedelta(days=2)
    
    end_date = current_date + timedelta(weeks=1)

    print(current_date)
    print(end_date)

    list_for_wishes = defaultdict(list)

    for user in users:
        birthday_date = current_date.fromisoformat(user["birthday"])
        birthday_date = birthday_date.replace(year=current_date.year)
                         
        if current_date <= birthday_date <= end_date:
                        
            if birthday_date.isoweekday() > 5:
                birthday_date += timedelta(days=(8 - birthday_date.isoweekday()))
            
            list_for_wishes[birthday_date].append(user['name'])
                      

    list_for_wishes_sort = dict(sorted(list_for_wishes.items()))
    print(list_for_wishes_sort)

    for key,val in list_for_wishes_sort.items():
        day = key.strftime('%A') 
        names = ", ".join(val)   
        print(f'{day}: {names}')
      

get_birthdays_per_week(users)
