import random

# Global variables
user_number = int(input('Please enter the number of times you would like the computer to flip your coin: '))


# Function that produces a head or tails


def coin_toss():

    heads_or_tails = random.randint(0, 51)

    if heads_or_tails %2 == 0:
        heads_or_tails = 'heads'
    else:
        heads_or_tails = 'tails'
    
    return heads_or_tails

def number_of_throws():

    