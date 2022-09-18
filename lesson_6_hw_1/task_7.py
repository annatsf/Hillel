
"""Програма випадковим чином обирає число від 1 до 10 і пропонує користувачу
 його вгадати. Користувач вводить число, а програма перевіряє його і,
  якщо користувач не вгадав, що повідомляє ви введене число більше чи менше 
  від згенерованого. 
Після цього знову просить вгадати. І так, поки користувач не вгадає."""

from random import randint

def quiz():
    hidden_number = randint(1, 10)
    while True:
        user_answer = int(input('Choose a number from 1 to 10: '))
        if user_answer < hidden_number:
            print('The number is less than expected. Please, try again!')
        if user_answer > hidden_number:
            print('The number is greater than expected. Please, try again!')
        if user_answer == hidden_number:
            print(hidden_number, 'You guessed!')




def main():

    print(quiz())

if __name__ == '__main__':
   main()

