import random

def coin_flip():

    flip = random.randint(0, 51)

    if flip % 2 == 0:
        return True
    else:
        return False
    
def game(num):

    heads = 0
    tails = 0
    list_results = []

    for i in range(num):
        if coin_flip():
            heads += 1
            list_results.append('Heads')
        else:
            tails += 1
            list_results.append('Tails')
    
    print(f'The number of times the coin landed heads was {heads}')
    print(f'The number of times the coin landed tails was {tails}')
    print(list_results)

number_of_throws = int(input('How many times would you like to toss the coin? '))
game(number_of_throws)
