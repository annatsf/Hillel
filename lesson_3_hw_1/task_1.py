"""За допомогою третьої проміжної
змінної c
"""
a = input("a = ")
b = input("b = ")
c = a
a = b
b = c
print("a =", a)
print("b =", b)

"""Без проміжних змінних
"""
a = input("a = ")
b = input("b = ")
a, b = b, a
print("a =", a)
print("b =", b)

"""використовуючи лише арифметичні 
операції "+" та "-"
"""
a = int(input("a = "))
b = int(input("b = "))
a = a + b
b = a - b
a = a - b
print("a =", a)
print("b =", b)
