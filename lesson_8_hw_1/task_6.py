"""Напишіть функцію, яка прийматиме рядок та перетворюватиме його способом, описаним вище. В якості алгоритму перемішування букв використовуйте наступні 
кроки для кожного слова в тексті:

- Залишаєте на місці перший та останні символи слова
- З тих, що лишилися, беремо перші символа та перемішуємо в довільному порядку
- Отриману перемішану трійку додаємо до результату
- Повторюємо з пункту 2 допоки не закінчаться неперемішані символи

"""

import random


def tramsformation_text(text):
    tmp_word = ""
    arr_tmp = []

    for i in text:
        if i.isalpha():
            tmp_word = tmp_word + i
        else:
            if len(tmp_word):
                arr_tmp.append(tmp_word)
                tmp_word = ""

            arr_tmp.append(i)

    return arr_tmp


def permtuate(text):

    converted_string = []

    for i in text:
        if i.isalpha():

            if len(i) < 4:
                converted_string = converted_string + list(i)
            else:
                tmp_word = ""
                first_letter = list(i[0])
                last_letter = list(i[-1])
                tmp_word = list(i[1:-1])
                random.shuffle(tmp_word)

                result = first_letter + tmp_word + last_letter
                converted_string = converted_string + result
        else:
            converted_string = converted_string + list(i)

    return "".join(converted_string)


def main():
    text_inp = str(input("Enter text: \n >>> "))

    print(permtuate(tramsformation_text(text_inp)))


if __name__ == "__main__":
    main()
