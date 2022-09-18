"""Напишіть програму, що вираховує починаючи з якої клітинки дошки раджі 
треба було віддати Nкг зерна, де N -- вводить користувач. 
Прийняти вагу однієї зернинки за 35мг. Номер клітинки виводити в 
букво-циферних традиційних шахових координатах. Наприклад: 
kilograms = 0.03584  # 35mg per seed, 1024 seeds
calculate_wheat_chess_position(kilograms)  # prints 'b3'

"""


from math import *

def calculate_wheat_chess_position(kilograms):
 
    step = 8
    num = 0
    quantity = 1
    result = 0

    for i in range(1,9):
        kilograms
        for letter in ['a','b','c','d','e','f','g','h']:
            if i <= step:               
                result =f"{letter}{i}"            
            else:
                result =f"{letter}{i- num}"                
            if kilograms <= (quantity * 0.03584):
                return result 

            quantity *= 2
    num = num + step 
  

def main():
    entered_kilograms = float(input('Enter kg: '))
    
    print(calculate_wheat_chess_position(entered_kilograms))
if __name__ == "__main__":
    main()