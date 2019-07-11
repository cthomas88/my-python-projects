import random


def flip():

    flips = random.randint(0, 51)

    if flips % 2 == 0:
        return True
    else:
        return False


def game(num):

    heads = 0
    tails = 0
    list_results = []

    for i in range(num):
        if flip():
            heads += 1
            list_results.append('Heads')
        else:
            tails += 1
            list_results.append('Tails')

    print(f"The number of times the coin landed on heads was {heads}")
    print(f"The number of times the coin landed on tails was {tails}")
    print(list_results)

user_input = int(input('Please select the number of times you would like to throw the coin: '))
game(user_input)
