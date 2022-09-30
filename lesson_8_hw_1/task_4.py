"""Створити генератор паролів, що генерує паролі сумісні з наступними вимогами:

Пароль складається з 8 символів
В паролі допускаються лише великі та маленькі латинські літери, цифри та символ підкреслення "_"
Пароль обов'язково має містити щонайменше одну велику літеру, одну маленьку літеру та одну цифру
Не повинно бути більше 2 однакових символів підряд"""

import random
from random import sample

password = []
dictionaries = [
    "abcdefghijklmnopqrstuvwxyz",
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
    "0123456789_",
]
password = sample(dictionaries, 1)
password = [random.choice(d) for d in dictionaries] + random.choices(
    "".join(dictionaries), k=random.randint(8, 8) - 3
)
random.shuffle(password)
password = "".join(password)

print(password)
