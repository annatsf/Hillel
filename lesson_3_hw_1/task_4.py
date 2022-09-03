"""Taras Shevchenko*1814-03-09*1861-03-10

"""
# преобразуя string в date
text = input("")
# импортирую из модуля datetime компонент date
from datetime import date


def name_age(text, DELIMITER="*"):
    # разбираю введенную строку на части, разделенные '*';
    # с помощью fromisoformat() возвращаю дату
    # в формате YYYY-MM-DD:
    name, date_birth, date_death = text.split(DELIMITER)
    y1 = date.fromisoformat(date_birth)
    y2 = date.fromisoformat(date_death)
    age = abs(y2.year - y1.year)
    return f"Name: {name} \nAge: {age} years"


print(name_age(text, DELIMITER="*"))

"""Другой вариант

"""

# преобразую string в integer
text = input("")


def name_age(text, DELIMITER="*"):
    name, date_birth, date_death = text.split(DELIMITER)
    # дополнительно разбираю даты по
    # разделителю '-'
    y1, m1, d1 = date_birth.split("-")
    y2, m2, d2 = date_death.split("-")
    age = abs(int(y2) - int(y1))
    return f"Name: {name} \nAge: {age} years"


print(name_age(text, DELIMITER="*"))
