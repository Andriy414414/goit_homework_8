import datetime
from datetime import datetime, timedelta

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

current_year = datetime.now().year  # поточний рік


def get_birthdays_per_week(users):
    greetings = {}
    # формуємо словник у форматі імя:день вітання
    # (якщо день народження у будній день поточного року, то тоді день вітання в той же день,
    # а якщо день народження у вихідний день поточного року, то тоді день вітання в наступний понеділок)

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y-%m-%d")
        birthday_date = birthday_date.replace(year=current_year)

        if birthday_date.weekday() >= 5:  # Субота/неділя переміщуємо на понеділок
            birthday_date += timedelta(days=(7 - birthday_date.weekday()))

        formatted_birthday = birthday_date.strftime("%Y-%m-%d")
        greetings[user["name"]] = formatted_birthday

    # print(greetings)

    next_week_dates = [
        datetime.now() + timedelta(days=i) for i in range(8)
    ]  # формуємо перелік днів потенційного вітання - поточний + 7 наступних

    for date in next_week_dates:
        day = date.strftime("%Y-%m-%d")  # переводимо формат з дататайм у стр

        names = ", ".join(
            [name for name, birthday in greetings.items() if birthday == day]
        )
        # витягнуємо імена, по яким співпадать день вітання і день з переліку днів потенційного вітання

        if names:  # якщо є імена у цей день друкуємо у потрібному форматі
            weekday_name = date.strftime("%A")
            print(f"{weekday_name}: {names}")


get_birthdays_per_week(users)
