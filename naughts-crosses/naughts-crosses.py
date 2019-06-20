# create the board

def display_board(board):
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

# Define game players names

player1_name = input('What is your name player 1? ')
player2_name = input('What is your name player 2? ')

# Players choose their playing piece
def player_input():
    marker = ''
     while marker.lower() != 'X' and marker.lower != 'O':
         marker = input(f'{player1_name} please choose either X or 0: ')
    
    player1 = marker
    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    
    return (player1, player2)
    

# First or second
def first_or_second():
    choice1 = input(f'{player1_name}, would you like to go first or second? ')
    if choice1.lower() == 'first':
        print(f'''{player1_name}, you have chosen to use {player1_piece} 
        and have chosen to go first''')
        position1 = int (input('Using a number reference, where would you like to place your first move? '))
    else:
        print (f'''{player1_name}, you have chosen to use {player1_piece} 
        and have chosen to go second''')
        position1 = int (input(f"""{player2_name}, you're up first, using a number reference, where would you like to make 
        your first move? """))

first_or_second()

start_game = []

