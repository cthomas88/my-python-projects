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

test_board = ['#','7','8','9','4','5','6','1','2','3']
display_board(test_board)

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
        position1 = int (input('Using a number reference, where would you like to place your first move? '))
    else:
        print (f'''{player1_name}, you have chosen to use {player1_piece} 
        and have chosen to go second''')
        position1 = int (input(f"""{player2_name}, you're up first, using a number reference, where would you like to make 
        your first move? """))

first_or_second()