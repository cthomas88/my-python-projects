# create the board

board = '''  

               |     |    
            1  |  2  |  3   
               |     |
         -------------------
               |     |    
            4  |  5  |  6   
               |     |
         -------------------
               |     |    
            7  |  8  |  9  
               |     | 
               
               '''

print (board)

# Define game players

player1_name = input('What is your name player 1? ')
player2_name = input('What is your name player 2? ')

# Players choose their playing piece

player1_piece = input(f'{player1_name} what character would you like to play? X or O ')
player2_piece = ''

if player1_piece == 'X':
    player2_piece == 'O'
else:
    player1_piece == 'O' 

# First or second

def first_or_second():
    choice1 = input(f'{player1_name}, would you like to go first or second? ')
    if choice1.lower() == 'first':
        print(f'''{player1_name}, you have chosen to use {player1_piece} 
        and have chosen to go first''')
        input('Where would you like to place your first move? ')
    else:
        print (f'''{player1_name}, you have chosen to use {player1_piece} 
        and have chosen to go second''')
        input (f"""{player2_name}, you're up first, where would you like to make 
        your first move? """)

first_or_second()

# Placing counter

def place_counter():
    pass

print(board.split())
