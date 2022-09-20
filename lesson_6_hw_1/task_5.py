"""Напишіть програму, що вираховує починаючи з якої клітинки дошки раджі 
треба було віддати Nкг зерна, де N -- вводить користувач. 
Прийняти вагу однієї зернинки за 35мг. Номер клітинки виводити в 
букво-циферних традиційних шахових координатах. Наприклад: 
kilograms = 0.03584  # 35mg per seed, 1024 seeds
calculate_wheat_chess_position(kilograms)  # prints 'b3'

"""

ONE_SEED_WEIGHT = 0.035
def calculate_wheat_chess_position(kilograms):
    step = 8
    quantity = 1
    result = 0
    chess_cage_seed = kilograms / ONE_SEED_WEIGHT
    for i in range(1,9):
        
        for letter in ['a','b','c','d','e','f','g','h']:
            if i <= step:               
                result =f"{letter}{i}"            
            if chess_cage_seed <= quantity:
                return result 
            quantity *= 2
   
def main():
    entered_kilograms = float(input('Enter kg: '))
    
    print(calculate_wheat_chess_position(entered_kilograms))
if __name__ == "__main__":
    main()