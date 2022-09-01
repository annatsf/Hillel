'''З формату snake_case 
в формат CapitalizedWords
'''
snake = input()
def snake_to_camel(snake):
        return ''.join(x.capitalize() 
        for x in snake.split('_'))
print(snake_to_camel(snake))
